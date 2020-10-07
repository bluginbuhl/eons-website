from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from guardian.shortcuts import get_users_with_perms


class EonsSite(models.Model):
    site_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['site_code']

        permissions = (
            ('upload_data', 'Can upload site data'),
            ('download_data', 'Can download site data'),
        )

    def users_list(self):
        return list(get_users_with_perms(self, 'can_upload'))

    def __str__(self):
        if self.name:
            return f'{self.site_code} - {self.name}'
        else:
            return f'{self.site_code}'
