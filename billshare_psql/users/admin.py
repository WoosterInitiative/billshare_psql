from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from billshare_psql.users.forms import UserAdminChangeForm, UserAdminCreationForm
from billshare_psql.users.models import PhoneNumber, PhoneNumberType

User = get_user_model()


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "name",
                    "email",
                    "address_line_1",
                    "address_line_2",
                    "zip_code",
                    "city",
                    "state",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name", "city", "state"]
    inlines = [PhoneNumberInline]


@admin.register(PhoneNumberType)
class PhoneNumberTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ["number", "user", "type"]
