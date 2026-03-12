from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.http import HttpResponse

@csrf_exempt
def api_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            return JsonResponse({"Status": "Success"})
        else:
            return JsonResponse({"Status": "Failure", "Message": "Invalid credentials"})

    return JsonResponse({"Status": "Failure"})



def create_admin(request):
    User.objects.create_superuser("admin2", "admin2@example.com", "StrongPassword123")
    return HttpResponse("Superuser created")