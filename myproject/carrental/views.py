from django.shortcuts import render
from .models import Car, CarInstance


def index(request):
    """View function for home page of website."""

    num_cars = Car.objects.all().count()
    num_instances = CarInstance.objects.all().count()

    # Available cars (status = "a")
    num_instances_available = CarInstance.objects.filter(status__exact="a").count()
    num_instances_taken = CarInstance.objects.filter(status__exact="u").count()
    num_instances_reserved = CarInstance.objects.filter(status__exact="r").count()

    context = {
        "num_cars": num_cars,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_instances_taken": num_instances_taken,
        "num_instances_reserved": num_instances_reserved,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
