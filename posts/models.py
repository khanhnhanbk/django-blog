from django.db import models
import datetime
import timeago

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_time_ago(self):
        now = datetime.datetime.now(tz=self.date.tzinfo)
        return timeago.format(self.date, now, "en_short")
