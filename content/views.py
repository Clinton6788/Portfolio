from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

class ProjectListView(TemplateView):
    template_name = "content/projects_list.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = (
            Project.objects.all
        )
        return context
    

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect("projects_list")
    else:
        form = ProjectForm()

    return render(request, "content/project_new.html", {"form": form})
