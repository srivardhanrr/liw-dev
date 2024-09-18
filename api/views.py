import threading

import resend
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from liwdev import settings
from .serializers import ContactMessageSerializer, SymposiumRequestSerializer, SpeakerApplicationSerializer, \
    CourseRegistrationSerializer, CourseFinderSerializer


class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email_subject = "Contact Form Request"
            email_message = f"""
                        <p><strong>Name:</strong> {serializer.data['name']}</p>
                        <p><strong>Email:</strong> {serializer.data['email']}</p>
                        <p><strong>Message:</strong> {serializer.data['message']}</p>
                        """

            EmailThread(subject=email_subject, html_content=email_message, recipient_list=["electrochaser26@gmail.com", "info@leadershipinnovationworld.com"]).run()
            return Response({"message": "Message sent successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SymposiumRequestView(APIView):
    def post(self, request):
        serializer = SymposiumRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email_subject = "Symposium Request"
            email_message = f"""
            <p><strong>Institution Name:</strong> {serializer.data['institution_name']}</p>
            <p><strong>Contact Person:</strong> {serializer.data['contact_person']}</p>
            <p><strong>Email:</strong> {serializer.data['email']}</p>
            <p><strong>Phone:</strong> {serializer.data['phone']}</p>
            <p><strong>Preferred Date:</strong> {serializer.data['preferred_date']}</p>
            <p><strong>Expected Attendees:</strong> {serializer.data['expected_attendees']}</p>
            <p><strong>Additional Info:</strong> {serializer.data['additional_info']}</p>
            """
            EmailThread(subject=email_subject, html_content=email_message, recipient_list=["electrochaser26@gmail.com", "info@leadershipinnovationworld.com"]).run()
            return Response({"message": "Symposium request submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeakerApplicationView(APIView):
    def post(self, request):
        serializer = SpeakerApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email_subject = "Speaker Application"
            email_message = f"""
            <p><strong>Name:</strong> {serializer.data['name']}</p>
            <p><strong>Email:</strong> {serializer.data['email']}</p>
            <p><strong>Phone:</strong> {serializer.data['phone']}</p>
            <p><strong>LinkedIn:</strong> {serializer.data['linkedin']}</p>
            <p><strong>Expertise:</strong> {serializer.data['expertise']}</p>
            """
            EmailThread(subject=email_subject, html_content=email_message, recipient_list=["electrochaser26@gmail.com", "info@leadershipinnovationworld.com"]).run()
            return Response({"message": "Application submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseRegistrationView(APIView):
    def post(self, request):
        serializer = CourseRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email_subject = "Course Registration"
            email_message = f"""
            <p><strong>Name:</strong> {serializer.data['name']}</p>
            <p><strong>Email:</strong> {serializer.data['email']}</p>
            <p><strong>Selected Course:</strong> {serializer.data['selected_course']}</p>
            <p><strong>Message:</strong> {serializer.data['message']}</p>
            """
            EmailThread(subject=email_subject, html_content=email_message, recipient_list=["electrochaser26@gmail.com", "info@leadershipinnovationworld.com"]).run()
            return Response({"message": "Course registration submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseFinderView(APIView):
    def post(self, request):
        serializer = CourseFinderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email_subject = "Course Preferences"
            email_message = f"""
            <p><strong>Career Stage:</strong> {serializer.data['career_stage']}</p>
            <p><strong>Interests:</strong> {serializer.data['interests']}</p>
            <p><strong>Time Commitment:</strong> {serializer.data['time_commitment']}</p>
            """
            EmailThread(subject=email_subject, html_content=email_message, recipient_list=["electrochaser26@gmail.com", "info@leadershipinnovationworld.com"]).run()
            return Response({"message": "Course preferences submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        # threading.Thread.__init__(self)

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



