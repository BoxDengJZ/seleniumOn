from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    # constructor method
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_vals):
        star_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        for star_val in star_vals:
            star_child = star_box.find_element(By.CSS_SELECTOR, f'div[data-filters-item="class:class={star_val}"]')
            # 感觉， html 上的元素，都可以点击
            star_child.click()

    def sort_by_price_lowest_first(self):
        price_btn = self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')
        price_btn.click()




