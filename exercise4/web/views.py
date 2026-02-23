from django.http import HttpResponse,request

def sad(request, name):
    return HttpResponse (f"Nobody likes you, {name}!")


def happy(request, name, times):
    respons = f"You are great, {name} :)<br>" * times
    return HttpResponse(respons) 
    
    