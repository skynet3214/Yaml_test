# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #this is a poor workaround - without fixing the issue
import yaml
# Create your views here.
#gettig the csrf error after changing the method to post 
html_webpage = '''
<!DOCTYPE html>
 <html>
 <body>
 <h2>Building a yaml-browser</h2>
 <p>Beginners html page</p>
 <form action="/your-name/" method="post">
  
  Paste your yaml file here:<br>
  <input type="text" name="yaml_file_text_box">
  <br>
  <input type="submit" value="Submit">
</form>
 </body>
 </html>'''

html_webpage_2 = '''
<!DOCTYPE html>
 <html>
 <body>
 <h2>prcessing data from a yaml-browser</h2>
 <p>{fname}</p>
</form>
 </body>
 </html>'''
@csrf_exempt #this is a poor workaround - without fixing the issue
def home(request):
	if request.method == "POST":
		screenname = request.POST.get("yaml_file_text_box", None)
		doc2 = yaml.load(screenname)
		for key, value in doc2.items():
			print key,
			print value

		return HttpResponse(html_webpage_2.format(fname=doc2)) 

	return HttpResponse(html_webpage)
	#return HttpResponse('Hello, World!')