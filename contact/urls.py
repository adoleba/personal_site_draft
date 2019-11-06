from django.urls import path
from contact.views import ContactView, ThankYouView

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('thank-you/', ThankYouView.as_view(), name='thank_you')
]
