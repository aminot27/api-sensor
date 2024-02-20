from django.urls import path
from cloro.views import CloroApiView, CloroApiViewDetail

urlpatterns_cloro = [
    path('cloro', CloroApiView.as_view()),
    path('cloro/<int:id', CloroApiViewDetail.as_view()),
    ]