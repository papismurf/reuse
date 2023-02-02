from django.http import JsonResponse

from itemise.models import Bill


def bill_json(request):
    """
    :param request:
    :return: Returns all the Bill onjects and their Item objects in the database
    """
    results = {
        "bills": [],
    }

    for bill in Bill.objects.all():
        line = [str(bill), []]
        for item in bill.item_set.all():
            line[1].append(str(item))

        results["bills"].append(line)

    return JsonResponse(results)
