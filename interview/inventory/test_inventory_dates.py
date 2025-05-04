from django.test import TestCase
from django.urls import reverse

from interview.inventory.models import Inventory, InventoryLanguage, InventoryTag, InventoryType
from datetime import datetime

class InventoryListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_language = InventoryLanguage.objects.create(
            name="EN")

        test_type =InventoryType.objects.create(
            name="TestType")

        test_tag = InventoryTag.objects.create(
            name="TestTag")

        Inventory.objects.create(
            created_at=datetime.now(),
            name="TestInventory",
            type=test_type,
            language=test_language
            ).tags.set([test_tag])

    def test_Testing(self):
        """WIP"""
        self.assertEqual(Inventory.objects.all().count(), 1)
