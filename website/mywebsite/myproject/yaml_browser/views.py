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
 <p>Paste your yaml file here</p>
 
 <form action="/your-name/" method="post" name="yaml_file_text_box" input type="text">
  
  <textarea name="yaml_file_text_box" rows="30" cols="50"> 
  </textarea>
  <input type="submit" value="Submit">
</form>
 
 </body>
 </html>'''

str2 = ""

html_webpage_2 = '''
<!DOCTYPE html>
 <html>
 <body>

 <a href={value2}>{fname}</a> 
 <h2>prcessing data from a yaml-browser</h2>
 
 <p>str2</p>
</form>
 </body>
 </html>'''
@csrf_exempt #this is a poor workaround - without fixing the issue
def home(request):
	if request.method == "POST":
		screenname = request.POST.get("yaml_file_text_box", None)
		doc2 = yaml.load(screenname)
		'''for key, value in doc2.items():
			print "{}:::::{}".format(key, value)'''
		print doc2['uif 0']
		print doc2['adv_uifetscfg 0']
		#return HttpResponse(doc2.values(), content_type="text/plain")
		global str2
		str2 = doc2['adv_uifetscfg 0']


		return HttpResponse(html_webpage_2.format(fname=doc2.keys(), value2=doc2['adv_uifetscfg 0'])) 

	return HttpResponse(html_webpage)
	#return HttpResponse('Hello, World!')