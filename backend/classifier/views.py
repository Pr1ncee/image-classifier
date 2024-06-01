import logging

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from classifier.enums.category_enum import CategoryEnum
from classifier.mappers.category_mapper import CategoryMapper
from classifier.models import Image
from classifier.serializers import ImageSerializer
from classifier.services.classifier_service import MobileNetClassifier
from image_classifier.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        logger.info(
            f"Creating a new Image object with category "
            f"assigned by user <{serializer.validated_data['category_by_user']}>"
        )
        self.perform_create(serializer),

        image_instance = serializer.instance
        image_path = image_instance.image.path

        logger.info("Calling the classifier to predict category...")
        model = MobileNetClassifier(
            image_path=image_path, category_mapper=CategoryMapper
        )
        category_name = model.classify_image()

        logger.info(f"Predicted category name is <{category_name}>")
        image_instance.category_by_ai = category_name
        image_instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class CategoryListView(APIView):
    def get(self, request):
        categories = CategoryEnum.get_list_values()
        return Response(categories, status=status.HTTP_200_OK)
