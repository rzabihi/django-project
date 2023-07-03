from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.

# def members(request):
#     return HttpResponse('Hello Django')

def members(request):
    mymembers = Member.objects.all().values()

    template = loader.get_template('all_members.html')

    context = {
        'mymembers':mymembers,
    }

    return HttpResponse(template.render(context, request))

def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')

    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    # mydata = Member.objects.filter(firstName = 'mahdi', lastName = 'rezaei').values() | Member.objects.filter(firstName='shahram').values()
    # mydata = Member.objects.filter(Q(firstName='mahdi') | Q(firstName='shahram')).values()
    # mydata = Member.objects.filter(firstName__startswith='m').values()
    # mydata = Member.objects.filter(firstName__endswith='m').values()
    # mydata = Member.objects.filter(firstName__icontains='mo').values()
    # mydata = Member.objects.filter(firstName__exact='Ali').values()
    # mydata = Member.objects.filter(joined_date__gte='2020-01-01').values()
    mydata = Member.objects.filter(joined_date__lte='2020-01-01').values()
    # mydata = Member.objects.values_list('firstName')
    template = loader.get_template('template.html')

    context = {
        'mymembers' : mydata,
    }

    return HttpResponse(template.render(context, request))