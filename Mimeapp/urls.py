from Mimeapp import views
from django.urls import path
urlpatterns = [path('html',views.Html.as_view()),
               path('excel',views.excel.as_view()),
               path('xml',views.xml.as_view()),
               path('pdf',views.pdf.as_view()),
]
