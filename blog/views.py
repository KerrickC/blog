from django.shortcuts import render #for importing HTML template
#from django.http import HttpResponse <- dont need
from .models import Post
from django.views.generic import ListView
from django.contrib import messages

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #still returns HTTP response

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    







    
