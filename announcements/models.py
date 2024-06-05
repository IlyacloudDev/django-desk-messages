from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from ckeditor_uploader.fields import RichTextUploadingField


class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)


class Author(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name.username


class Category(models.Model):
    tanks = "TA"
    healths = "HE"
    dd = "DD"
    merchants = "ME"
    guild_masters = "GM"
    quests_givers = "QG"
    blacksmiths = "BS"
    tanners = "TN"
    potion_makers = "PM"
    spell_masters = "SM"

    POSITIONS = [
        (tanks, "Танки"),
        (healths, "Хиллы"),
        (dd, "ДД"),
        (merchants, "Торговцы"),
        (guild_masters, "Гилдмастеры"),
        (quests_givers, "Квестгиверы"),
        (blacksmiths, "Кузнецы"),
        (tanners, "Кожевники"),
        (potion_makers, "Зельевары"),
        (spell_masters, "Мастера заклинаний"),
    ]

    category_name = models.CharField(max_length=2,
                                     choices=POSITIONS,
                                     unique=True,
                                     default=tanks)

    def __str__(self):
        return self.get_category_name_display()


class Announcement(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=115)
    announcement_text = RichTextUploadingField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='announcements')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='announcements')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('announcement_detail', args=[str(self.id)])


class Comment(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField()
    allowed = models.BooleanField(default=False)

    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self, **kwargs):
        return reverse('announcement_detail', args=[str(self.announcement.id)])
