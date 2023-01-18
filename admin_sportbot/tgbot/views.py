from django.shortcuts import render
from tgbot.models import UserBot
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
USERS_ON_PAGE = 20
def home_page(request):
    return render(request, "index.html")


def users_page(request):
    cards = UserBot.objects.all().order_by('id')
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
    return render(request, "users.html", {"cards": page_obj, "nums":nums})