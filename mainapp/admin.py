from django.contrib import admin

from .models import PostNews, User, UserCommentPost, UserVotePost

admin.site.register(
    User,
)
admin.site.register(
    PostNews,
)
admin.site.register(
    UserVotePost,
)
admin.site.register(
    UserCommentPost,
)
