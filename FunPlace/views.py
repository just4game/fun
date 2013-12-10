'''
Created on Dec 10, 2013

@author: stone
'''

from django.http import HttpResponse

def test(request):
    return  HttpResponse("Done")