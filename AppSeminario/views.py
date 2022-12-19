from django.shortcuts import render, redirect
from AppSeminario.models import Inscritos, Institucion
from AppSeminario.forms import FormSeminario
from django.http import JsonResponse
from .serializers import InscritosSerializer, InstitucionSerializer
from .models import Inscritos, Institucion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadodeinscritos(request):
    ins = Inscritos.objects.all()
    data = {'Inscritos': ins}
    return render(request, 'listarinscripcion.html', data)

def ingresodeinscritos(request):
    form = FormSeminario()
    if request.method == 'POST':
        form = FormSeminario(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarinscripcion.html', data)

def modificacióndeinscritos(request, id):
    ins = Inscritos.objects.get(id = id)
    form = FormSeminario(instance=ins)
    if request.method == 'POST':
        form = FormSeminario(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarinscripcion.html', data)

def eliminacióndeinscritos(request, id):
    ins = Inscritos.objects.get(id = id)
    ins.delete()
    return redirect('/Seminario/')

#API REST

def verinscriptosDb(request):
    inscriptos= Inscritos.objects.all()
    data = {'inscriptos' : list(inscriptos.values('id', 'nombre','telefono','fechainscripción','institucion','horainscripción','estado','observacion'))}

    return JsonResponse(data)

# Class Based Views

class ListarSeminario(APIView):

    def get(self, request):
        ins = Inscritos.objects.all()
        serial = InscritosSerializer(ins, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleSeminario(APIView):

    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        ins = self.get_object(pk)
        serial = InscritosSerializer(ins)
        return Response(serial.data)

    def put(self, request, pk):
        ins = self.get_object(pk)
        serial = InscritosSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        ins = self.get_object(pk)
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#  Función Based Views

@api_view(['GET', 'POST'])
def seminario_list(request):
    if request.method == 'GET':
        ins = Institucion.objects.all()
        serial = InstitucionSerializer(ins, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def seminario_detalle(request, pk):
    try:
        ins = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(ins)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)