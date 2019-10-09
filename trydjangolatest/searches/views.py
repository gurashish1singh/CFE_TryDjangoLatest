from django.shortcuts import render
from .models import *

# Create your views here.
def search_view(request):

    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)

    template_name = 'searches/view.html'
    context = {
        'query': query
    }
    return render(request, template_name, context)