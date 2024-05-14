from django.urls import path
from .views import AnnouncementList, AnnouncementCreate


urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcement_list'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create')
]
