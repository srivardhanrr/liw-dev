from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from api.models import ContactMessage, SymposiumRequest, SpeakerApplication, CourseRegistration, CourseFinder, Blog, \
    CaseStudy


# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


class SymposiumRequestAdmin(admin.ModelAdmin):
    list_display = ('institution_name', 'contact_person', 'phone')


class SpeakerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'selected_course')


class CourseFinderAdmin(admin.ModelAdmin):
    list_display = ('career_stage', 'interests')


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(
                config_name='extends',
                attrs={'class': 'django_ckeditor_5'},  # Use the config named 'extends' that we defined in settings.py
            )
        }


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'description', 'content', 'slug')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('created_at',)
        return self.readonly_fields


class CaseStudyForm(forms.ModelForm):
    class Meta:
        model = CaseStudy
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(
                config_name='extends',
                attrs={'class': 'django_ckeditor_5'},  # Use the config named 'extends' that we defined in settings.py
            )
        }


class CaseStudyAdmin(admin.ModelAdmin):
    form = CaseStudyForm
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'content', 'slug')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('created_at',)
        return self.readonly_fields


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(SymposiumRequest, SymposiumRequestAdmin)
admin.site.register(SpeakerApplication, SpeakerApplicationAdmin)
admin.site.register(CourseRegistration, CourseRegistrationAdmin)
admin.site.register(CourseFinder, CourseFinderAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(CaseStudy, CaseStudyAdmin)
