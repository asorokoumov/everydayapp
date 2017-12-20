from django.shortcuts import render
from django.http import JsonResponse
from backend.models import Page
import json
from django.core import serializers
from django.http import HttpResponse
from itertools import chain
from random import randint


# Create your views here.
def pages(request):
    types = request.GET.get('types', '').split(',')

    # create empty queryset
    query_sets = Page.objects.filter(type='')

    # get result for each type and combine them
    for type in types:
        object = Page.objects.filter(type=type).order_by('?')[:1]
        query_sets = list(chain(query_sets, object))

    # a little bit of json magic
    raw_data = serializers.serialize('json', query_sets)
    data = json.loads(raw_data)
    actual_data = json.dumps([d['fields'] for d in data])

    return HttpResponse(actual_data, content_type='application/json')
