from django.test import TestCase
from .models import Video

class VideoTestCase(TestCase):
    def test_fields(self):
        video1 = Video.objects.create(name="psy gagnam", url="takoi-to")
        self.assertEqual(video1.get_fields(), "psy gagnam, takoi-to")

    def test_model_name(self):
        video1 = Video.objects.create(name="tigr", url="krutoi")
        self.assertEqual(video1.name, "tigr")

    def test_model_url(self):
        video1 = Video.objects.create(name="tigr", url="krutoi")
        self.assertEqual(video1.url, "krutoi")