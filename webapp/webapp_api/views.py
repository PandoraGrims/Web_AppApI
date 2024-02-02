from django.http import JsonResponse, HttpResponseBadRequest
import json
from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def view_add(request, *args, **kwargs):
    return api_calculator(request, 'add')


def view_subtract(request, *args, **kwargs):
    return api_calculator(request, 'subtract')


def view_multiply(request, *args, **kwargs):
    return api_calculator(request, 'multiply')


def view_divide(request, *args, **kwargs):
    return api_calculator(request, 'divide')


def api_calculator(request, method_calculator):
    data = json.loads(request.body)
    a = data.get("A")
    b = data.get("B")

    if isinstance(a, (int, float)) or isinstance(b, (int, float)):
        if method_calculator == 'add':
            result = a + b
            return JsonResponse({"answer": result})
        elif method_calculator == 'subtract':
            result = a - b
            return JsonResponse({"answer": result})
        elif method_calculator == 'multiply':
            result = a * b
            return JsonResponse({"answer": result})
        elif method_calculator == 'divide':
            if b == 0:
                return HttpResponseBadRequest(json.dumps({"error": "Делить на ноль сегодня нельзя :("}),
                                              content_type="application/json")
            else:
                result = a / b
                return JsonResponse({"answer": result})
    else:
        return JsonResponse({"error": "A и B должны быть числами"}, status=400)
