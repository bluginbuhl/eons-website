from django.urls import path

from .views import EonsSiteList, EonsSiteDetail, EonsCsvList, EonsCsvDetail, UploadCsvView


urlpatterns = [
    path('sites/<pk>/', EonsSiteDetail.as_view()),
    path('sites/', EonsSiteList.as_view()),
    path('sites/<pk>/csvs', EonsCsvList.as_view()),

    path('upload/', UploadCsvView.as_view(), name='upload_csv'),
]
