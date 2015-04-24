from django.shortcuts import HttpResponseRedirect, render_to_response, render
from django.core.context_processors import csrf

from models import Person
from forms import PersonForm

class Something(object):
    def __init__(self):
        self.number = [1,2,3,4,5]

def home(request, *args, **kwargs):
    usenum = 42
    if 'article_id' in kwargs:
        usenum=kwargs['article_id']

    people = [x.name for x in Person.objects.all()]

    new_person_form = PersonForm();

    context = {'whoever': usenum,
            'people' : people,
            'complexObjects' : Something(),
            'new_person_form' : new_person_form,
            }
    context.update(csrf(request))

    return render_to_response('index.html',
                  context,
                  );


def newperson(request):
    """whatever"""
    print request.POST
    form = PersonForm(request.POST or None)
    if form.is_valid():
        print form.save()

    return HttpResponseRedirect('/')

