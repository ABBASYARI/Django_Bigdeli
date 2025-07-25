from django.shortcuts import render


def calculator_view(request):
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operation = request.POST.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2
        except Exception as e:
            result = "خطا: " + str(e)

    return render(request, "website/calculator.html", {"result": result})


def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/about.html")


def contact(request):
    return render(request, "website/contact.html")
