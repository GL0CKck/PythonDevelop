from django.urls import include, path

from .views import RegisterUserApi, PostCreateViewSet, PostCreateCommentViewSet, UserVotePostViewSet, PostAPIView
from rest_framework.routers import DefaultRouter
app_name = 'mainapp'
router = DefaultRouter()
router.register('post_create', PostCreateViewSet)
router.register('comment_create', PostCreateCommentViewSet)
router.register('vote_create', UserVotePostViewSet)
urlpatterns = [
    path('registration/', RegisterUserApi.as_view(), name='register_user'),
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('api/', include(router.urls)),

]