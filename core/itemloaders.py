from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
import re


class MedicineItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    usage_in = MapCompose(lambda x: re.sub(r"</?a[^>]*>|</?p[^>]*>", "", x))
