from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.
def project_list(request):
    projects = Project.published.all()
    return render(request,
                  'portfolio/project/list.html',
                  {'projects': projects})


def project_detail(request, year, month, day, project):
    project = get_object_or_404(Project, slug=project,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,
                  'portfolio/project/detail.html',
                  {'project': project})
