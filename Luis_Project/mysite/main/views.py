from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Submission
from .forms import SubmissionForm

# Create your views here.

def sub_history(response):
	sub = Submission.objects.all().values()
	data = {'sub' : sub}
	return render(response, "main/base.html", data)

def home(response):

	if response.method == "POST":
		form = SubmissionForm(response.POST)
		print(form.is_valid())
		if form.is_valid():
			name_data = form.cleaned_data["name"]
			email_data = form.cleaned_data["email"]
			sub_instance = Submission(name=name_data, email=email_data)
			sub_instance.save()
			return HttpResponseRedirect("/sub_history/")
			
	else:
		form = SubmissionForm()
	return render(response, "main/home.html", {"form": form})