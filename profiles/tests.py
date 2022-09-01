import pytest

from django.urls import reverse
from django.test import Client

from django.contrib.auth.models import User
from .models import Profile

@pytest.mark.django_db
def test_profiles_index():
    client = Client()
    url = reverse('profiles_index')
    response = client.get(url)
    assert response.status_code == 200
    assert '<title>Profiles</title>' in str(response.content)


@pytest.mark.django_db
def test_profiles_profile():
    client = Client()
    username_test = "test_profile"
    User.objects.create(username=username_test, email="test@mail.com",
                        first_name="John", last_name="Doe", password="azer1234")
    Profile.objects.create(user=User.objects.get(id=1), favorite_city="Paris")
    url = reverse("profile", kwargs={"username": username_test})
    response = client.get(url)
    assert response.status_code == 200
    assert f"<title>{username_test}</title>" in str(response.content)
