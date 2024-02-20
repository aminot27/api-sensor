from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cloro.models import CloroModel
from cloro.serializers import CloroSerializer

class CloroApiView(APIView):
    def get(self, request):
        serializers = CloroSerializer(CloroModel.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializers.data)
    def post(self, request):
        serializer = CloroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class CloroApiViewDetail(APIView):
    def get_object(self, id):
        try:
            return CloroModel.objects.get(pk=id)
        except CloroModel.DoesNotExist:
            return None
    def get(self, request, id):
        cloro = self.get_object(id)
        serializer = CloroSerializer(cloro)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def put(self, request, id):
        cloro=self.get_object(id)
        if(cloro==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = CloroSerializer(cloro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        cloro = self.get_object(id)
        cloro.delete()
        response = {'deleted':True}
        return Response(status=status.HTTP_200_OK, data=response)



# Create your views here.
