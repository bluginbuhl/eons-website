from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from guardian.shortcuts import get_users_with_perms


User = get_user_model()

class EonsStation(models.Model):
    station_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    info = models.TextField(null=True, max_length=2500)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['station_code']

        permissions = (
            ('upload_data', 'Can upload station data'),
            ('download_data', 'Can download station data'),
        )

        verbose_name = "EONS Station"
        verbose_name_plural = "EONS Stations"

    def users_list(self):
        return list(get_users_with_perms(self, 'can_upload'))

    def sensors_list(self):
        return list(EonsSensor.objects.filter(station_code=self.station_code))

    def __str__(self):
        if self.name:
            return f'{self.station_code} - {self.name}'
        else:
            return f'{self.site_code}'

class EonsSensor(models.Model):
    sensor_id = models.CharField(max_length=10, primary_key=True)
    station_code = models.ForeignKey(EonsStation, on_delete=models.PROTECT, related_name='sensors')
    is_snow_sensor = models.BooleanField(default=False)

    class Meta:
        ordering = ['station_code']
        
        verbose_name = "EONS Sensor",
        verbose_name_plural = "EONS Sensors"

    def __str__(self):
        return f"{self.sensor_id}"


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    date = str(instance.uploaded_date).split('.')[0].replace('-', '')
    station_code = str(instance.site_code).split('-')[0].strip()
    new_name = f"eons_csvs/{station_code}/{date}_{site_code}.{ext}"
    return new_name

class EonsCsv(models.Model):
    station_code = models.ForeignKey(EonsStation, on_delete=models.PROTECT, null=True)
    sensor_id = models.ForeignKey(EonsSensor, on_delete=models.PROTECT, null=True)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    file_name = models.FileField(upload_to=content_file_name, max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    converted_to_raw_data = models.BooleanField(default=False)

    class Meta:
        verbose_name = "EONS CSV"
        verbose_name_plural = "EONS CSVs"

    def set_activated(self, value):
        try: 
            flag = bool(value)
        except Exception as e:
            print(f'Error: {e}')
        self.activated = flag

    def __str__(self):
        return f"{self.file_name.name.split('/')[-1]}"

class EonsBaseData(models.Model):
    station = models.ForeignKey(EonsStation, on_delete=models.PROTECT, null=True)
    sensor_id = models.ForeignKey(EonsSensor, on_delete=models.PROTECT, null=True)
    utc_datetime = models.DateTimeField(verbose_name='UTC datetime')
    local_datetime = models.DateTimeField(null=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    battery_voltage = models.DecimalField(max_digits=4, decimal_places=2)
    sky_brightness = models.DecimalField(max_digits=10, decimal_places=2)
    init_subs = models.FloatField()
    sky_counts = models.IntegerField(null=True)
    sky_brightness_discard = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sky_led_counts = models.IntegerField(null=True)
    moon_phase_deg = models.DecimalField(max_digits=6, decimal_places=1)
    moon_elev_deg = models.DecimalField(max_digits=6, decimal_places=3, default=0.00)
    moon_illum_percent = models.DecimalField(max_digits=4, decimal_places=1)
    sun_elev_deg = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        verbose_name = "EONS Raw Datum"
        verbose_name_plural = "EONS Raw Data"

        unique_together = [['sensor_id', 'utc_datetime']]

    def __str__(self):
        return f"{self.utc_datetime}"