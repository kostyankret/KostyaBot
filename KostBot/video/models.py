from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def get_fields(self):
        return f"{self.name}, {self.url}"