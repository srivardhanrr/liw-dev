from django.urls import path
from .views import ContactMessageView, SymposiumRequestView, SpeakerApplicationView, CourseRegistrationView, \
    CourseFinderView

urlpatterns = [
    path('contact/', ContactMessageView.as_view(), name='contact'),
    path('symposium-request/', SymposiumRequestView.as_view(), name='symposium-request'),
    path('speaker-application/', SpeakerApplicationView.as_view(), name='speaker-application'),
    path('course-registration/', CourseRegistrationView.as_view(), name='course-registration'),
    path('course-finder/', CourseFinderView.as_view(), name='course-finder'),
]
