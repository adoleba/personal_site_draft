from django.shortcuts import render
from django.views.generic.base import View


class AboutView(View):

    def get(self, request):
        return render(request, 'about/about.html')
