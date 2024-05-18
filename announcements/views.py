from django.views.generic import View, ListView, CreateView, UpdateView, DetailView
from django.shortcuts import render

from .models import Announcement, Author
from .forms import AnnouncementForm


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


class AnnouncementCreate(CreateView):
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcements/create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.author = Author.objects.get(author_name=self.request.user.id)
        post.save()
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
        author_pk = Author.objects.get(pk=user_id).id
        announcements = Announcement.objects.filter(author_id=author_pk)
        return render(request, 'announcements/announcements_of_user.html', context={'announcements': announcements})
