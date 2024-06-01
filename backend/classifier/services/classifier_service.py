import logging
from pathlib import Path

import cv2
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (decode_predictions,
                                                        preprocess_input)

from image_classifier.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


class MobileNetClassifier:
    """
    A classifier implements methods for preparing and predicting image's category.
    The reason I chose tensorflow as a machine learning platform
    is just because it's lightweight (in comparison with pytorch) and very easy to integrate with.
    """

    def __init__(self, image_path: str | Path, category_mapper: type) -> None:
        self.dsize = (224, 224)
        self.model = MobileNetV2(weights="imagenet")
        self.image_path = image_path
        self.mapper = category_mapper

    def preprocess_image(self) -> np.ndarray:
        """
        Read, resize and preprocess input image
        :return: ndarray of the image
        """
        logger.info(f"Preprocessing the image <{self.image_path}>...")
        img = cv2.imread(self.image_path)  # Read the image

        img = cv2.resize(img, self.dsize)  # Resize to the size the model expects
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB

        img = preprocess_input(img)
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        return img

    def classify_image(self) -> str:
        """
        Call the model to predict image's category
        :return: predicted category name
        """
        img = self.preprocess_image()

        logger.info("Predicting the class from the image...")
        preds = self.model.predict(img)

        decoded_preds = decode_predictions(preds, top=1)[0][0]
        class_name = decoded_preds[1]
        logger.info(f"Predicted class name is <{class_name}>")

        logger.info("Mapping the class name with the defined categories...")
        category_name = self.mapper.get_category(class_name=class_name)
        return category_name
