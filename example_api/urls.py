from django.urls import path
from rest_framework import routers
from .views import PetViewSet

router = routers.DefaultRouter()
router.register(r"pets", PetViewSet)

urlpatterns = [
    path("pets/", PetViewSet.as_view({"get": "list"})),
]
