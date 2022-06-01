
from django.contrib import admin
from django.urls import path,include
from gallery import views as galleryViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include('gallery.urls')),
    path('auth/',galleryViews.UserAuthToken.as_view()),
]
