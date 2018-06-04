from django.shortcuts import render,HttpResponse
from . import models
from django.forms.models import model_to_dict
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from . import search_func

from django.utils import timezone
from datetime import datetime,date
from decimal import Decimal
class DirectorEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, (timezone.datetime,datetime) ):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        elif isinstance(obj, Decimal):
            return str(obj)
        else:  
            return json.JSONEncoder.default(self, obj) 


@csrf_exempt
def model_query(request):
    """
    POST request.body= model,filters,order_by
    """
    dc = json.loads(request.body)
    fun_name = dc.pop('fun')
    fun = getattr(search_func,fun_name)
    out_list = fun(**dc)
    
    #model_name = dc.get('model')
    #filters = dc.get('filters')
    #order_by = dc.get('order_by','-pk')
    #start=dc.get('start',0)
    #end=dc.get('end',-1)
   
    #model = getattr(models,model_name)
    
    #query = model.objects.filter(**filters).order_by(order_by)[start:end]
    #ls = []
    #for item in query:
        #ls.append(model_to_dict(item))
        
    
    return HttpResponse(json.dumps(out_list,cls=DirectorEncoder),content_type="application/json")


