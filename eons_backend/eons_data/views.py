from rest_framework import generics
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth import get_user_model

from guardian.shortcuts import get_user_perms

from .models import EonsSite, EonsCsv
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
class UploadCsvView(CreateView):
    template_name = 'eons_data/upload_csv.html'
    form_class = EonsCsvForm
    sites = EonsSite.objects.all()

    # def get(self, request, *args, **kwargs):
    #     user = request.user
    #     perms = []
    #     for site in self.sites:
    #         perms.append(get_user_perms(user, site))
    #     form = self.form_class()
    #     return render(request, self.template_name, {
    #         'form': form,
    #         'req': request,
    #         'perms': perms,
    #     })

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(data=request.POST, files=request.FILES)
    #     if form.is_valid():
    #         print("valid form!")
    #         user = request.user
    #         form.save(user=user)
    #         return HttpResponse('/')
    #     print("form invalid!")
    #     return render(request, self.template_name, {
    #         'form': form
    #     })

    def form_valid(self, form):
        csv = form.save(commit=False)
        csv.user = get_user_model().objects.get(email=self.request.user)
        csv.save()
        return HttpResponseRedirect(reverse('home'))