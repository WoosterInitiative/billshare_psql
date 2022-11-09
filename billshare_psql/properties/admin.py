from django.contrib import admin

from .models import Property


# Register your models here.
class BaseAdminModel(admin.ModelAdmin):
    class Meta:
        abstract = True

    def save_model(self, request, obj, form, change) -> None:
        if not change:
            obj.created_by = request.user

        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Property)
class PropertyAdmin(BaseAdminModel):
    list_display = ["name", "responsible_user", "address_line_1"]

    # @admin.display(description="Address")
    # def address_one_line(self, obj):
    #     line_1 = self.address_line_1
    #     line_2 = self.address_line_2
    #     city = self.city
    #     state = self.state
    #     zip_code = self.zip_code
    #     rvalue = f"{line_1} {line_2}, {city}, {state.code} {zip_code}"

    #     return rvalue
