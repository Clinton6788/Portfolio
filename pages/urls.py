from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ExperiencePageView,
    contact_view,)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("experience/", ExperiencePageView.as_view(), name="experience"),
    path("contact/", contact_view, name="contact"),
]