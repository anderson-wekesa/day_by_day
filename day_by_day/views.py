from django.shortcuts import render
from .models import Article, Message

# Create your views here.

#Home Page
def home_page(request):
    page_name = "Home"
    articles = Article.objects.all()

    context = {'page_title': page_name, 'articles' : articles}
    return render(request, "index.html", context)

#About Page
def about_page(request):
    page_name = "About Me"
    context = {'page_title': page_name}
    return render(request, "about.html", context)

#Test Post
def post_page(request, post_slug):
    content = Article.objects.get(post_slug=post_slug)
    context = {'article': content}

    return render(request, "post.html", context)


#Contacts Page
def contact_page(request):
    if request.method=="POST":
        data = Message()
        post_data = request.POST
        data.name = post_data.get ('name')
        data.email = post_data.get ('email')
        data.phone = post_data.get ('phone')
        data.message = post_data.get ('message')

        data.save()

        response = "Message Successfully Sent!"

        context = {'message': response}
        return render(request, 'contact.html', context)
    else:
        #This is a GET Operation, so just return the page as it is.
        return render(request, 'contact.html')

