from decimal import Decimal

from django.test import TestCase

from itemise.models import Item, Bill


class BillTest(TestCase):
    fixtures = ["bills.json", ]

    def test_bill(self):
        bill = Bill.objects.get(id=1)
        total = bill.total()

        expected = Decimal("98.50")
        self.assertEqual(expected, total)

