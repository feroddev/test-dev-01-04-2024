from django.shortcuts import render
from calculator_python import calculator

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
        (
            annual_savings,
            month_savings,
            applied_discount,
            coverage,
        ) = calculator(consumption_values, distributor_tax, tax_type)
        result = (
            name,
            document,
            avg_consumption,
            tax_type,
            coverage,
            applied_discount,
            annual_savings,
            month_savings,
        )

        # Aqui, estou passando todos os dados relevantes para o template list.html
        return render(
            request,
            "calculator/list.html",
            {"results": [result]},
        )
    else:
        return render(request, "calculator/calculate.html", {})


def view2():
    # Create the second view here.
    pass
