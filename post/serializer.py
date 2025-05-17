from rest_framework import serializers
from .models import Tweet
from django.contrib.auth import get_user_model


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        # fields = ['id', 'content', 'created_at', 'user'] #, 'likes_count', 'retweets_count']
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'likes_count', 'retweets_count']

class TweetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content', 'user', 'parent_tweet', 'retweeted_tweet']

class TweetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']