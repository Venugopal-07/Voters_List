from django.shortcuts import render
from .models import Voter
from django.contrib import messages
# Create your views here.

def voter_list(request):
    voters=Voter.objects.all()
    if request.method=="POST":
        voter_name=request.POST.get("voter_name")
        voter_age=int(request.POST.get("age"))
        voter=Voter(voter_name=voter_name,voter_age=voter_age)
        voter.save()
    
    eligible_voters = [voter for voter in voters if voter.voter_age >= 18]
    not_eligible_voters = [voter for voter in voters if voter.voter_age < 18]
    messages.info(request,"Your Application Completed..")
    return render(request, 'voter.html', {'eligible_voters': eligible_voters,'not_eligible_voters': not_eligible_voters,})