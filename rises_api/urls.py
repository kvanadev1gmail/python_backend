from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rises_api import views



router = DefaultRouter()

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
