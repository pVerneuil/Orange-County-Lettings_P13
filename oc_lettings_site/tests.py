import pytest

from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_oc_lettings_site_home():
    client = Client()
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in str(response.content)