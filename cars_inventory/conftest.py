import pytest

from rest_framework.test import APIClient

from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_api_client():
    class APIClientWithUser(APIClient):
        user = User.objects.create()

    client = APIClientWithUser()
    client.force_authenticate(user=client.user)
    return client
