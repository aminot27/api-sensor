from django.urls import path
from cloro.views import CloroApiView, CloroApiViewDetail
from .DownloadExcelView import DownloadExcelView 

urlpatterns_cloro = [
    path('sensor', CloroApiView.as_view()),
    path('sensor/<int:id>', CloroApiViewDetail.as_view()),
    path('descargar/', DownloadExcelView.as_view(), name='descargar-excel'),
    ]