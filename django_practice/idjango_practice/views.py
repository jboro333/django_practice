from django.shortcuts import render

def mainpage(request): # objecte de tipus http request k em proporciona django
    page = """
    <html>
    <body>
    sobres, a PP application
    </body>
    </html>
    """
    return HttpResponse() # construeix resposta hhttp a apartir duna cadena
                        # de text k ha de contenir el html
# Create your views here.
