from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserRegistrationForm


class UserAdmin(BaseUserAdmin):
    add_form = UserRegistrationForm

    list_display = [
        "email",
        "username",
        "is_staff",
        "is_active",
    ]

    list_filter = ["is_staff", "is_active", "date_joined"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_active", "is_staff"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                ],
            },
        ),
    ]

    search_fields = [
        "email",
    ]

    ordering = [
        "email",
    ]

    filter_horizontal = []

    # def save_model(self, request, obj, form, change):
    #     if obj.username is None:
    #         obj.username = generate_username()[0]
    #     if not obj.is_active:
    #         obj.is_active = True
    #     super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
