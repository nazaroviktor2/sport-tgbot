from django.shortcuts import render, get_object_or_404
from tgbot.models import User, Dnevnik
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
USERS_ON_PAGE = 20


def home_page(request):
    return render(request, "index.html")

def add_training(request):


    if request.GET:
        return render(request, "add_training.html")
    else:
        print(1)
        print(request.POST)
        return render(request, "add_training.html")
def users_page(request):
    cards = User.objects.all().order_by('id')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(cards, USERS_ON_PAGE)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    nums = "a" * page_obj.paginator.num_pages

    return render(request, "users.html", {"users": page_obj, "nums": nums})


def about_user(request):
    user = get_object_or_404(User, id=request.GET.get("id"))
    dnevniks = Dnevnik.objects.filter(user=request.GET.get("id")).order_by('-id')
    print(dnevniks)
    print(dnevniks[0].trainings.all())
    return render(request, "user_characteristics.html", {"user": user, "dnevniks": dnevniks})
