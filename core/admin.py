from django.contrib import admin
from .models import Contact, Interaction


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "company",
        "user",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "email", "company")
    list_filter = ("company", "created_at")
    ordering = ("-created_at",)


class InteractionAdmin(admin.ModelAdmin):
    list_display = ("contact", "date", "type", "created_at", "updated_at")
    search_fields = ("contact__name", "type")
    list_filter = ("type", "date", "created_at")
    ordering = ("-date",)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Interaction, InteractionAdmin)
