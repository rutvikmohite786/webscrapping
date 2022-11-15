from django.shortcuts import render
from django.http import HttpResponse
import json
from pytesseract import pytesseract
from PIL import Image
import requests
from bs4 import BeautifulSoup
from django.template import loader

def html(request):
    return render(request, "home.html")

def image(request):
    return render(request, "image.html")

def search(request):
    my_list = []
    query = request.POST['input']
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    for j in search(query, tld="co.in", num=5, stop=5, pause=2):
        my_list.append(j)
    return HttpResponse(json.dumps(my_list), content_type="application/json")

def searchdata(request):
    # Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Define path to image
    path_to_image = 'images/sampletext3-ocr-539x450.png'

    # Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract
    # Open image with PIL
    img = Image.open(path_to_image)

    print('img',img)
    # Extract text from image
    text = pytesseract.image_to_string(img)
    print('newone',text)

def webscrape(request):
    url = request.POST['input']
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', id='mainbar')

    #soup.body
    return HttpResponse(json.dumps(s.prettify()), content_type="application/json",status=200)









