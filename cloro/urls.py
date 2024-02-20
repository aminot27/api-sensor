from django.urls import path
from cloro.views import CloroApiView, CloroApiViewDetail

urlpatterns_cloro = [
    path('sensor', CloroApiView.as_view()),
    path('sensor/<int:id', CloroApiViewDetail.as_view()),
    ]