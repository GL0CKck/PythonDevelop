from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Имя пользователя должно быть указанно')
        if not email:
            raise ValueError('Почта пользователя должна быть указанна')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(self, username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=55, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', )

    def __str__(self):
        return self.email


class PostNews(models.Model):
    title_news = models.CharField(max_length=128)
    owner_news = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_posts')
    link = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    count_votes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title_news


class UserCommentPost(models.Model):
    owner_comment = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='my_comments')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    post_news = models.ForeignKey(PostNews, on_delete=models.CASCADE)


class UserVotePost(models.Model):
    post_news = models.ForeignKey(PostNews, on_delete=models.CASCADE)
    owner_vote = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)



