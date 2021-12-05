from django.contrib import admin
from .models import Car, CarInstance

# admin.site.register(Car)
# admin.site.register(CarInstance)


class CarInstanceInline(admin.TabularInline):
    model = CarInstance

    extra = 0


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make", "body_type", "mileage", "location")

    list_filter = ("make", "body_type", "mileage", "location")

    inlines = [CarInstanceInline]


@admin.register(CarInstance)
class CarInstanceAdmin(admin.ModelAdmin):
    list_display = ("car", "price", "due_date", "status", "id")

    list_filter = ("status", "due_date", "price")


