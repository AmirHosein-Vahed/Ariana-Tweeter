from django.shortcuts import render

# Create your views here.
# # To make user1 follow user2
# user1.following.add(user2)
# # Or using the helper method:
# user1.follow(user2)

# # To make user1 unfollow user2
# user1.following.remove(user2)
# # Or using the helper method:
# user1.unfollow(user2)

# # To check if user1 is following user2
# is_following = user1.following.filter(pk=user2.pk).exists()
# # Or using the helper method:
# is_following = user1.is_following(user2)

# # To get all users that user1 is following
# users_followed_by_user1 = user1.following.all()

# # To get all users that are following user1 (using the related_name)
# users_following_user1 = user1.followers.all()
# # Or using the helper method:
# is_followed = user1.is_followed_by(user2) # Checks if user2 is following user1

