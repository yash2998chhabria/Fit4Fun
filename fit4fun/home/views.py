from django.shortcuts import render
from .models import activity
from django_user_agents.utils import get_user_agent
# Create your views here.
def home(request):
    activities = activity.objects.all()
    context = {
        'activities':activities
    }
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return render(request, "mobileindex.html", context)
    else:
        return render(request, "index.html", context)