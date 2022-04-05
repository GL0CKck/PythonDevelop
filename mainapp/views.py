import datetime

import pytz
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.utils import timezone
from django.http import Http404
from .models import PostNews, UserCommentPost, UserVotePost
from .serializers import RegisterSerializer, UserCommentPostSerializer, UserVotePostSerializer, PostNewsSerializer
from rest_framework.viewsets import ModelViewSet


class RegisterUserApi(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostCreateViewSet(ModelViewSet):
    queryset = PostNews.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = PostNewsSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner_news'] = self.request.user
        serializer.save()


class PostCreateCommentViewSet(ModelViewSet):
    queryset = UserCommentPost.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserCommentPostSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner_comment'] = self.request.user
        serializer.save()


class UserVotePostViewSet(ModelViewSet):
    queryset = UserVotePost.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserVotePostSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner_vote'] = self.request.user
        serializer.save()


class PostAPIView(ListAPIView):
    queryset = PostNews.objects.all()
    permission_classes = (IsAdminUser, )
    serializer_class = PostNewsSerializer


def update_count_vote(request):
    today = datetime.datetime.now().replace(tzinfo=pytz.utc)
    one_day = datetime.timedelta(days=1)
    post = PostNews.objects.all()
    index = len(post)
    for i in range(0, index):
        odds = today-post[i].date_created > one_day
        votes = UserVotePost.objects.filter(post_news=post[i].pk)
        if odds:
            votes.delete()
            post[i].count_votes = 0
            post[i].save(update_fields=['count_votes'])
    return redirect('/')