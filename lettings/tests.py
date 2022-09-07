import pytest

from django.urls import reverse
from django.test import Client
from .models import Letting, Address


@pytest.mark.django_db
def test_lettings_index():
    client = Client()
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Lettings</title>" in str(response.content)


@pytest.mark.django_db
def test_letting_letting():
    client = Client()
    title_test = "test_lettings"
    Address.objects.create(
        number=1,
        street="test street",
        city="djangoTown",
        state="az",
        zip_code=1337,
        country_iso_code="abf",
    )
    Letting.objects.create(title=title_test, address=Address.objects.get(id=1))
    url = reverse("letting", kwargs={"letting_id": 1})
    response = client.get(url)
    assert response.status_code == 200
    assert f"<title>{title_test}</title>" in str(response.content)
