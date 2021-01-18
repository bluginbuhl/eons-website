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
from .models import EonsSite, EonsCsv, EonsBaseData
from .serializers import EonsSiteSerializer, EonsCsvSerializer
from .forms import EonsCsvForm


# EONS Site API views
class EonsSiteList(generics.ListCreateAPIView):
    queryset = EonsSite.objects.all()
    serializer_class = EonsSiteSerializer

class EonsSiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EonsSite.objects.all()
    serializer_class = EonsSiteSerializer

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
    
    sites = list(get_objects_for_user(
        request.user, 'eons_data.upload_data'
    ))

    context = {
        'title': "Upload Data",
        'data': data,
        'sites': sites,
    }

    if request.method == 'GET':
        return render(request, template, context)

    csv_file = request.FILES['file1']
    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)

    site_choice = request.POST['site_choice']

    next(io_string)

    for column in csv.reader(io_string, delimiter=';'):
        _, created = EonsBaseData.objects.update_or_create(
            site = EonsSite.objects.filter(site_code=site_choice).first(),
            utc_datetime = to_datetime(column[0] + 'T' + column[1], utc=True),
            local_datetime = to_datetime(column[2] + 'T' + column[3], utc=True),
            temperature = Decimal(column[4]),
            battery_voltage = Decimal(column[5]),
            surf_brightness = Decimal(column[6]),
            init_subs = float(column[7]),
            moon_phase_deg = Decimal(column[8]),
            moon_elev_deg = Decimal(column[9]),
            moon_illum_percent = Decimal(column[10]),

            sky_counts= None,
            sky_brightness_discard= None,
            sky_led_counts= None
        )

    context = {
        'title': "Upload Data",
        'data': data,
        'sites': sites,
        'messages': "Success!"
    }

    return render(request, 'home', context)