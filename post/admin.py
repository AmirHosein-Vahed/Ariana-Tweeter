from django.contrib import admin
from .models import Tweet

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'parent_tweet', 'retweeted_tweet')
    search_fields = ('user__username', 'content')
    list_filter = ('created_at',)

