from django.contrib import admin
from django.urls import path, include
from lesson.api.views import PostViewset
from lesson.api.views import post_detail, post_list
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewset)


urlpatterns = [
    path('api/', include(router.urls)),
    path('posts/', post_list, name="posts"),
    path('post/<int:pk>/', post_detail, name='detail'),
]
