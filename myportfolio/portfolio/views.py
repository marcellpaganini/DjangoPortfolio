from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.views.generic import ListView


# Create your views here.
def project_list(request):
    object_list = Project.published.all()
    paginator = Paginator(object_list, 3)  # 3 projects in each page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is note an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)
    return render(request,
                  'portfolio/project/list.html',
                  {'page': page,
                   'projects': projects})


def project_detail(request, year, month, day, project):
    project = get_object_or_404(Project, slug=project,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,
                  'portfolio/project/detail.html',
                  {'project': project})


class ProjectListView(ListView):
    queryset = Project.published.all()
    context_object_name = 'projects'
    paginate_by = 3
    template_name = 'portfolio/project/list.html'
