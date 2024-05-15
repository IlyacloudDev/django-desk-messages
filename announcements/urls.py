from django.urls import path
from .views import AnnouncementList, AnnouncementDetail, AnnouncementCreate, AnnouncementUpdate


urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcement_list'),
    path('<int:pk>/', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create'),
    path('update/<int:pk>/', AnnouncementUpdate.as_view(), name='announcement_update'),
]
