from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# @permission_required('view_user')
def temp_view(request):
    if request.user.has_perms(['view_student']):
        return HttpResponse("Hello world!")
    else:
        return HttpResponse("Hello world!")
