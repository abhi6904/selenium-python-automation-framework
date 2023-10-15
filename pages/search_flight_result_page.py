import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import basedriver
from utilies.utils import utils

class search_flightresult(basedriver):
    log = utils.Custom_logger(logLevel=logging.WARNING)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    filter_by_1_stop = "//p[normalize-space()='1']"
    filter_by_2_stop ="//p[normalize-space()='2']"
    filter_by_non_stop ="//p[normalize-space()='0']"
    search_flight_result= "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"



    def get_search_flight_result(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.search_flight_result)
    def get_filter_by_1_stop(self):
        return self.driver.find_element(By.XPATH, self.filter_by_1_stop)

    def get_filter_by_2_stop(self):
            return self.driver.find_element(By.XPATH, self.filter_by_2_stop)

    def get_filter_by_non_stop(self):
            return self.driver.find_element(By.XPATH, self.filter_by_non_stop)



    def filter_flight_by_stop(self,by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_1_stop().click()
            self.log.warning("Selected flight with 1 stop")


        elif by_stop == "2 Stop":
            self.get_filter_by_2_stop().click()
            self.log.warning("Selected flight with 2 stop")


        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop().click()
            self.log.warning("Selected flight with non stop")

        else:
            self.log.warning("Please provide valid option")


