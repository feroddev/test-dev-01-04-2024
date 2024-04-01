from django.shortcuts import render
from calculator_python import calculator
from calculator.models import Consumer
from asgiref.sync import sync_to_async


# TODO: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
    if request.method == "POST":
        name = request.POST["name"]
        document = request.POST["document"]
        consumption_values = [
            float(request.POST["consumption1"]),
            float(request.POST["consumption2"]),
            float(request.POST["consumption3"]),
        ]
        avg_consumption = round(sum(consumption_values) / 3, 2)
        distributor_tax = float(request.POST["distributor_tax"])
        tax_type = request.POST["tax_type"]
        city = request.POST["city"]
        state = request.POST["state"]
        (
            annual_savings,
            month_savings,
            applied_discount,
            coverage,
        ) = calculator(consumption_values, distributor_tax, tax_type)

        Consumer.objects.create(
            name=name,
            document=document,
            city=city,
            state=state,
            consumption=avg_consumption,
            consumer_type=tax_type,
            cover_value=coverage,
            distributor_tax=distributor_tax,
        )

        get_all_consumers = Consumer.objects.all()

        return render(
            request,
            "calculator/list.html",
            {"consumers": get_all_consumers},
        )
    else:
        return render(request, "calculator/calculate.html", {})


def view2(request):
    # if request.method == "GET":
    consumers = Consumer.objects.all()

    return render(request, "calculator/list.html", {"consumers": consumers})
