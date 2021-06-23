from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post

# posts = [
#     {"slug": "hike-in-the-mountains",
#      "image": "mountains.jpg",
#      "author": "Deepanshu",
#      "date": date(2021, 7, 21),
#      "title": "Mountain Hiking",
#      "excerpt": """ There is nothing like the views you get when hiking in the mountains.
#                     And I wasn't even prepared for what happened whilst I was enjoying the views! """,
#      "content": """
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
#             ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
#             fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
#             mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
#             ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
#             fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
#             mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
#             ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
#             fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
#             mollit anim id est laborum.
#             """
#      },
#
#     {"slug": "programming-is-fun",
#      "image": "coding.jpg",
#      "author": "Deepanshu",
#      "date": date(2022, 3, 10),
#      "title": "Programming Is Great!",
#      "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened "
#                 "to me yesterday...",
#      "content": """
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#     """
#      },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Deepanshu",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#     """
#     }
# ]


def get_date(post):
    return post['date']


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]  # We are sorting the Posts in descending order on date
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def all_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/posts.html", context={
        "posts": posts
    })


def post_detail(request, slug):
    # posts = Post.objects.all()
    # identified_post = next(post for post in posts if post['slug'] == slug)

    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", context={
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
