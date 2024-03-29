from django.urls import path
from django.utils.translation import gettext_lazy as _

from contact.views import ContactView, ThankYouView

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path(_('thank-you/'), ThankYouView.as_view(), name='thank_you')
]

