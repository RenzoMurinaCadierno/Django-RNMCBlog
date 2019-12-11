from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):

    # links the author to the only authorized user (SUser) as a FK
    author = models.ForeignKey('auth.User')

    title = models.CharField(max_length=200)

    text = models.TextField()

    # timezone.now() will be taken from settings.py ('UTC')
    create_date = models.DateTimeField(default=timezone.now)

    # you can leave this blank or set it tu None
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ Sets publish_date to current UTC and saves it """
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        """
        Returns all comments filtered by approval.
        'approved_comment' comes from Comment class attribute.
        """
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        """ After creating a post, reverse the user to post_detail
        view with the PK set for that created post in the URL """
        return reverse('post_detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):

    # link the comment to the post they are called from
    post = models.ForeignKey('blog.Post', related_name='comments')

    author = models.CharField(max_length=80)

    text = models.TextField()

    create_date = models.DateTimeField(default=timezone.now())

    # a boolean to set the comment to approved.
    # > this attrribute links to Post() via its method.
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """ Sets the comment to approved and saves it """
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        """ After commenting, reverse the author to the list of all
        comments for that post """
        return reverse('post_list')

    def __str__(self):
        return self.text
