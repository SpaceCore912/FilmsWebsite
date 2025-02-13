from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.template import loader
from .models import Film,Profile,Watchlist,Like
from .forms import NameForm,ContactForm,RegisterForm
from django.core.mail import send_mail
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser 
from django.db.models import F

import asyncio
from time import sleep
import polls.manager as manager

import httpx
import json 
#manager.filmloader1()

# Create your views here.
def chatPage(request,*args,**kwargs):
	if  not request.user.is_authenticated:
		return redirect("login")
	context={}
	return render(request,"polls/chatPage.html",context)

def my_view(request):
	username=request.POST["username"]
	password=request.POST["password"]
	user=authenticate(request, username =username, password=password)
	if user is not None:
		login(request, user)
	else:
		print("error")


def contact(request):
	form=ContactForm(request.POST)
	title=form.cleaned_data["subject"]
	message=form.cleaned_data["message"]
	sender=form.cleaned_data["sender"]
	cc_myself=form.cleaned_data["cc_myself"]

	recipients =["spacecore912@gmail.com"]
	if cc_myself:
		recipients.append(sender)
	
	#send_mail(title, message, sender, recipients)
	def save(self, commit):

		return HttpResponseRedirect("/thanks/")	

from django.core import serializers
from django.forms.models import model_to_dict

class IndexView(generic.ListView):
	template_name="polls/index.html"
	context_object_name="latest_films"
	model=Film
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			profile=Profile.objects.get(pk=self.request.user.id)
			context["profile_url"]=f"polls/images/{profile.user.username}.jpg"
		except: 
			user=AnonymousUser()
			context["profile_url"]=user
		
		#data = serializers.serialize('json', self.get_queryset())
		#print(data)
		
		
		#context["genre-list"][]]({movie["name_text"]:})
		print(context)
		return context
	
class popularView(generic.ListView):
	template_name="polls/index.html"
	context_object_name="latest_films"
	queryset=Film.objects.filter(category__name="popular")
	print(Film.objects.filter(category__name="popular"))
class classicView(generic.ListView):
	template_name="polls/index.html"
	context_object_name="latest_films"
	queryset=Film.objects.filter(category__name="classic")

class trendView(generic.ListView):
	template_name="polls/index.html"
	context_object_name="latest_films"
	queryset=Film.objects.filter(category__name="trend")

class unseenView(generic.ListView):
	template_name="polls/index.html"
	context_object_name="latest_films"
	queryset=Film.objects.filter(category__name="unseen")

def aboutView(request):
	return render(request,"polls/about.html")
	


def descriptionView(request, film_id):
	
	try:
		film=Film.objects.get(id=film_id)
		user=request.user.id
		liked=False
		addedToW=False
		#profile=Profile.objects.get(user=user)
		l2=Like.objects.get(user=request.user)
		w2=Watchlist.objects.get(user=request.user)
		

		
		
		
	except:
		liked=False
		addedtoW=False
		return render(request,"polls/description.html",context={"film":film,"liked":liked,"addedToW":addedToW})
		
	else:
		f2=Film.objects.get(pk=film_id)
		for film in w2.films.all():
			if film ==f2:
				addedToW=True
		if film in l2.linked_film.all():
				for film in l2.linked_film.all():
					if film.id==f2.id:
						liked=True
	print (addedToW)
	return render(request,"polls/description.html",context={"film":film,"liked":liked,"addedToW":addedToW})

def ProfileView(request,user_username):
	user=request.user.id
	profile=get_object_or_404(Profile, pk=user)
	watchlist=Watchlist.objects.filter(user=user)
	liked=Like.objects.get(user=user)
	liked=liked.linked_film.all()
	return render(request, "polls/profile.html",context={"profile":profile,"watchlists":watchlist,"liked":liked})	



@csrf_exempt
def like_film(request, film_id):
	if request.method == 'POST':
		film = get_object_or_404(Film, pk=film_id)
		liked = True
		l2=Like.objects.get(user=request.user)
		f2=Film.objects.get(pk=film_id)
		
		
		# Example logic to like/unlike the film
		contains= l2.linked_film.all()
		if contains:
			if film in l2.linked_film.all():
				for film in l2.linked_film.all():
					if film.id==f2.id:

						l2.linked_film.clear()
						liked=False
						print("cleared")
						
					else:
						l2.linked_film.add(f2)
						print("added")
						liked=True
		else:
			l2.linked_film.add(f2)
			print("there were no likes")
			liked=True
		 

		
		return JsonResponse({'liked': liked})
	
	return JsonResponse({'error': 'Invalid request'}, status=400)


def search(request):
	if request.method=="POST":
		form =form.SearchForm()
		
		if form.is_valid():
			search=form.cleaned["search"]
			Film.objects.filter(name_text__icontains("search"))




@csrf_exempt
def watchlist_film(request, film_id):
	if request.method == 'POST':
		film = get_object_or_404(Film, pk=film_id)
		added = True
		w2=Watchlist.objects.get(user=request.user)
		f2=Film.objects.get(pk=film_id)
		
		
		# Example logic to like/unlike the film
		contains= w2.films.all()
		if contains:
			for film in contains:
				if film.id==f2.id:

					w2.films.clear()
					added=False
					print("cleared")
					
				else:
					w2.films.add(f2)
					print("added")
					added=True
		else:
			w2.films.add(f2)
			print("there were no likes")
			added=True
		 

		
		return JsonResponse({'added': added})
	
	return JsonResponse({'error': 'Invalid request'}, status=400)



class WatchlistView(generic.TemplateView):
	template_name="polls/watchlist.html"
	context_object_name="films"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
	
		w1=Watchlist.objects.get(pk=kwargs["watchlist_id"])
		context["films"]=w1.films.all()
		print(context)
		return context



def get_name(request):
	if request.method =="POST":
		form =NameForm(request.POST)
		if form.is_valid():
			name=NameForm.cleaned_data["your_name"]
			print(form)
			send_mail("email",name, "tykhonbyshkin07@gmail.com")
			return HttpResponseRedirect("/thanks/")
	else:
		form=NameForm()	
		print("not valid form")	
	return render(request, "polls/name.html", {"form":form})

"""class SignUpView(CreateView):
	form_class=UserCreationForm
	success_url=reverse_lazy("login")
	template_name="registration/signup.html"
	"""

class SignUpView(CreateView):
	form_class=RegisterForm
	success_url=reverse_lazy("login")
	template_name="registration/signup.html"

async def index(request):
	return HttpResponse("Hello, async Django!")


#async functions	
async def http_call_async():
	for num in range(1,6):
		await asyncio.sleep(1)
		print(num)
	async with httpx.AsyncClient as client:
		r=await client.get("https://httpbin.org/")

def http_call_sync():
	for num in range(1,6):
		sleep(1)
		print(num)
		r =httpx.get("https://httpbin.org/")
		print(r)

async def async_view(request):
	loop=asyncio.get_event_loop()
	loop.create_task(http_call_async())
	return HttpResponse("Non-blocking HTTP request")

def sync_view(request):
	http_call_sync()
	return HttpResponse("Blocking HTTP request")
	#template= loader.get_template("polls/index.html")
	#context ={"director_films":Film.objects.all()}
	#return HttpResponse(template.render(context, request)


