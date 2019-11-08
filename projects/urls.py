from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.urls import path
from projects.views import projects


urlpatterns = [
    path('', projects, name='projects')
]

