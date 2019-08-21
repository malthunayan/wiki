from django.shortcuts import render
from .models import Page

# Create your views here.
def wiki_list(request):
	context = {
			'pages': Page.objects.all(),
	}
	return render(request, 'list.html', context)

def wiki_detail(request, wiki_id):
	context = {
			'page': Page.objects.get(id=wiki_id)
	}
	return render(request, 'detail.html', context)