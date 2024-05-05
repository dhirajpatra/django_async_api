# movies/views.py
from django.shortcuts import render
from django.http import JsonResponse
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
        return {"success": True, "message": "Theatres fetched successfully", "data": list(qs.values())}
    except Exception as e:
        return {"success": False, "error": str(e)}


# Get all movies (asynchronous)
async def get_movies_async():
    try:
        print("Getting movies ...")
        await asyncio.sleep(2)  # Simulating asynchronous I/O operation
        qs = await asyncio.to_thread(Movies.objects.all)
        print(qs)
        print("All movies fetched")
        return {"success": True, "message": "Movies fetched successfully", "data": list(qs.values())}
    except Exception as e:
        return {"success": False, "error": str(e)}


# Get all theatres (asynchronous)
async def get_theatres_async():
    try:
        print("Getting theatres ...")
        await asyncio.sleep(5)  # Simulating asynchronous I/O operation
        qs = await asyncio.to_thread(Theatres.objects.all)
        print(qs)
        print("All theatres fetched")
        return {"success": True, "message": "Theatres fetched successfully", "data": list(qs.values())}
    except Exception as e:
        return {"success": False, "error": str(e)}


# Calculate time taken for synchronous view
def sync_view(request):
    try:
        start_time = time.time()
        movies_response = get_movies()
        theatres_response = get_theatres()
        total = time.time() - start_time
        return JsonResponse({"time_taken": total, "movies": movies_response, "theatres": theatres_response})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Calculate time taken for asynchronous view
async def async_view(request):
    try:
        start_time = time.time()
        movies_response = await get_movies_async()
        theatres_response = await get_theatres_async()
        total = time.time() - start_time
        return JsonResponse({"time_taken": total, "movies": movies_response, "theatres": theatres_response})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
