from rest_framework.routers import DefaultRouter

from .viewsets import ProductViewSet

router = DefaultRouter()
router.register('products-xyz', ProductViewSet, basename="products")
urlpatterns = router.urls
print(router.urls)