import string
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import Url
from .models import UrlData
import random

# Create your views here.

def index(request):
	return HttpResponse("Hello World")

def urlShort(request):
	slug=""
	context={}
	UrlData.objects.all().delete()
	if request.method == 'POST':
		form = Url(request.POST)
		if form.is_valid():
			for i in range(10):
				slug+=random.choice(string.ascii_letters)
			long_url=request.POST.get("url","")
			new_url=UrlData(url=long_url,slug=slug)
			new_url.save()
			print("saved ",new_url.slug)
			context['form']=form
			context['short']=slug
	return render(request,'url/index.html',context)

def urlRedirect(request, slugs):
	data=UrlData.objects.get(slug=slugs)
	return redirect(data.url)