from django.shortcuts import render
from blog.models import Post
from vacancy.models import Vacancy



def home(request):
    count_posts = 5       #  count of top items on home page
    count_vacancies = 5

    posts = Post.published.all()
    vacancies = Vacancy.objects.all()
    if len(posts) >= count_posts and len(vacancies) >= count_vacancies:
        context_object = {"posts": posts[:count_posts], "vacancies": vacancies[:count_vacancies]}
    #----------------------- note create other cases

    else:
        context_object = {"posts":posts, "vacancies": vacancies}


    return render(request, 'home/home_page.html', context_object)
