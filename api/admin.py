from django.contrib import admin

from api.models import ContactMessage, SymposiumRequest, SpeakerApplication, CourseRegistration, CourseFinder


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


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(SymposiumRequest, SymposiumRequestAdmin)
admin.site.register(SpeakerApplication, SpeakerApplicationAdmin)
admin.site.register(CourseRegistration, CourseRegistrationAdmin)
admin.site.register(CourseFinder, CourseFinderAdmin)
