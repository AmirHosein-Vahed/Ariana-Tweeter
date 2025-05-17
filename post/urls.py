from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.TweetLists.as_view(), name='list_tweet'),
    path('<int:tweet_id>/', views.TweetDetail.as_view(), name='detail_tweet'),
    path('create/', views.TweetCreate.as_view(), name='create_tweet'),
    path('update/<int:tweet_id>', views.TweetUpdate.as_view(), name='update_tweet'),
    path('delete/<int:tweet_id>', views.TweetDelete.as_view(), name="delete_tweet"),
]