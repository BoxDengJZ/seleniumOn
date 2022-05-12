import time

from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.by import By

import booking.constants as const
from booking.Filtrations import BookingFiltration
from booking.booking_report import BookingReport


class Booking(webdriver.Chrome):
    def __init__(self, gg=True):
        super(Booking, self).__init__()
        # implicit wait ,
        # will allow us to wait some amount of time,
        # until the element is ready on the website
        self.implicitly_wait(15)
        self.maximize_window()
        self.tearDown = gg

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency="USD"):
        btn = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text*="选择你使用的货币"]')
        btn.click()
        # 寻找元素， 包含子串
        # asterisk equal
        selectedA = self.find_element(By.CSS_SELECTOR,
                                      f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selectedA.click()

    def select_to_go(self, place):
        search_field = self.find_element(By.ID, "ss")
        # clear the exsiting text
        search_field.clear()
        search_field.send_keys(place)
        firstResult = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        firstResult.click()

    def select_date(self, checkIn, checkOut):
        check_in = self.find_element(By.CSS_SELECTOR, f'td[data-date="{checkIn}"]')
        check_in.click()
        check_out = self.find_element(By.CSS_SELECTOR, f'td[data-date="{checkOut}"]')
        check_out.click()

    def selectAdults(self, total=3):
        btn = self.find_element(By.ID, "xp__guests__toggle")
        btn.click()
        decrease_btn = self.find_element(By.CSS_SELECTOR, 'button[aria-label="减少成人数量"]')
        add_btn = self.find_element(By.CSS_SELECTOR, 'button[aria-label="增加成人数量"]')
        valContainer = self.find_element(By.ID, "group_adults")
        target = total
        while True:
            #  get_attribute, receives a key name,
            #  then it tries to give back the value of whatever the attribute is
            count = valContainer.get_attribute("value")
            if int(count) == target:
                break
            elif int(count) > target:
                decrease_btn.click()
            else:
                add_btn.click()

    def clickSearch(self):
        searchB = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        searchB.click()

    def apply_filtrations(self):
        filter = BookingFiltration(self)
        self.implicitly_wait(15)
        filter.apply_star_rating(4, 5)
        time.sleep(5)
        filter.sort_by_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element(By.ID, "search_results_table")
        report = BookingReport(hotel_boxes)
        table = PrettyTable(field_names=["Name", "Price", "Score", "Star"])
        table.add_rows(report.pull_deal_box_info())
        print(table)

    # once we have finished everything
    def __exit__(self, exc_type, exc_val, exc_tb):
        # to shut down the chrome browser
        if self.tearDown:
            self.quit()
