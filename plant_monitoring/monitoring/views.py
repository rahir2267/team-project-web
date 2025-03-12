# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PlantData
from django.shortcuts import render

@csrf_exempt  # Allows API to accept POST requests (disable in production)
def add_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            plant_data = PlantData.objects.create(
                temperature=data['temperature'],
                humidity=data['humidity'],
                soil_moisture=data['soil_moisture'],
                air_quality=data['air_quality']
            )
            return JsonResponse({"message": "Data added successfully", "id": plant_data.id})
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({"error": "Invalid data format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=400)


def dashboard(request):
    # Fetch all plant data from the database
    plant_data = PlantData.objects.all()
    return render(request, 'dashboard.html', {'plant_data': plant_data})
