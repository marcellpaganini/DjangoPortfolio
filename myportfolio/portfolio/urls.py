from django.urls import path
from . import views


app_name = 'portfolio'
urlpatterns = [
    # project views
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:project>/',
         views.project_detail,
         name='project_detail'),
]
