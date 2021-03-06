from django.shortcuts import render
from django.utils import timezone
from .models import Note, Subject, Branch, Paper
from django.http import Http404
from .forms import Contactform

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

	g=subjects.filter(featured=True)
	subjects2=g[:4]
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
		context={'notes':notes, 'branches':branches, 'subjects':subjects, 'subjects2':subjects2},
	)


def branchview(request, branchname='all', year='0'):
	branches=Branch.objects.all()
	subjects=Subject.objects.all()
	flag=0
	if(branchname=='all'):
			branch=Branch.objects.get(branch_short="all")
			if(year=='0'):
				flag=1
				return render(
					request,
					'branchview.html',
					context={'selectedbranch':branch, 'subjects':subjects,'year':year, 'branches':branches},
				)
			else:
				flag=1
				subjects=branch.included_subjects.filter(year=year)
				return render(
					request,
					'branchview.html',
					context={'selectedbranch':branch, 'subjects':subjects,'year':year, 'branches':branches},
				)
	else:
		for branch in branches:
			if branch.branch_short==branchname:
				if(year=='0'):	
					flag=1
					subjects=branch.included_subjects.all()
					return render(
						request,
						'branchview.html',
						context={'selectedbranch':branch, 'subjects':subjects,'year':year, 'branches':branches},
					)
				else:
					flag=1
					subjects=branch.included_subjects.filter(year=year)
					return render(
					request,
					'branchview.html',
					context={'selectedbranch':branch, 'subjects':subjects,'year':year, 'branches':branches},
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


def contact(request):
	return render(
		request,
		'contactform.html',
		context={},
	)

def savemessage(request):
	if request.method == "POST":
		MyContactform = Contactform(request.POST)

		if MyContactform.is_valid():
			new_contact=MyContactform.save()
			fname=new_contact.fname
		return render(request, 'contactpost.html', {"fname":fname})


def paperbranchview(request, branchname='all', year= '0'):
	branches=Branch.objects.all()
	subjects=Subject.objects.all()
	flag=0
	if(branchname=='all'):
			branch=Branch.objects.get(branch_short="all")
			if(year=='0'):
				flag=1
				return render(
					request,
					'paperbranchview.html',
					context={'selectedbranch':branch, 'subjects':subjects,'year':year, 'branches':branches},
				)
			else:
				flag=1
				subjects=branch.included_subjects.filter(year=year)
				return render(
					request,
					'paperbranchview.html',
					context={'selectedbranch':branch, 'subjects':subjects,'year':year, 'branches':branches},
				)
	else:
		for branch in branches:
			if branch.branch_short==branchname:
				if(year=='0'):	
					flag=1
					subjects=branch.included_subjects.all()
					return render(
						request,
						'paperbranchview.html',
						context={'selectedbranch':branch, 'subjects':subjects,'year':year, 'branches':branches},
					)
				else:
					flag=1
					subjects=branch.included_subjects.filter(year=year)
					return render(
					request,
					'paperbranchview.html',
					context={'selectedbranch':branch, 'subjects':subjects,'year':year, 'branches':branches},
				)


	if(flag==0):
		raise Http404("Subject does not exist")

def papersubjectview(request, pk):
	subject=Subject.objects.get(pk=pk)
	papers=subject.paper_set.all()
	return render(
		request,
		'papersubjectview.html',
		context={'papers':papers, 'subject':subject},
	)

def paperview(request, pk):
	paper=Paper.objects.get(pk=pk)
	return render(
		request,
		'paperview.html',
		context={'paper':paper},
	)