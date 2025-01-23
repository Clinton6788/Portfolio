from django.views.generic import TemplateView
# from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ExperiencePageView(TemplateView):
    template_name = "pages/experience.html"

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"



# def home_view(request):
#     return render(request, "pages/home.html")
