from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from .permissions import JWTPermission
from .models import Tweet
from .serializer import TweetSerializer, TweetCreateSerializer, TweetUpdateSerializer

# Create your views here.
class TweetLists(ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = [JWTPermission]
    # pagination_class = StandardResultsSetPagination
    ordering_fields = ['created_at', 'likes_count']

    def get_queryset(self):
        queryset = Tweet.objects.all()
        following = self.request.query_params.get('following', None)
        
        if following and following.lower() == 'true':
            # Get tweets from users that the current user follows
            user = self.request.user
            following_users = user.following.all()
            queryset = queryset.filter(user__in=following_users)
            
        return queryset

class TweetDetail(RetrieveAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    # permission_classes = [JWTPermission]
    lookup_field = 'id'
    lookup_url_kwarg = 'tweet_id'

class TweetCreate(CreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetCreateSerializer
    # permission_classes = [JWTPermission]

class TweetUpdate(UpdateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetUpdateSerializer
    # permission_classes = [JWTPermission]
    lookup_field = 'id'
    lookup_url_kwarg = 'tweet_id'

class TweetDelete(DestroyAPIView):
    queryset = Tweet.objects.all()
    # permission_classes = [JWTPermission]
    lookup_field = 'id'
    lookup_url_kwarg = 'tweet_id'