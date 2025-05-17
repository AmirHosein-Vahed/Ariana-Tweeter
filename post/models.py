from django.db import models
from django.conf import settings

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tweets",
        help_text="The user who created this tweet"
    )
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_tweet = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="replies"
    )
    retweeted_tweet = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="retweets"
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_tweets",
        blank=True
    )
    # dislikes = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL,
    #     related_name="liked_tweets",
    #     blank=True
    # )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"
    
    def is_reply(self):
        """Checks if the tweet is a reply."""
        return self.parent_tweet is not None

    def is_retweet(self):
        """Checks if the tweet is a retweet."""
        return self.retweeted_tweet is not None

    def like_count(self):
        """Returns the number of likes."""
        return self.likes.count()
    
    # def dislike_count(self):
    #     """Returns the number of likes."""
    #     return self.dislikes.count()

    def reply_count(self):
        """Returns the number of replies."""
        return self.replies.count()

    def retweet_count(self):
        """Returns the number of retweets."""
        return self.retweets.count()