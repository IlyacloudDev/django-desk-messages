from django.urls import path
from .views import (ConfirmUser, AnnouncementList,
                    AnnouncementDetail, AnnouncementCreate,
                    AnnouncementUpdate, AnnouncementDelete,
                    AuthorAnnouncementList, CommentCreate,
                    CommentDelete, comment_allow,
                    CommentList,
                    )


urlpatterns = [
    path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
    path('', AnnouncementList.as_view(), name='announcement_list'),
    path('<int:pk>/', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('create/', AnnouncementCreate.as_view(), name='announcement_create'),
    path('update/<int:pk>/', AnnouncementUpdate.as_view(), name='announcement_update'),
    path('delete/<int:pk>', AnnouncementDelete.as_view(), name='announcement_delete'),
    path('own/profile/', AuthorAnnouncementList.as_view(), name='author_announcements'),
    path('comment/<int:pk>/create', CommentCreate.as_view(), name='comment_create'),
    path('delete/<int:pk>/comment', CommentDelete.as_view(), name='comment_delete'),
    path('allow/<int:pk>/comment', comment_allow, name='comment_allow'),
    path('list/filtering/comment/', CommentList.as_view(), name='comment_list_filter')
]
