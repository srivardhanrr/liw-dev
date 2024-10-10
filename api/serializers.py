from rest_framework import serializers
from .models import ContactMessage, SymposiumRequest, SpeakerApplication, CourseRegistration, CourseFinder, Blog, \
    CaseStudy, Testimonial


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['name', 'position', 'image', 'content', 'created_at']


class SymposiumRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymposiumRequest
        fields = ['institution_name', 'contact_person', 'email', 'phone', 'preferred_date', 'expected_attendees',
                  'additional_info']


class SpeakerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerApplication
        fields = ['name', 'email', 'phone', 'linkedin', 'expertise']


class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = ['name', 'email', 'selected_course', 'message']


class CourseFinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFinder
        fields = ['career_stage', 'interests', 'time_commitment']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'description', 'content', 'created_at', 'updated_at', 'slug']


class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = ['id', 'title', 'description', 'content', 'created_at', 'updated_at', 'slug']
