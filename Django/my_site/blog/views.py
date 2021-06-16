from django.shortcuts import render
from datetime import date

posts = [
    {"slug": "hike-in-the-mountains",
     "image": "mountains.jpg",
     "author": "Deepanshu",
     "date": date(2021, 7, 21),
     "title": "Mountain Hiking",
     "excerpt": """ There is nothing like the views you get when hiking in the mountains.
                    And I wasn't even prepared for what happened whilst I was enjoying the views! """,
     "content": """ 
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
            et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip 
            ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
            fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
            mollit anim id est laborum. 
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
            et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip 
            ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
            fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
            mollit anim id est laborum.
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
            et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip 
            ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
            fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
            mollit anim id est laborum.
            """
     },

    {"slug": "programming-is-fun",
     "image": "coding.jpg",
     "author": "Deepanshu",
     "date": date(2022, 3, 10),
     "title": "Programming Is Great!",
     "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened "
                "to me yesterday...",
     "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
     },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Deepanshu",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
    }
]


def starting_page(request):
    return render(request, "blog/index.html")


def all_posts(request):
    return render(request, "blog/posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
