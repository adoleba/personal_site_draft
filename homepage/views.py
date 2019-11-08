from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import translation


def index(request):
    return render(request, 'homepage/index.html')


def set_language(request):
    language = request.POST.get('language', settings.LANGUAGE_CODE)
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language
    return redirect('index')
