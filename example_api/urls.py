from django.urls import path, include
from rest_framework import routers
from .views import DepartmentViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"departments", DepartmentViewSet)
router.register(r"employees", EmployeeViewSet)

urlpatterns = [path("", include(router.urls))]  # PetViewSet.as_view({"get": "list"})),
