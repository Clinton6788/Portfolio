from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
# from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form Valid")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            m = f"Contact Request: \nName: {name}\nEmail: {email}\nMessage: {message}"
            send_mail(subject='Contact Request',
                      message=m,
                      from_email=email,
                      recipient_list=['clinton.g.hockenberry@gmail.com'])
            
            return render(request, "pages/contact.html", {'form': ContactForm(), 'success':True})

        else:
            print("Form Invalid")
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {'form': form})




# def home_view(request):
#     return render(request, "pages/home.html")
