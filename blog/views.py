from django.shortcuts import render

posts = [
    {
        'author':      'John Doe',
        'title':       'Blog Post 1',
        'content':     'First Post Content',
        'date_posted': 'August 1, 2024'
    },
    {
        'author':      'Jane Doe',
        'title':       'Blog Post 2',
        'content':     'Second Post Content',
        'date_posted': 'August 3, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})