from enum import Enum

class KeywordsEnum(Enum):
    @classmethod
    def get_all_values(cls):
        return [x.value for x in cls]

class MenKeywords(KeywordsEnum):
    MEN = 'men'
    MALE = 'male'
    MAN = 'man'

class WomenKeywords(KeywordsEnum):
    WOMEN = 'women'
    FEMALE = 'female'
    WOMAN = 'woman'

class FashionItemKeywords(KeywordsEnum):
    ACCESSORIES = 'accessories'
    CLOTHING = 'clothing'
    WATCHES = 'watches'
    JEWELRY = 'jewelry'
    SHOES = 'shoes'
    HANDBAGS = 'handbags'
