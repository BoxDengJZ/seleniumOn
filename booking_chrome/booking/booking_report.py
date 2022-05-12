from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class BookingReport:
    def __init__(self, box_section_element: WebElement):
        self.box_section_element = box_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.box_section_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_deal_box_info(self):
        # print(len(self.deal_boxes))
        result_collection = []
        for box in self.deal_boxes:
            # pulling hotel name
            nameDiv = box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]')
            hotelName = nameDiv.get_attribute('innerHTML').strip()
            priceDiv = box.find_element(By.CSS_SELECTOR, 'div[data-testid="price-and-discounted-price"]')
            hotelPrice = priceDiv.find_element(By.TAG_NAME, "span").get_attribute('innerHTML').strip()
            starDiv = box.find_element(By.CSS_SELECTOR, 'div[data-testid="rating-stars"]')
            stars = starDiv.find_elements(By.TAG_NAME, "span")
            scoreDiv = box.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]')
            score = scoreDiv.find_element(By.CSS_SELECTOR, 'div[aria-label*="评"]').get_attribute('innerHTML').strip()

            # print(f'{hotelName} ,  {hotelPrice},  {len(stars)}  星级,   评分  f{score}')
            result_collection.append([hotelName, hotelPrice, score, f'{len(stars)}  星级'])
        return result_collection
