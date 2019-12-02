from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import apikey
from . models import application
from . serializers import applicationSerializer
from . serializers import apikeySerializer



class appList(APIView):
    def post(self,request):
        if 'key' in request.data[0]:
            if apikey.objects.filter(key=request.data[0]['key']).exists():
                apps = application.objects.all()
                datas = applicationSerializer(apps,many=True)
                return Response(datas.data)
            else:
                return Response("Error: Please write valid key!")
        else:
            return Response("Error: Please write valid key!")


class appCreate(APIView):
    def post(self,request):
        if 'key' in request.data[0]:
            if apikey.objects.filter(key=request.data[0]['key']).exists():
                if 'title' in request.data[0]:
                    form = application(title=request.data[0]['title'])
                    form.save()
                    return Response("Success: Application added successfully!")
                else:
                    return Response("Error: Application title can not be empty!")

            else:
                return Response("Error: Please write valid key!")
        else:
            return Response("Error: Please write valid key!")

class appUpdate(APIView):
    def post(self,request):
        if 'key' in request.data[0]:
            if apikey.objects.filter(key=request.data[0]['key']).exists():
                    if 'id' in request.data[0]:
                        if application.objects.filter(id=request.data[0]['id']).exists():
                            if 'title' in request.data[0]:
                                form = application.objects.get(pk=request.data[0]['id'])
                                form.title=request.data[0]['title']
                                form.save()
                                return Response("Success: Application updated successfully!")
                            else:
                                return Response("Error: Application title can not be empty!")
                        else:
                            return Response("Error: Application id not correct!")
                    else:
                        return Response("Error: Application id not correct!")
            else:
                return Response("Error: Please write valid key!")
        else:
            return Response("Error: Please write valid key!")

class appDelete(APIView):
    def post(self,request):
        if 'key' in request.data[0]:
            if apikey.objects.filter(key=request.data[0]['key']).exists():
                    if 'id' in request.data[0]:
                        if application.objects.filter(id=request.data[0]['id']).exists():
                            form = application.objects.get(pk=request.data[0]['id'])
                            form.delete()
                            return Response("Success: Application deleted successfully!")
                        else:
                            return Response("Error: Application id not correct!")
                    else:
                        return Response("Error: Application id not correct!")
            else:
                return Response("Error: Please write valid key!")
        else:
            return Response("Error: Please write valid key!")


class keyUpdate(APIView):
    def post(self,request):
        if 'key' in request.data[0]:
            if apikey.objects.filter(key=request.data[0]['key']).exists():
                if 'new_key' in request.data[0]:
                    form = apikey.objects.get(key=request.data[0]['key'])
                    form.key = request.data[0]['new_key']
                    form.save()
                    return Response("Success: New key updated successfully!")
                else:
                    return Response("Error: New key not correct!")
            else:
                return Response("Error: Please write valid old key!")
        else:
            return Response("Error: Please write valid old key!")
