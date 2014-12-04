from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import UpdateView


from django.contrib.auth.models import User
from wishlist.models import Gift, UserInfo

from wishlist.forms import GiftForm, UserInfoForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse


from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
	user_list = User.objects.all()
	
	context_dict = {'user_list':user_list,'user':request.user}

	return render(request, 'wishlist/index.html', context_dict)


def detail(request,user_name):

	
	try: 
		user= User.objects.get(username=user_name)
		user_info= UserInfo.objects.get(user=user)
		gifts=Gift.objects.filter(user=user)
		
		context_dict={'username':user,'user_info':user_info, 'gifts':gifts}

	except User.DoesNotExist:

		return redirect('index')

	return render(request,'wishlist/detail.html',context_dict)


def gift_detail(request,user_name,gift_name):
	

	try:
		user= User.objects.get(username=user_name)
		gift=Gift.objects.get(slug=gift_name)
		if request.method == 'POST':
			if 'gifted' in request.POST:
				gift.gifted=True
				gift.save()
			if 'delete' in request.POST:
				gift.delete()
				return redirect('/user/%s' %(user_name))

		context_dict={'username':user,'gift':gift}

	except User.DoesNotExist:
		return redirect('index')
	except Gift.DoesNotExist:
		return redirect('/user/%s' %(user_name))
		
	return render(request,'wishlist/gift_detail.html',context_dict)

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username,password=password)

		if user:
			login(request,user)
			if password=="xmas":
				return HttpResponseRedirect("/password")
			else:
				return HttpResponseRedirect('/')
		else:
			print "Invalid login details"
			return render(request, 'wishlist/login.html', {'error':True})


	else:
			return render(request, 'wishlist/login.html', {'error':False})




@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/')



def add_gift(request,user_name):
	if request.method == 'POST':
			form= GiftForm(request.POST)

			if form.is_valid():
				gift=form.save(commit=False)
				gift.clean()
				gift.user = User.objects.get(username=user_name)
				gift.save()

				return HttpResponseRedirect('/user/{}'.format(user_name))

			else:
				print form.errors
	else:
			form= GiftForm()

	return render(request, 'wishlist/add_gift.html',{'form':form,'username':user_name})


class GiftUpdate(UpdateView):
	model = Gift
	fields =['short_name','description','link']
	

class AddressUpdate(UpdateView):
	model = UserInfo
	fields =['address_street','address_city','address_state','address_zip']
	template_name='wishlist/userinfo_form.html'

	def get_object(self):
		obj = UserInfo.objects.get(user=self.request.user)
		return obj

	def get_success_url(self):
		return reverse('detail',kwargs={'user_name':self.request.user.username})


class UserUpdate(UpdateView):
	model = User
	fields =['first_name','last_name','email']
	template_name='wishlist/email_form.html'
	def get_object(self, queryset=None):
		obj = User.objects.get(username=self.request.user.username)
		return obj

	def get_success_url(self):
		return reverse('detail',kwargs={'user_name':self.request.user.username})



