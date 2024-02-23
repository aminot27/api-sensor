from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CloroModel
from openpyxl import Workbook
from django.http import HttpResponse
from django.utils.timezone import make_naive
from django.utils.timezone import get_default_timezone

class DownloadExcelView(APIView):
    def get(self, request, *args, **kwargs):
        cloro_data = CloroModel.objects.all()

        # Crear un libro de trabajo y una hoja de Excel
        wb = Workbook()
        ws = wb.active

        # Agregar títulos de columnas en la primera fila
        columns = ['ID', 'Fecha Creación', 'UNSAAC_TESIS_ELECTRONICA', 'Data Cloro', 'Data Turbidez']
        ws.append(columns)

        # Agregar datos
        for data in cloro_data:
            created_at_naive = make_naive(data.created_at, get_default_timezone())
            ws.append([
                data.id,
                created_at_naive,
                data.UNSAAC_TESIS_ELECTRONICA,
                data.data_cloro,
                data.data_turbidez,
            ])

        # Guardar el libro de trabajo en un objeto BytesIO
        from io import BytesIO
        excel_file = BytesIO()
        wb.save(excel_file)
        excel_file.seek(0)

        # Crear una respuesta HTTP con el archivo Excel
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="datos_cloro.xlsx"'
        return response