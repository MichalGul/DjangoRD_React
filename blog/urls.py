from django.urls import path
from django.views.generic import TemplateView

app_name = "blog"

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")), #Home page for the app, nie ma potrzeba robic dodatkow view tylko do wyswietlenia templateu, trzeba podać siężkę w settings
]