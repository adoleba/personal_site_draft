from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('', include('homepage.urls')),

    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path(_('about/'), include('about.urls')),
    path(_('contact/'), include('contact.urls')),
    path(_('projects/'), include('projects.urls')),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
