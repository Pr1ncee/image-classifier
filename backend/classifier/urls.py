from django.urls import include, path
from rest_framework import routers

from classifier.views import CategoryListView, ImageViewSet

app_name = "classifier"

router = routers.DefaultRouter()
router.register(r"images", ImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("categories/", CategoryListView.as_view(), name="category-list"),
]

urlpatterns += router.urls
