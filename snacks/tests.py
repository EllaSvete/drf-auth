from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snack


class SnackTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_snack = Snack.objects.create(
            title="apple",
            purchaser=testuser1,
            description="Crunchy and delicious.",
        )
        test_snack.save()
    
    def setUp(self):
        self.client.login(username="testuser1", password="pass")
    
    def test_snack_model(self):
        snack = Snack.objects.get(id=1)
        actual_owner = str(snack.purchaser)
        actual_name = str(snack.title)
        actual_description = str(snack.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "apple")
        self.assertEqual(
            actual_description, "Crunchy and delicious."
        )

    def test_get_snack_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = response.data
        self.assertEqual(len(snack), 1)
        self.assertEqual(snack[0]["title"], "apple")

    def test_get_snack_by_id(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = response.data
        self.assertEqual(snack["title"], "apple")

    def test_create_snack(self):
        url = reverse("snack_list")
        data = {
          "purchaser": 1, 
          "title": "chips", 
          "description": "salty"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        snacks = Snack.objects.all()
        self.assertEqual(len(snacks), 2)
        self.assertEqual(Snack.objects.get(id=2).title, "chips")

    def test_update_snacks(self):
        url = reverse("snack_detail", args=(1,))
        data = {
            "purchaser": 1,
            "title": "apple",
            "description": "juicy",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = Snack.objects.get(id=1)
        self.assertEqual(snack.title, data["title"])
        self.assertEqual(snack.purchaser.id, data["purchaser"])
        self.assertEqual(snack.description, data["description"])

    def test_delete_snack(self):
        url = reverse("snack_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        snacks = Snack.objects.all()
        self.assertEqual(len(snacks), 0)
