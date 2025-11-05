from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.ordenes.models import OrdenDetalle
from .serializers import OrdenDetalleSerializer

class OrdenDetalleListAPIView(APIView):
    def get(self, request, format=None):
        orden_detalles = OrdenDetalle.objects.filter(orden__estatus='pendiente')
        serializer = OrdenDetalleSerializer(orden_detalles, many=True)
        return Response(serializer.data)
