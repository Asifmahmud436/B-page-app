from .views import HomePageView,AboutViewPage
from django.urls import path

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutViewPage.as_view(),name='about'),
]
