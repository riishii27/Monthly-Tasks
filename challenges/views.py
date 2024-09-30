from django.shortcuts import render
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Dont eat any veggies this  month",
    "febuary": "Walk for atleast 20 mins every day!",
    "march": "Learn django for evry day for 20 mins",
    "april": "Learn React every day",
    "may": "Attend all the online lectures every day",
    "june": "Go to office everyday",
    "july": "Start going to gym everday",
    "august": "Start doing yoga everyday",
    "september": "Complete all your homework",
    "october": "Finish the course in this month",
    "november": "Learn data analysis this month",
    "december": None
}
# Create your views here.


def index(request):

    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "text1": month
        })
        return HttpResponse(response_data)
    except:
        raise Http404()

   
