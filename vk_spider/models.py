from django.db import models


class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    from_id = models.BigIntegerField()
    owner_id = models.BigIntegerField()
    date = models.DateTimeField()
    post_type = models.CharField(max_length=20)
    text = models.TextField()


class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    post = models.ForeignKey(Post)
    from_id = models.BigIntegerField()
    date = models.DateTimeField()
    text = models.TextField()
    likes = models.IntegerField()

# class Attachment (models.Model):
#


# Create your models here.
