from django.urls import path
from .views import EonsSiteList, EonsSiteDetail


urlpatterns = [
    path('sites/<pk>/', EonsSiteDetail.as_view()),
    path('sites/', EonsSiteList.as_view()),
]
