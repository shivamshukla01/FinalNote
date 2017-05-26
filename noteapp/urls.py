from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^branch/(?P<shortname>.+)/$', views.branchview, name='branchview'), #check later if the name to this url should be changed
	url(r'^subject/(?P<pk>\d+)/$', views.subjectview, name='subjectview'),
	url(r'^note/(?P<pk>\d+)/$', views.noteview, name='noteview'),
	url(r'^comingsoon/$', views.comingsoon, name='comingsoon'),
]