from django.shortcuts import HttpResponseRedirect, render_to_response, render
from django.core.context_processors import csrf

from models import *
from forms import *


#TODO: Create a view and render context
#TODO: Implement custom URL

#TODO: Create a model
#TODO: Show the model
#TODO: Render the model inn a view 

#TODO: Creating a form to show the model


def home(request, *args, **kwargs):
    #TODO: implement me!

    context = {
              }
    return render_to_response('index.html',
                  context,
                  );


def newperson(request):
    """whatever"""
    #TODO: Implement me!
    return HttpResponseRedirect('/')

