from django_filters import FilterSet

from .models import Announcement


class AnnouncementsFilter(FilterSet):
    class Meta:
        model = Announcement
        fields = {
            'title': ['icontains'],
        }
