from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from tgbot.models import Place, Training, User, Dnevnik


# class CustomAdmin(UserAdmin):
#     add_form_template = "admin/auth/user/add_form.html"
#     change_user_password_template = None
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         (_("Personal info"), {"fields": ("first_name", "age", "weight", "height", "gender",
#                                          "lvl", "training_goal", "place")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "password1", "password2"),
#             },
#         ),
#     )
#     form = UserChangeForm
#     add_form = UserCreationForm
#     change_password_form = AdminPasswordChangeForm
#     list_display = ("username", "first_name",  "is_staff",)
#     list_filter = ("is_staff", "is_superuser", "is_active", "groups")
#     search_fields = ("username", "first_name")
#     ordering = ("username",)
#     filter_horizontal = (
#         "groups",
#         "user_permissions",
#     )


# Register your models here.
admin.site.register(Place)
admin.site.register(Training)
admin.site.register(Dnevnik)
admin.site.register(User)
