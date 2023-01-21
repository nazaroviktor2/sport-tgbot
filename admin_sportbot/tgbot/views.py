from django.shortcuts import render, get_object_or_404
from tgbot.models import User, Dnevnik, Place, Training
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
USERS_ON_PAGE = 5

muscle_groups = {
    1: "Спина",
    2: "Грудь",
    3: "Ноги",
    4: "Руки",
    5: "Бицепс",
    6: "Трицепс",
    7: "Трапеции",
    8: "Плечи",
    9: "Пресс",
    10: "Разминка",
    11: "Функциональная",
    12: "Кардио"
}

gender = {
    "M": "Мужской", "F": "Женский", "M/F": "М/Ж"
}


def home_page(request):
    return render(request, "index.html")


def add_training(request):
    place = (Place.objects.all())

    if request.method == "GET":
        pass

    else:
        print(request.POST)
        name = request.POST.get("name")
        description = request.POST.get("description")
        user_lvl = request.POST.get("user_lvl")
        user_gender = request.POST.get("user_gender")
        user_type_training = request.POST.get("user_type_training")
        places = request.POST.getlist("places")
        user_muscles = request.POST.get("user_muscles")

        training = Training(name=name, description=description, lvl=int(user_lvl),
                            type=user_type_training, gender=user_gender, muscle_group=muscle_groups[int(user_muscles)])
        training.save()
        for place in places:
            training.places.add(place)
            training.save()
    return render(request, "add_training.html", {"places": place, "muscle_groups": muscle_groups,
                                                 "gender": gender})


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

    return render(request, "user_characteristics.html", {"user": user, "dnevniks": dnevniks})
