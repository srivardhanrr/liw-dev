import threading
import resend
from django.core.mail import EmailMessage
from rest_framework import status, viewsets
from rest_framework.response import Response
from liwdev import settings
from .models import Blog, CaseStudy
from .serializers import ContactMessageSerializer, SymposiumRequestSerializer, SpeakerApplicationSerializer, \
    CourseRegistrationSerializer, CourseFinderSerializer, BlogSerializer, CaseStudySerializer


class BaseViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            self.send_email(serializer.data)
            return Response({"message": f"{self.success_message}"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_email(self, data):
        email_subject = self.email_subject
        email_message = self.format_email_message(data)
        EmailThread(subject=email_subject, html_content=email_message,
                    recipient_list=["electrochaser26@gmail.com", "info@leadershipinnovationworld.com"]).run()

    def format_email_message(self, data):
        raise NotImplementedError("Subclasses must implement format_email_message")


class ContactMessageViewSet(BaseViewSet):
    serializer_class = ContactMessageSerializer
    success_message = "Message sent successfully"
    email_subject = "Contact Form Request"

    def format_email_message(self, data):
        return f"""
        <p><strong>Name:</strong> {data['name']}</p>
        <p><strong>Email:</strong> {data['email']}</p>
        <p><strong>Message:</strong> {data['message']}</p>
        """


class SymposiumRequestViewSet(BaseViewSet):
    serializer_class = SymposiumRequestSerializer
    success_message = "Symposium request submitted successfully"
    email_subject = "Symposium Request"

    def format_email_message(self, data):
        return f"""
        <p><strong>Institution Name:</strong> {data['institution_name']}</p>
        <p><strong>Contact Person:</strong> {data['contact_person']}</p>
        <p><strong>Email:</strong> {data['email']}</p>
        <p><strong>Phone:</strong> {data['phone']}</p>
        <p><strong>Preferred Date:</strong> {data['preferred_date']}</p>
        <p><strong>Expected Attendees:</strong> {data['expected_attendees']}</p>
        <p><strong>Additional Info:</strong> {data['additional_info']}</p>
        """


class SpeakerApplicationViewSet(BaseViewSet):
    serializer_class = SpeakerApplicationSerializer
    success_message = "Application submitted successfully"
    email_subject = "Speaker Application"

    def format_email_message(self, data):
        return f"""
        <p><strong>Name:</strong> {data['name']}</p>
        <p><strong>Email:</strong> {data['email']}</p>
        <p><strong>Phone:</strong> {data['phone']}</p>
        <p><strong>LinkedIn:</strong> {data['linkedin']}</p>
        <p><strong>Expertise:</strong> {data['expertise']}</p>
        """


class CourseRegistrationViewSet(BaseViewSet):
    serializer_class = CourseRegistrationSerializer
    success_message = "Course registration submitted successfully"
    email_subject = "Course Registration"

    def format_email_message(self, data):
        return f"""
        <p><strong>Name:</strong> {data['name']}</p>
        <p><strong>Email:</strong> {data['email']}</p>
        <p><strong>Selected Course:</strong> {data['selected_course']}</p>
        <p><strong>Message:</strong> {data['message']}</p>
        """


class CourseFinderViewSet(BaseViewSet):
    serializer_class = CourseFinderSerializer
    success_message = "Course preferences submitted successfully"
    email_subject = "Course Preferences"

    def format_email_message(self, data):
        return f"""
        <p><strong>Career Stage:</strong> {data['career_stage']}</p>
        <p><strong>Interests:</strong> {data['interests']}</p>
        <p><strong>Time Commitment:</strong> {data['time_commitment']}</p>
        """


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    lookup_field = 'slug'


class CaseStudyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    lookup_field = 'slug'


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        resend.api_key = settings.RESEND_API_KEY
        params: resend.Emails.SendParams = {
            "from": "Leadership Innovation World <alerts@marksmanclub.in>",
            "to": self.recipient_list,
            "subject": self.subject,
            "html": self.html_content,
        }
        email = resend.Emails.send(params)
        print(email)
