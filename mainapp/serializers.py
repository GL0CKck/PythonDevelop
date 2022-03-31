from rest_framework import serializers

from .models import PostNews, UserVotePost, UserCommentPost, User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserCommentPostSerializer(serializers.ModelSerializer):
    owner_comment = serializers.CharField(source='owner_comment.username', default='', read_only=True)

    class Meta:
        model = UserCommentPost
        fields = ('owner_comment', 'content', 'date_created', 'post_news')


class UserVotePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserVotePost
        fields = ('post_news', 'owner_vote', 'like')


class PostNewsSerializer(serializers.ModelSerializer):
    owner_news = serializers.CharField(source='owner_news.username', default='', read_only=True)

    class Meta:
        model = PostNews
        fields = ('title_news', 'owner_news', 'text_news', 'date_created', 'count_votes')