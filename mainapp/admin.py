from django.contrib import admin


from .models import PostNews, UserVotePost, UserCommentPost, User

admin.site.register(User,)
admin.site.register(PostNews,)
admin.site.register(UserVotePost,)
admin.site.register(UserCommentPost,)
