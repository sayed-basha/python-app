from django.shortcuts import render
from.models import Dest

# Create your views here.

def index(request):
     dests=Dest.objects.all()
     return render(request,'index.html',{'dests':dests})
