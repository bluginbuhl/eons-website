from django.urls import path

from .views import EonsSiteList, EonsSiteDetail, EonsCsvList, EonsCsvDetail, upload_csv


urlpatterns = [
    path('sites/<pk>/', EonsSiteDetail.as_view()),
    path('sites/', EonsSiteList.as_view()),
    path('sites/<pk>/csvs', EonsCsvList.as_view()),

    path('upload/', upload_csv, name='upload_csv'),
]
