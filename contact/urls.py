from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.utils.translation import gettext_lazy as _

from contact.views import ContactView, ThankYouView

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('thank-you/', ThankYouView.as_view(), name='thank_you')
]

