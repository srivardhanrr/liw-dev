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
            email_subject = "Symposium Request"
            email_message = f"""
                        <p><strong>Name:</strong> {serializer.data['name']}</p>
                        <p><strong>Email:</strong> {serializer.data['email']}</p>
                        <p><strong>Message:</strong> {serializer.data['message']}</p>
                        """
            EmailThread(email_subject, email_message, ["electrochaser26@gmail.com"]).start()

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
            EmailThread(email_subject, email_message, ["srivardhan.singh.rathore@gmail.com"]).start()

            return Response({"message": "Symposium request submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeakerApplicationView(APIView):
    def post(self, request):
        serializer = SpeakerApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Application submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, html_message=None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.html_message = html_message
        threading.Thread.__init__(self)

    def run(self):
        message = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER,
                               self.recipient_list)
        message.content_subtype = "html"
        message.send(fail_silently=False)
        print(message.to)
        print(message.from_email)


class CourseRegistrationView(APIView):
    def post(self, request):
        serializer = CourseRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course registration submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseFinderView(APIView):
    def post(self, request):
        serializer = CourseFinderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course preferences submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
