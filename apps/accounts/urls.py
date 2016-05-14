from django.conf.urls import patterns, url
from . import views
from .views import Index, Login, Register
# , Logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', Index.as_view()),
	url(r'^login/$', Login.as_view(), name='accounts-login'),
	url(r'^register/$', Register.as_view(), name='accounts-register'),
	url(r'^success/$', login_required(views.Success.as_view(), login_url = '/accounts/login'), name='accounts-success'),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
	]