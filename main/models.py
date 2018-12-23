from django.db import models
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ClubList(models.Model):
	ClubName = models.CharField(max_length = 50, blank = "True")
	ClubDescription = models.TextField(max_length = 500, blank = "True")
	ClubManager1 = models.TextField(blank = "True")
	ClubManager2 = models.TextField(blank = "True")
	ClubMemberSum = models.IntegerField(blank = "True")
	ClubMember = models.ManyToManyField(User)

    #class Meta:
    #    ordering = ['-ClubMemberSum']

    #def __unicode__(self):
    #    return u"{0}".format(self.ClubName)

class Question(models.Model):
    """question
    when a user posts questions
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=300)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

    def __unicode__(self):
        return u"{0}".format(self.title)


class Comment(models.Model):
    """comments
    comments in one question
    """
    question = models.ForeignKey(Question)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    popularity = models.PositiveIntegerField(default=0)
    content = models.TextField(max_length=600)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-popularity', '-created_at']
        get_latest_by = 'created_at'

    def __unicode__(self):
        return u'Q: {0} - Comment: {1}'.format(self.question.id, self.id)


class Tag(models.Model):
    """Tag
    Tag in question
    """
    name = models.CharField(max_length=80, blank=True)

    def __unicode__(self):
        return u"{0}".format(self.name)