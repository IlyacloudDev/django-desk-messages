from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Announcement, Author, Comment
from .forms import AnnouncementForm, CommentForm
from .filters import AnnouncementsFilter, CommentFilter
from .tasks import comment_created, comment_accept


class AnnouncementList(ListView):
    model = Announcement
    ordering = '-time_in'
    template_name = 'announcements/list.html'
    context_object_name = 'announcements'
    paginate_by = 4


class AnnouncementDetail(DetailView):
    model = Announcement
    template_name = 'announcements/detail.html'
    context_object_name = 'announcement'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments'] = Comment.objects.filter(announcement=self.kwargs['pk'], allowed=True)
        return context


class AnnouncementCreate(CreateView):
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcements/create.html'

    def form_valid(self, form):
        announcement = form.save(commit=False)
        form.instance.author = Author.objects.get(author_name=self.request.user.id)
        announcement.save()
        return super().form_valid(form)


class AnnouncementUpdate(UpdateView):
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcements/create.html'

    def form_valid(self, form):
        form.instance.author = Author.objects.get(author_name=self.request.user.id)
        return super().form_valid(form)


class AuthorAnnouncementList(View):
    def get(self, request):
        current_user = request.user
        user_id = current_user.id
        author_pk = Author.objects.get(author_name=user_id).id
        announcements = Announcement.objects.filter(author_id=author_pk).order_by('-time_in')
        filterset = AnnouncementsFilter(self.request.GET, queryset=announcements)
        return render(request, 'announcements/announcements_of_user.html', context={'filterset': filterset})


class CommentCreate(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'comments/create.html'

    def form_valid(self, form, *args, **kwargs):
        comment = form.save(commit=False)
        form.instance.author = Author.objects.get(author_name=self.request.user.id)
        form.instance.announcement = Announcement.objects.get(pk=self.kwargs['pk'])
        author_of_comment_id = Author.objects.get(author_name=self.request.user.id).author_name.id
        if author_of_comment_id == comment.announcement.author.author_name.id:
            comment.allowed = True
            comment.save()
        else:
            comment.save()
            comment_created.delay(comment.pk)
        return super().form_valid(form)


class CommentDelete(DeleteView):
    model = Comment
    template_name = 'comments/delete.html'
    success_url = reverse_lazy('author_announcements')


def comment_allow(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.allowed = True
    comment.save()
    comment_accept.delay(comment.pk)
    return redirect('author_announcements')


class CommentList(ListView):
    model = Comment
    template_name = 'comments/list_filter.html'

    def get_queryset(self):
        queryset = Comment.objects.filter(announcement__author__author_name=self.request.user.id)
        self.filterset = CommentFilter(self.request.GET, queryset, request=self.request.user.id)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
