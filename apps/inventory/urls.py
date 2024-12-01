from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'common-items', views.CommonItemViewSet)
router.register(r'grocery-stores', views.GroceryStoreViewSet)
router.register(r'grocery-store-items', views.GroceryStoreItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 