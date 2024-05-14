from django.views.generic import ListView, CreateView, UpdateView

from .models import Announcement
from .forms import AnnouncementForm


class AnnouncementList(ListView):
    model = Announcement
    ordering = '-time_in'
    template_name = 'announcements/list.html'
    context_object_name = 'announcements'
    paginate_by = 5


class AnnouncementCreate(CreateView):
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcements/create.html'
