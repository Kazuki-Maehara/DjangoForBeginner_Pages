# from django.shortcuts import render

# from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


# def homePageView(request):
#     """homePageView
#     It is a test Docstrings
#     """
#     return HttpResponse("Hello, World!")


class HomePageView(TemplateView):
    """A view for home.html"""

    template_name: str = "home.html"


class AboutPageView(TemplateView):
    """A view for about.html"""

    template_name: str = "about.html"
