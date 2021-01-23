# base Python libraries
import csv
import io
from decimal import Decimal

# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Third-party
from rest_framework import generics
from guardian.shortcuts import get_objects_for_user
from guardian.decorators import permission_required
from pandas import to_datetime

# Local
from .models import EonsStation, EonsCsv, EonsBaseData
from .serializers import EonsStationSerializer, EonsCsvSerializer
from .forms import EonsCsvForm
from .utils import BulkCreateManager


# EONS Site API views
class EonsStationList(generics.ListCreateAPIView):
    queryset = EonsStation.objects.all()
    serializer_class = EonsStationSerializer

class EonsStationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EonsStation.objects.all()
    serializer_class = EonsStationSerializer

# EONS CSV API views
class EonsCsvList(generics.ListCreateAPIView):
    queryset = EonsCsv.objects.all()
    serializer_class = EonsCsvSerializer

class EonsCsvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EonsCsv.objects.all()
    serializer_class = EonsCsvSerializer

# Upload CSV view
# using function-based view for now
# TODO: get class-based view to work
# class UploadCsvView(CreateView):
#     template_name = 'eons_data/upload_csv.html'
#     form_class = EonsCsvForm
#     sites = EonsSite.objects.all()

#     # def get(self, request, *args, **kwargs):
#     #     user = request.user
#     #     perms = []
#     #     for site in self.sites:
#     #         perms.append(get_user_perms(user, site))
#     #     form = self.form_class()
#     #     return render(request, self.template_name, {
#     #         'form': form,
#     #         'req': request,
#     #         'perms': perms,
#     #     })

#     # def post(self, request, *args, **kwargs):
#     #     form = self.form_class(data=request.POST, files=request.FILES)
#     #     if form.is_valid():
#     #         print("valid form!")
#     #         user = request.user
#     #         form.save(user=user)
#     #         return HttpResponse('/')
#     #     print("form invalid!")
#     #     return render(request, self.template_name, {
#     #         'form': form
#     #     })

#     def form_valid(self, form):
#         csv = form.save(commit=False)
#         csv.user = get_user_model().objects.get(email=self.request.user)
#         csv.save()
#         return HttpResponseRedirect(reverse('home'))


@login_required
# @permission_required('eons_data.upload_data')
def upload_csv(request, methods=['GET', 'POST']):

    template = 'eons_data/upload_csv.html'
    data = EonsBaseData.objects.all()
    
    stations = list(get_objects_for_user(
        request.user, 'eons_data.upload_data'
    ))

    context = {
        'title': "Upload Data",
        'data': data,
        'stations': stations,
    }

    if request.method == 'GET':
        return render(request, template, context)

    csv_temp = request.FILES['file1']
    # data_set = csv_file.read().decode('utf-8')
    # io_string = io.StringIO(data_set)

    station_choice = request.POST['station_choice']

    eons_csv, _ = EonsCsv.objects.update_or_create(
        station_code = EonsStation.objects.filter(site_code=site_choice).first(),
        user=request.user,
        file_name = csv_temp,
    )

    # with open(eons_csv.file_name.path, 'r') as f:
    #     bulk_mgr = BulkCreateManager(chunk_size=500)
    #     next(f)
    #     for row in csv.reader(f, delimiter=';'):
    #         if len(row) > 12:
    #                 bulk_mgr.add(EonsBaseData(
    #                 station = EonsSite.objects.filter(site_code=site_choice).first(),
    #                 utc_datetime = to_datetime(row[0], utc=True),
    #                 local_datetime = to_datetime(row[1], utc=True),
    #                 temperature = Decimal(row[2]),
    #                 battery_voltage = Decimal(row[3]),
    #                 surf_brightness = Decimal(row[4]),
    #                 init_subs = float(row[5]),
    #                 sky_counts= int(row[6]),
    #                 sky_brightness_discard= Decimal(row[7]),
    #                 sky_led_counts= int(row[8]),
    #                 moon_phase_deg = Decimal(row[9]),
    #                 moon_elev_deg = Decimal(row[10]),
    #                 moon_illum_percent = Decimal(row[11]),
    #                 sun_elev_deg = Decimal(row[12]),
    #             ))
    #         else:
    #             bulk_mgr.add(EonsBaseData(
    #                 station = EonsSite.objects.filter(site_code=site_choice).first(),
    #                 utc_datetime = to_datetime(row[0], utc=True),
    #                 local_datetime = to_datetime(row[1], utc=True),
    #                 temperature = Decimal(row[2]),
    #                 battery_voltage = Decimal(row[3]),
    #                 surf_brightness = Decimal(row[4]),
    #                 init_subs = float(row[5]),
    #                 moon_phase_deg = Decimal(row[6]),
    #                 moon_elev_deg = Decimal(row[7]),
    #                 moon_illum_percent = Decimal(row[8]),
    #                 sun_elev_deg = Decimal(row[9]),

    #                 sky_counts= None,
    #                 sky_brightness_discard= None,
    #                 sky_led_counts= None
    #             ))
    #     bulk_mgr.done()

    eons_csv.set_activated(True)

    context = {
        'title': "Upload Data",
        'data': data,
        'sites': sites,
        'messages': None
    }

    return render(request, 'eons_data/upload_success.html', context)