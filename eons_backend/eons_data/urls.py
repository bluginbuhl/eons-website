from django.urls import path

from .views import EonsStationList, EonsStationDetail, EonsCsvList, EonsCsvDetail, upload_csv


urlpatterns = [
    path('stations/<pk>/', EonsStationDetail.as_view()),
    path('stations/', EonsStationList.as_view()),
    path('stations/<pk>/csvs', EonsCsvList.as_view()),

    path('upload/', upload_csv, name='upload_csv'),
]
