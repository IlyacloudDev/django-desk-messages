from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Announcement, Author, Comment
from .forms import AnnouncementForm, CommentForm
from .filters import AnnouncementsFilter


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
        announcements = Announcement.objects.filter(author_id=author_pk)
        filterset = AnnouncementsFilter(self.request.GET, announcements)
        return render(request, 'announcements/announcements_of_user.html', context={'announcements': announcements, 'filterset': filterset})


class CommentCreate(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'comments/create.html'

    def form_valid(self, form, *args, **kwargs):
        comment = form.save(commit=False)
        form.instance.author = Author.objects.get(author_name=self.request.user.id)
        form.instance.announcement = Announcement.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return super().form_valid(form)


class CommentDelete(DeleteView):
    model = Comment
    template_name = 'comments/delete.html'
    success_url = reverse_lazy('author_announcements')


def comment_allow(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.allowed = True
    comment.save()
    return redirect('author_announcements')
