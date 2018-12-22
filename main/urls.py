from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from main.forms import LoginForm

urlpatterns = [
	url(r'', include('social.apps.django_app.urls', namespace='social')),
	url(r'', include('django.contrib.auth.urls', namespace='auth')),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signup_ok/$', TemplateView.as_view(
        template_name='registration/signup_ok.html'
    ), name='signup_ok'),
	url(r'^login/', auth_views.login, {
        'authentication_form': LoginForm
    	}, name='login_url'),
	url(r'^logout/', auth_views.logout, {
        'next_page': '/login/',
    	}, name='logout_url'),
	url(r'^about/$', TemplateView.as_view(
        template_name='about.html'
    ), name='about'),
    url(r'^summernote/', include('django_summernote.urls')),
   
    #url(r'^question/(?P<question_id>[0-9]+)/$', 'question',
    #	name='view_question'),
    # url(r'^question/(?P<question_id>[0-9]/\
    #     comment/(?P<comment_id>[0-9]+)/(?P<status>up|down)/$', 'popularity',
    #     name='comment_popularity'),
    #url(
    #    r'^question/comment/(?P<comment_id>[0-9]+)/(?P<status>up|down)/$',
    #    'popularity', name='comment_popularity'),
    #url(r'^post/$', 'post', name='post'),
]


'''
url(r'^$', 'qna.views.home', name='home'),
'''