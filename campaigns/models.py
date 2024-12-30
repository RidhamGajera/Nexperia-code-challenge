from django.db import models

class EmailCampaign(models.Model):
    title = models.CharField(max_length=255)
    csv_file = models.FileField(upload_to='uploads/')
    template = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
