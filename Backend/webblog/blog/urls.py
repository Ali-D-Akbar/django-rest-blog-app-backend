from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from blog import views

router = DefaultRouter()
router.register(r'blog', views.BlogAPI)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
