from django.core import mail
from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse
from django.contrib.messages.storage.fallback import FallbackStorage
from .views import contact
from .models import ContactMessage


class ContactAndResumeTests(TestCase):
    def test_contact_page_shows_profile_links_and_message_form(self):
        request = RequestFactory().get(reverse("contact"))
        request.session = {}
        request._messages = FallbackStorage(request)

        response = contact(request)
        content = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertIn("Full Name", content)
        self.assertIn("Send Me a Message", content)
        self.assertIn("https://www.linkedin.com/in/lwazi-gumede-425307164/", content)
        self.assertIn(reverse("download_resume"), content)

    @override_settings(
        EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
        ADMIN_EMAIL="owner@example.com",
    )
    def test_contact_form_saves_message_and_emails_site_owner(self):
        request = RequestFactory().post(
            reverse("contact"),
            data={
                "name": "A. Visitor",
                "email": "visitor@example.com",
                "phone": "+27 11 123 4567",
                "subject": "Engineering opportunity",
                "message": "I would like to discuss a role.",
            },
        )
        request.session = {}
        request._messages = FallbackStorage(request)
        response = contact(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("contact"))
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ["owner@example.com"])
        self.assertIn("A. Visitor", mail.outbox[0].body)
        self.assertIn("I would like to discuss a role.", mail.outbox[0].body)

    def test_resume_pdf_links_to_linkedin(self):
        response = self.client.get(reverse("download_resume"))

        self.assertEqual(response["Content-Type"], "application/pdf")
        self.assertIn(
            b"https://www.linkedin.com/in/lwazi-gumede-425307164/",
            response.content,
        )
