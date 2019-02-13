# djangotemplates/example/views.py
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.http import HttpResponseRedirect
# Add the two views we have been talking about  all this time :)
from rest_framework.views import APIView
from rest_framework.response import Response
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class AarifTest(APIView):
    def get(self,request):
        data = {'name':'Aarif faridi','add':'New delhi'}
        return  Response(data)