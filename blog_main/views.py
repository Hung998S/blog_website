from django.http import HttpResponse

def home(request):
    return HttpResponse("Education For Nation")