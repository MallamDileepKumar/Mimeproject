from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
data = """<table bgcolor = 'orange' border='2' bordercolor = 'blue'><tr><th>S.No</th><th>Name</th><th>Place</th><th>PH.NO</th><th>Qualify</th></tr>
            <tr><td>1</td><td>Roshan</td><td>Guntakal</td><td>6302636380</td><td>Degree</td></tr>
            <tr><td>2</td><td>Hemanth</td><td>Vizag</td><td>9895156529</td><td>Degree</td></tr>
            <tr><td>3</td><td>Santhosh</td><td>Warangal</td><td>9951505304</td><td>BTech</td></tr>
            <tr><td>4</td><td>Dileep</td><td>Tirupati</td><td>9966982387</td><td>MTech</td></tr>
            </table>"""
class Html(View):
    def get(self,request):
        return HttpResponse(data,content_type='text/html')
class excel(View):
    def get(self,request):
        return HttpResponse(data,content_type='application/vnd.ms-excel')
class xml(View):
    def get(self,request):
        return HttpResponse(data,content_type='application/xml')

class pdf(View):
    def get(self, request):
        return HttpResponse(data, content_type='application/pdf')


