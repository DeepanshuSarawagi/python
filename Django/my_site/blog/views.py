from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm

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


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]  # We are sorting the Posts in descending order on date
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })
# Commented above code since we are converting the fn view to class based view


class StartingPage(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"  # By default the context name is "object_list". "We are changing it to 'posts'"
    
    def get_queryset(self):
        queryset = super(StartingPage, self).get_queryset()
        data = queryset[:3]
        return data


# def all_posts(request):
#     posts = Post.objects.all()
#     return render(request, "blog/posts.html", context={
#         "posts": posts
#     })
# Commented above code since we are converting all_posts view to class based view


class AllPostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


# def post_detail(request, slug):
#     # posts = Post.objects.all()
#     # identified_post = next(post for post in posts if post['slug'] == slug)
#
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", context={
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })
# Commented above code to convert the post_detail view to class based view


# class SinglePostView(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post
#
#     def get_context_data(self, **kwargs):
#         context = super(SinglePostView, self).get_context_data()
#         context["post_tags"] = self.object.tags.all()
#         context["comment_form"] = CommentForm()
#         return context


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),  # getting all post tags
            "comment_form": CommentForm()  # creating content form
        }
        return render(request, "blog/post-detail.html", context=context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/posts.html", context=context)
