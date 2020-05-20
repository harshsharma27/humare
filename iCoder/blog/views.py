from django.shortcuts import render, HttpResponse
from blog.models import Aut
from blog.models import Post
from blog.models import Author


# Create your views here.
def ab(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        ab.save()

    return render(request,'blog/an.html')
def blogHome(request):
    # return HttpResponse('This is bloghome. We will keep all the blog post')

    b_ab = Aut.objects.all()
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts,'b_ab':b_ab}
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, slug):
    babo = Aut.objects.all()
    post = Post.objects.filter(slug=slug).first
    context = {'post': post,'babo':babo}

    return render(request, 'blog/blogPost.html', context)
    # return HttpResponse(f'This is blogPost: {slug}')


def abou(request):
    babou = Aut.objects.all()
    ab = Author.objects.all()
    context = {'ab': ab,'babou':babou}
    return render(request, 'blog/abou.html', context)