from django.shortcuts import render
from django.views.generic.base import View


class ProjectsView(View):

    def get(self, request):
        return render(request, 'projects/projects.html')
