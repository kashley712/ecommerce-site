from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#def members(request):
    #return HttpResponse("Hello world!")
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
    #template = loader.get_template('shopitem.html')
    #return HttpResponse(template.render())

    #
    #def indexpage(request):
  #context = {'selected_page': 'index'}
 # return render(request, 'index.html', context)

 # def shopitempage(request):
 # context = {'selected_page': 'shopitem'}
 # return render(request, 'shopitem.html', context)

from django.shortcuts import render

def members(request):
    # You can remove this line as it is not needed
    # return HttpResponse("Hello world!")

    # Load and render the 'index.html' template
    return render(request, 'index.html')
    return render(request, 'shopitem.html')


def indexpage(request):
    context = {'selected_page': 'index'}
    return render(request, 'index.html', context)

def shopitempage(request):
    context = {'selected_page': 'shopitem'}
    return render(request, 'shopitem.html', context)
#
