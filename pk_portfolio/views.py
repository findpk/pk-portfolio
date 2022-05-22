from django.http import HttpResponse
from django.shortcuts import render
import pymongo
my_client = pymongo.MongoClient('localhost', 27017)


def home(request):
    dbname = my_client['Portfolio']
    collection_name = dbname["user-context"]
    context = collection_name.find({'name': 'Praveenkumar B'})
    for row in context:
        data = row
    return render(request, 'index.html', data)


def addUser(request):
    dbname = my_client['Portfolio']
    collection_name = dbname["user-context"]
    context = collection_name.insert_one(request)
    for row in context:
        data = row
    return data
