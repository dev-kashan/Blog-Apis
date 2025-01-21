from django.urls import path , include
from .views import *

urlpatterns = [
    path('all_blogs/', BlogsApi.as_view()),
    path('recent_blogs/', RecentBlogsApi.as_view()),
    path('blog_detail/<id>/', BlogDetailApi.as_view()),
    path('all_categories/', CategoryApi.as_view()),
    path('category_blog/<id>/', CategoryBlogApi.as_view()),
    # path('contact/', views.contact),
]