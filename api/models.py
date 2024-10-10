from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = ResizedImageField(size=[200, 200], upload_to='testimonials/', blank=True,
                              force_format='WEBP', quality=75)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SymposiumRequest(models.Model):
    institution_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    preferred_date = models.DateField(null=True, blank=True)
    expected_attendees = models.PositiveIntegerField(null=True, blank=True)
    additional_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.institution_name} - {self.contact_person}"


class SpeakerApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField()
    expertise = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.expertise[:30]}"


class CourseRegistration(models.Model):
    COURSE_CHOICES = [
        ('leadership', 'Leadership and Management'),
        ('personal', 'Personal Development'),
        ('marketing', 'Marketing and Sales'),
        ('hr', 'Human Resources'),
        ('organizational', 'Organizational Essentials'),
        ('administrative', 'Administrative Skills'),
        ('professional', 'Professional Advancement'),
        ('career', 'Advanced Career Building'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    selected_course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_selected_course_display()}"


class CourseFinder(models.Model):
    CAREER_STAGES = [
        ('Early Career', 'Early Career'),
        ('Mid-Level', 'Mid-Level'),
        ('Senior Executive', 'Senior Executive'),
        ('Career Transition', 'Career Transition'),
    ]

    TIME_COMMITMENTS = [
        ('1-3 months', '1-3 months'),
        ('3-6 months', '3-6 months'),
        ('6-12 months', '6-12 months'),
        ('1+ year', '1+ year'),
    ]

    career_stage = models.CharField(max_length=50, choices=CAREER_STAGES)
    interests = models.JSONField()  # This will store the list of interests
    time_commitment = models.CharField(max_length=20, choices=TIME_COMMITMENTS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.career_stage} - {self.time_commitment}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = ResizedImageField(size=[1080, 1080], upload_to='blogs/', blank=True,
                              force_format='WEBP', quality=75)
    description = models.TextField(blank=True)
    content = CKEditor5Field('Content', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content = CKEditor5Field('Content', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
