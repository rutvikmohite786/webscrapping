from django.shortcuts import render
from django.http import HttpResponse
import json


def html(request):
    return render(request, "home.html")

def search(request):
    my_list = []

    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    # to search
    query = "Geeksforgeeks"

    for j in search(query, tld="co.in", num=5, stop=5, pause=2):
        my_list.append(j)
       # print(j)
    #print(my_list)
    return HttpResponse(json.dumps(my_list), content_type="application/json")



