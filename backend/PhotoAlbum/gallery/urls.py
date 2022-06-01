# Django
from django.urls import path
from django.conf.urls import include
# Django Rest Framework
from rest_framework import routers
# Apps
from gallery import views as galleryViews

# Define routes at app

router = routers.DefaultRouter()
router.register('users'  ,  galleryViews.UsersViewSet,  basename="users")
router.register('albums' ,  galleryViews.AlbumViewSet,  basename="albums")
router.register('images' ,  galleryViews.ImageViewSet,  basename="images")
router.register('gallery',  galleryViews.GalleryViewSet,basename="gallery")


# nest routes
urlpatterns = [
    path('', include(router.urls)),
]