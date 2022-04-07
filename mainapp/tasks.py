from celery import shared_task
import datetime
import pytz

from main.mainapp.models import PostNews, UserVotePost


@shared_task()
def add(x, y):
    return x * y


# @shared_task()
# def update_count_vote():
#     today = datetime.datetime.now().replace(tzinfo=pytz.utc)
#     one_day = datetime.timedelta(days=1)
#     post = PostNews.objects.all()
#     index = len(post)
#     for i in range(0, index):
#         odds = today-post[i].date_created > one_day
#         votes = UserVotePost.objects.filter(post_news=post[i].pk)
#         if odds:
#             votes.delete()
#             post[i].count_votes = 0
#             post[i].save(update_fields=['count_votes'])
#     return True