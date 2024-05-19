from django.urls import path
from .views import (AnnouncementList, AnnouncementDetail,
                    AnnouncementCreate, AnnouncementUpdate,
                    AuthorAnnouncementList, CommentCreate)


urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcement_list'),
    path('<int:pk>/', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create'),
    path('update/<int:pk>/', AnnouncementUpdate.as_view(), name='announcement_update'),
    path('own/', AuthorAnnouncementList.as_view(), name='author_announcements'),
    path('comment/<int:pk>/create', CommentCreate.as_view(), name='comment_create')
]
