from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Resevation,Geust,Movie
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer
from  rest_framework import status
from rest_framework import mixins,generics,viewsets
# Create your views here.

# queryset not used rest_framework
def no_rest_from_model(request):
    data=Geust.objects.all()
    response={
        'guest':list(data.values('name','phone'))
    }
    
    return JsonResponse(response)
# function based view 
@api_view(['GET','POST'])
def FBV_list(request):
    if request.method=='GET':
        geusts=Geust.objects.all()
        serializer=GuestSerializer(geusts,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.data,status=400)
    

@api_view(['GET','PUT','DELETE'])
def FBV_pk(request,pk):
    try:
      geusts=Geust.objects.get(pk=pk)
    except geusts.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        
        serializer=GuestSerializer(geusts)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=GuestSerializer(geusts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)    
    
    elif request.method=='DELETE':
        geusts.delete()
        return Response(status=204)
             
        
# class based view

class Cbv_list(APIView):
    def get(self,request):
        geusts=Geust.objects.all()
        serializer=GuestSerializer(geusts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
class Cbv_pk(APIView):
    def get_object(self,pk):
        try:
            return Geust.objects.get(pk=pk)
        except Geust.DoesNotExist:
            raise  Http404
        #   return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk):
       guest=self.get_object(pk)
       serializer=GuestSerializer(guest)
       return Response(serializer.data)
    def put(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
    def delete(self,request,pk):
        guest=self.get_object(pk)
        guest.delete()
        return Response(status=204)
    
       
       
#mixins get,post
class Mixin_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

# mixin_pk get,put,delete 
class mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)
    
#Grnerics
class Generic_list(generics.ListCreateAPIView):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer
    
class Generic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer
    
#viewset
class GuestViewSet(viewsets.ModelViewSet):
    queryset=Geust.objects.all()
    serializer_class=GuestSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    
class ServationViewSet(viewsets.ModelViewSet):
    queryset=Resevation.objects.all()
    serializer_class=ReservationSerializer