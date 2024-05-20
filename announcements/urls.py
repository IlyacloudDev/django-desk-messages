from django.urls import path
from .views import (AnnouncementList, AnnouncementDetail,
                    AnnouncementCreate, AnnouncementUpdate,
                    AuthorAnnouncementList, CommentCreate,
                    CommentDelete, comment_allow
                    )


urlpatterns = [
    path('', AnnouncementList.as_view(), name='announcement_list'),
    path('<int:pk>/', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create'),
    path('update/<int:pk>/', AnnouncementUpdate.as_view(), name='announcement_update'),
    path('own/profile/', AuthorAnnouncementList.as_view(), name='author_announcements'),
    path('comment/<int:pk>/create', CommentCreate.as_view(), name='comment_create'),
    path('delete/<int:pk>/comment', CommentDelete.as_view(), name='comment_delete'),
    path('allow/<int:pk>/comment', comment_allow, name='comment_allow')
]
