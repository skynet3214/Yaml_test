# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #this is a poor workaround - without fixing the issue
from django.template import Template, Context
from django.template.loader import get_template
import yaml
import json

# Create your views here.
#getting the csrf error after changing the method to post 
homepage = '''
<!DOCTYPE html>
 <html>
 <body>
 <h2>Building a yaml-browser</h2>
 <p>Paste your yaml file here</p>
 
 <form action="/yaml-keys/" method="post" name="yaml_file_text_box" input type="text">
  
  <textarea name="yaml_file_text_box" rows="30" cols="50"> 
  </textarea>
  <input type="submit" value="Submit">
</form>
 
 </body>
 </html>'''




yaml_key_value_dict = {}

@csrf_exempt #this is a poor workaround - without fixing the issue
def home(request):
	return HttpResponse(homepage)

@csrf_exempt
def yaml_key_view(request):
	yaml_input_string = request.POST.get("yaml_file_text_box", None)
	global yaml_key_value_dict
	yaml_key_value_dict = yaml.load(yaml_input_string)
	return render(request, 'index.html', {'yaml_key_value_dict':yaml_key_value_dict, 'sorted_yaml_keys':sorted(yaml_key_value_dict.keys())})

@csrf_exempt
def yaml_key_value_view(request, key):

	#print "Request :: {} Key:: {}".format(request, yaml_key_value_dict[key])
	
	
	
	if type(yaml_key_value_dict[key]) is str:
		yaml_key_value_dict[key] = yaml_key_value_dict[key].replace(" ", "&nbsp;")
		print yaml_key_value_dict[key] 
	
	
	return render(request, 'placeholder.html', {'key_name':key,'to_print':yaml_key_value_dict[key]})
	#return HttpResponse(key+':'+'\n'+'\n'+str(yaml_key_value_dict[key]), content_type="text/plain")

	
	
		#print str(yaml_key_value_dict[key])
	#return HttpResponse(key+':'+'\n'+'\n'+str(yaml_key_value_dict[key]), content_type="text/plain")
	#return render(request, 'placeholder.html', {'to_print':yaml_key_value_dict[key]})
	#return render(request, 'extend.html', {'yaml_key_value_dict':yaml_key_value_dict, 'sorted_yaml_keys':sorted(yaml_key_value_dict.keys())})



#Converting to string doe not work in all places. 










