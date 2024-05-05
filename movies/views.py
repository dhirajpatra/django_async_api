# movies/views.py
from django.shortcuts import render
from django.http import JsonResponse
from channels.db import database_sync_to_async
import time
from .models import Movies, Theatres
import asyncio


# Get all movies (synchronous)
def get_movies():
    try:
        print("Getting movies ...")
        time.sleep(2)  # Simulating I/O operation
        qs = Movies.objects.all()
        print(qs)
        print("All movies fetched")
        return {"success": True, "message": "Movies fetched successfully", "data": list(qs.values())}
    except Exception as e:
        return {"success": False, "error": str(e)}


# Get all theatres (synchronous)
def get_theatres():
    try:
        print("Getting theatres ...")
        time.sleep(5)  # Simulating I/O operation
        qs = Theatres.objects.all()
        print(qs)
        print("All theatres fetched")
        theatres_data = []
        for theatre in qs:
            theatre_data = {"id": theatre.id, "name": theatre.name}
            movies_in_theatre = theatre.movies.all()
            theatre_data["movies"] = list(movies_in_theatre.values("id", "name"))
            theatres_data.append(theatre_data)
        return {"success": True, "message": "Theatres fetched successfully", "data": theatres_data}
    except Exception as e:
        return {"success": False, "error": str(e)}


# Get all movies (asynchronous)
@database_sync_to_async
def get_movies_async():
    try:
        print("Getting movies ...")
        time.sleep(2)  # Simulating I/O operation
        qs = Movies.objects.all()
        print(qs)
        print("All movies fetched")
        return {"success": True, "message": "Movies fetched successfully", "data": list(qs.values())}
    except Exception as e:
        return {"success": False, "error": str(e)}

# Get all theatres (asynchronous)
@database_sync_to_async
def get_theatres_async():
    try:
        print("Getting theatres ...")
        time.sleep(5)  # Simulating I/O operation
        qs = Theatres.objects.all()
        print(qs)
        print("All theatres fetched")
        theatres_data = []
        for theatre in qs:
            theatre_data = {"id": theatre.id, "name": theatre.name}
            movies_in_theatre = theatre.movies.all()
            theatre_data["movies"] = list(movies_in_theatre.values("id", "name"))
            theatres_data.append(theatre_data)
        return {"success": True, "message": "Theatres fetched successfully", "data": theatres_data}
    except Exception as e:
        return {"success": False, "error": str(e)}


# Calculate time taken for synchronous view
def sync_view(request):
    try:
        start_time = time.time()
        movies_response = get_movies()
        theatres_response = get_theatres()
        total = time.time() - start_time
        pretty_response = {
            "time_taken": total,
            "movies": movies_response["data"],
            "theatres": theatres_response["data"]
        }
        return JsonResponse(pretty_response, json_dumps_params={'indent': 4})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Calculate time taken for asynchronous view
async def async_view(request):
    try:
        start_time = time.time()
        # Fetch movies and theatres concurrently using asyncio.gather
        movies_response, theatres_response = await asyncio.gather(
            get_movies_async(),
            get_theatres_async()
        )
        # Unpack the results from the futures
        total = time.time() - start_time
        pretty_response = {
            "time_taken": total,
            "movies": movies_response["data"],
            "theatres": theatres_response["data"]
        }
        return JsonResponse(pretty_response, json_dumps_params={'indent': 4})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
