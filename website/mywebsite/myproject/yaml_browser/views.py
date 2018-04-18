# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #this is a poor workaround - without fixing the issue
from django.template import Template, Context
from django.template.loader import get_template
import yaml

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

placeholder = '''
<!DOCTYPE html>
 <html>
 <body>
 <p>Placeholder html page</p>
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
def yaml_key_value_view(request, something):
	print something
	return HttpResponse(something+':'+'\n'+'\n'+yaml_key_value_dict[something], content_type="text/plain")













