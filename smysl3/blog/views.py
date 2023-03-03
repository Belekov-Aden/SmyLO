from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse('''<html>
    <title>Site Belekov Aden</title>
    <h1>Belekov Aden</h1>
    </html>''')