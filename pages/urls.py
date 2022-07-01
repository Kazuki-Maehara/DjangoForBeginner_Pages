from django.urls import path
from .views import HomePageView, AboutPageView
from typing import Any, Callable, List


urlpatterns: List[Callable[[str, Any, str], Any]] = [
    # path("", homePageView, name="home")
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
