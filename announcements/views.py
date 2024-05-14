from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .models import Announcement
from .forms import AnnouncementForm


class AnnouncementList(ListView):
    model = Announcement
    ordering = '-time_in'
    template_name = 'announcements/list.html'
    context_object_name = 'announcements'
    paginate_by = 5


class AnnouncementDetail(DetailView):
    model = Announcement
    template_name = None
    context_object_name = 'announcement'


class AnnouncementCreate(CreateView):
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcements/create.html'


class AnnouncementUpdate(UpdateView):
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcements/create.html'
