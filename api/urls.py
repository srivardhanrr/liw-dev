from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, SymposiumRequestViewSet, SpeakerApplicationViewSet, \
    CourseRegistrationViewSet, CourseFinderViewSet, BlogViewSet, CaseStudyViewSet

router = DefaultRouter()
router.register(r'contact', ContactMessageViewSet, basename='contact')
router.register(r'symposium-request', SymposiumRequestViewSet, basename='symposium-request')
router.register(r'speaker-application', SpeakerApplicationViewSet, basename='speaker-application')
router.register(r'course-registration', CourseRegistrationViewSet, basename='course-registration')
router.register(r'course-finder', CourseFinderViewSet, basename='course-finder')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'case-studies', CaseStudyViewSet, basename='case-study')

urlpatterns = [
    path('', include(router.urls)),
]
