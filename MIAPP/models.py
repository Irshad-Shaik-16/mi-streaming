
from django.db import models

resolution = (
    ('480p', '480p'),
    ('720p', '720p'),
    ('1080p', '1080p'),
    ('4K', '4K'),
    ('4K+HDR', '4K+HDR'),
)


class Subscriptions(models.Model):
    Plan_Name = models.CharField(max_length=20, blank=False)
    Monthly_Price = models.IntegerField(blank=False)
    Yearly_Price = models.IntegerField(blank=False)
    Video_Quality = models.CharField(max_length=10, blank=False)
    Resolution = models.CharField(
        choices=resolution, max_length=10, default="480p")
    Devices = models.CharField(blank=False, max_length=25)
    Active_Screens = models.IntegerField(blank=False)

    def __str__(self):
        return self.Plan_Name
