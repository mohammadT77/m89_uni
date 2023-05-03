from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def cookie_sample_view(request):
    if request.COOKIES.get('turn', None):
        response = HttpResponse("It's your turn!")
    else:
        response = HttpResponse("Come back again!")
        response.set_cookie("turn", "YOU HAVE TURN HERE!")

    return response


def session_sample_view(request):
    if request.session.get('turn', None):
        response = HttpResponse("It's your turn!")
    else:
        response = HttpResponse("Come back again!")
        request.session['turn'] = "YOU HAVE TURN HERE!"

    return response
