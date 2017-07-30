from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^notes/branch/(?P<branchname>.+)/(?P<year>[0-4]{1})$', views.branchview, name='branchview'), #check later if the name to this url should be changed
	url(r'^subject/(?P<pk>\d+)/$', views.subjectview, name='subjectview'),
	url(r'^note/(?P<pk>\d+)/$', views.noteview, name='noteview'),
	url(r'^comingsoon/$', views.comingsoon, name='comingsoon'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^contactpost/$', views.savemessage, name='savemessage'),
	url(r'^about/',TemplateView.as_view(template_name = 'about.html'), name='about'),
	url(r'^privacy-policy/',TemplateView.as_view(template_name = 'privacy.html'), name='privacy'),
	url(r'^disclaimer/',TemplateView.as_view(template_name = 'disclaimer.html'), name='disclaimer'),
	url(r'^meet/',TemplateView.as_view(template_name = 'meet.html'), name='meet'),
	url(r'^terms-of-use/',TemplateView.as_view(template_name = 'tou.html'), name='tou'),
	url(r'^services/',TemplateView.as_view(template_name = 'services.html'), name='services'),
	url(r'^paper/branch/(?P<branchname>.+)/(?P<year>[0-4]{1})$', views.paperbranchview, name='paperbranchview'),
	url(r'^paper/subject/(?P<pk>\d+)/$', views.papersubjectview, name='papersubjectview'),
	url(r'^paper/(?P<pk>\d+)/$', views.paperview, name='paperview'),
]