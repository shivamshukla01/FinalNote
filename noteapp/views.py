from django.shortcuts import render
from django.utils import timezone
from .models import Note, Subject, Branch
from django.http import Http404

def index(request):
	"""
 	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	notes=Note.objects.all()
	branches=Branch.objects.all().exclude(branch_short__contains='all')
	subjects=Subject.objects.all()
	f=notes.filter(published_date__lte=timezone.now())
	notes=f.order_by('-created_date')[:4]
	for branch in branches:
		branch.non=0
		inc=branch.included_subjects.all()
		for i in inc:
			branch.non=branch.non+ i.note_set.all().count()

		branch.nos=inc.count()
	



	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'notes':notes, 'branches':branches, 'subjects':subjects},
	)


def branchview(request, shortname='all'):
	branches=Branch.objects.all()
	subjects=Subject.objects.all()
	flag=0
	if(shortname=='all'):
			flag=1
			branch=Branch.objects.get(branch_short="all")
			return render(
			request,
			'branchview.html',
			context={'branch':branch, 'subjects':subjects},
		)

	else:
		for branch in branches:
			if branch.branch_short==shortname:
				flag=1
				subjects=branch.included_subjects.all()
				return render(
					request,
					'branchview.html',
					context={'branch':branch, 'subjects':subjects},
					)
	if(flag==0):
		raise Http404("Subject does not exist")		


def subjectview(request, pk):
	subject=Subject.objects.get(pk=pk)
	notes=subject.note_set.all()
	return render(
		request,
		'subjectview.html',
		context={'notes':notes, 'subject':subject},
	)

def noteview(request, pk):
	note=Note.objects.get(pk=pk)
	return render(
		request,
		'noteview.html',
		context={'note':note},
	)

def comingsoon(request):
	return render(
		request,
		'comingsoon.html',
		context={},
	)
