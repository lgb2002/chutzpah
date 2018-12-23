from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from main.forms import SignupForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from main.models import ClubList
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

'''
def login(request):
	return render(request, 'main/login.html')
'''

def home(request, tag=None):
    clublist = ClubList.objects.order_by('-ClubMemberSum')
    return render(request, "index.html", {
    	'clublists': clublist
    })


def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )
    elif request.method == "GET":
        signupform = SignupForm()

    return render(request, "registration/signup.html",{
    		'signupform' : signupform
    })


@login_required
@csrf_exempt
def join(request):
	clublist = ClubList.objects.order_by('-ClubMemberSum')
	if request.method == "POST":
		join_name = request.POST.get('username')
		join_club = request.POST.get('clubname')
		ClubList.objects.get(ClubName = join_club).update(ClubMemberSum=ClubMemberSum+1,ClubMember=join_name)

	return render(request, "index.html",{
		'clublists': clublist
	})