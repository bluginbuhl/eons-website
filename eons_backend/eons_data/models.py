from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from guardian.shortcuts import get_users_with_perms


User = get_user_model()

class EonsSite(models.Model):
    site_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # eons_data = models.ManyToOneRel(EonsBaseData)

    class Meta:
        ordering = ['site_code']

        permissions = (
            ('upload_data', 'Can upload site data'),
            ('download_data', 'Can download site data'),
        )

        verbose_name = "EONS Site"
        verbose_name_plural = "EONS Sites"

    def users_list(self):
        return list(get_users_with_perms(self, 'can_upload'))

    def __str__(self):
        if self.name:
            return f'{self.site_code} - {self.name}'
        else:
            return f'{self.site_code}'


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    date = str(instance.uploaded_date).split('.')[0].replace('-', '')
    site_code = str(instance.site_code).split('-')[0].strip()
    new_name = f"eons_csvs/unprocessed/{date}_{site_code}.{ext}"
    return new_name

class EonsCsv(models.Model):
    site_code = models.ForeignKey(EonsSite, on_delete=models.PROTECT)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    file_name = models.FileField(upload_to=content_file_name, max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activated = models.BooleanField(default=False)

    class Meta:
        verbose_name = "EONS CSV"
        verbose_name_plural = "EONS CSVs"

    def set_activated(self, value):
        try: 
            flag = bool(value)
        except Exception as e:
            print(f'Error: {e}')
        self.activated = flag

    # def get_success_url(self):
    #     return reverse('home')

    def __str__(self):
        return f"{self.file_name.name.split('/')[-1]}"

class EonsBaseData(models.Model):
    site = models.ForeignKey(EonsSite, on_delete=models.PROTECT)
    utc_datetime = models.DateTimeField()
    local_datetime = models.DateTimeField(null=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    battery_voltage = models.DecimalField(max_digits=4, decimal_places=2)
    surf_brightness = models.FloatField()
    init_subs = models.FloatField()
    sky_counts = models.IntegerField(null=True)
    sky_brightness_discard = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sky_led_counts = models.IntegerField(null=True)
    moon_phase_deg = models.DecimalField(max_digits=6, decimal_places=1)
    moon_elev_deg = models.DecimalField(max_digits=6, decimal_places=3, default=0.00)
    moon_illum_percent = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        verbose_name = "EONS Datum"
        verbose_name_plural = "EONS Data"

        unique_together = [['site', 'utc_datetime']]

    def __str__(self):
        return f"{self.utc_datetime}"