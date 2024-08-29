from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class main1(TemplateView):
    template_name = 'index1.html'

# class shop(TemplateView):
#     template_name = 'index2.html'

class bascet(TemplateView):
    template_name = 'index3.html'

def menu(request):
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    # mydict=["Atomic Heart", "Cyberpunk 2077"]
    context={
         'mydict':mydict,
    }
    return render(request, 'index2.html', context)

# {% list = mydict|setdefault('games') %}

# образец
# def index(request):
#      text= 1
#      name='vasy'
#      list=[1.0, 2.22, 3.3]
#      dict={'games': ['Atomic Heart", "Cyberpunk 2077"]}
#      context={
#          'text':text,
#          'name':name,
#          'list':list,
#      }
#      return render(request, 'index.html', context)