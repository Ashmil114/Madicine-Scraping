import scrapy
from core.items import MedicineItem
from core.itemloaders import MedicineItemLoader


class MedicinespiderSpider(scrapy.Spider):
    name = "medicinespider"
    allowed_domains = ["www.webmd.com"]

    search_letter = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "0",
    ]

    def start_requests(self):
        for letter in self.search_letter:
            yield scrapy.Request(
                f"https://www.webmd.com/drugs/2/alpha/{letter}", self.parse
            )

    def parse(self, response):
        items = response.css("a.alpha-drug-name")
        for item in items:
            medicine = MedicineItemLoader(item=MedicineItem(), selector=item)
            medicine.add_css("name", "::text")
            link = item.css("::attr(href)").get()
            yield response.follow(
                link, self.parse_medicine, meta={"medicine": medicine}
            )

    def parse_medicine(self, response):

        medicine_loader = response.meta["medicine"]
        usage = response.css("div.monograph-content p").getall()
        if usage:
            medicine_loader.add_value("usage", usage)
        else:
            self.logger.warning(f"No usage found for {response.url}")

        yield medicine_loader.load_item()
