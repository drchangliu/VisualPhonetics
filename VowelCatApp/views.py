from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import MyRegistrationForm, MyChangeForm

def home(request):
   c = {}
   c.update(csrf(request))
   if request.user.is_authenticated():
     return render_to_response('user_home.html', c, context_instance=RequestContext(request))
   return render_to_response('login_home.html', c, context_instance=RequestContext(request))

def logout(request):
   auth.logout(request)
   return render_to_response('logout.html', context_instance=RequestContext(request))

def loggedin(request):
   return render_to_response('user_home.html', context_instance=RequestContext(request))

def invalid_login(request):
   return render_to_response('invalid_login.html', context_instance=RequestContext(request))

def auth_view(request):
   username = request.POST.get('username', '')
   password = request.POST.get('password', '')
   user = auth.authenticate(email=username, password=password)

   if user is not None:
     auth.login(request, user)
     return HttpResponseRedirect(reverse('home'))
   else:
     return HttpResponseRedirect(reverse('invalid'))

def register_user(request):
   args = {}
   args.update(csrf(request))

   if request.method == 'POST':
      form = MyRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse('register_success'))
      else:
         args = {}
         args.update(csrf(request))
         args['form'] = form
   else:
       args = {}
       args.update(csrf(request))
       args['form'] = MyRegistrationForm()

   return render_to_response('register.html', args, context_instance=RequestContext(request))

def register_success(request):
   return render_to_response('register_success.html', context_instance=RequestContext(request))


@login_required(login_url='/')
def update_user(request):
    if request.method == 'POST':
        form = MyChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = MyChangeForm(instance=request.user)
    return render_to_response('update_user.html', {'form': form}, context_instance=RequestContext(request))


@login_required(login_url='/')
def files(request):
  return render_to_response('files.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def practice(request):
  return render_to_response('practice.html', context_instance=RequestContext(request))

def download(request):
  if request.user.is_authenticated():
    base_template_name = 'user_download.html'
  else:
    base_template_name = 'login_download.html'
  return render_to_response('download.html', {'base_template_name':base_template_name}, context_instance=RequestContext(request))

@login_required(login_url='/')
def listening(request):
  return render_to_response('listening.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def training(request):
  return render_to_response('training.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def upload(request):
  return render_to_response('upload.html', context_instance=RequestContext(request))
