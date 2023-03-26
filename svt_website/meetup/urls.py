from django.urls import path
from .views import HomeTemplateView, MeetupDetail, ThankYouPage

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home-page'),
    path('<slug:slug>', MeetupDetail, name='meetup-detail'),
    path('thanks/<slug:slug>', ThankYouPage, name='thanks')
    # path('<slug:slug>', MeetupDetailView.as_view(), name='meetup-detail'),
    # path('registration/<slug:slug>', FormHandlingView.as_view(), name='registration-form'),
    
]
