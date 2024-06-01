from classifier.enums.category_enum import CategoryEnum


class CategoryMapper:
    """
    This class maps our predefined categories with existing classes in the model since
    ImageNet pre-trained model has 1000 clases.
    """

    MAPPING = {
        CategoryEnum.CAT: ["tiger", "lion", "cheetah", "Persian_cat", "Egyptian_cat"],
        CategoryEnum.DOG: [
            "Labrador_retriever",
            "golden_retriever",
            "German_shepherd",
            "beagle",
            "pug",
        ],
        CategoryEnum.CAR: [
            "sports_car",
            "convertible",
            "minivan",
            "ambulance",
            "fire_engine",
        ],
        CategoryEnum.PLANE: ["airliner", "wing", "airship", "parachute", "warplane"],
        CategoryEnum.BIRD: ["bird", "hummingbird", "bald_eagle", "magpie", "macaw"],
    }

    @classmethod
    def get_category(cls, class_name: str) -> str:
        for category_enum, imagenet_objects in cls.MAPPING.items():
            if class_name in imagenet_objects:
                return category_enum
        return "Unknown"
