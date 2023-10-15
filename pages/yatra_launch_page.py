import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base.base_driver import basedriver
from pages.search_flight_result_page import search_flightresult
from utilies.utils import utils


class Launcpage(basedriver):
    log = utils.Custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver1 = driver

    # locators
    DEPART_FROM_FIELD="//input[@id='BE_flight_origin_city']"
    GOING_TO_FEILD ='//input[@id="BE_flight_arrival_city"]'
    GOING_TO_RESUT_LIST ="//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD="//input[@id='BE_flight_origin_date']"
    ALL_DATES="//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON ="BE_flight_flsearch_btn"

    def getdeparfield(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def goingtolocation(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FEILD)

    def goingtoresult(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESUT_LIST)

    def departuredate(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getalldate(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)


    def searchbutton(self):
        return self.driver.find_element(By.ID, self.SEARCH_BUTTON)



    def enterdepartlocation(self,departlocation):
        self.getdeparfield().click()
        self.getdeparfield().send_keys(departlocation)
        self.getdeparfield().send_keys(Keys.ENTER)

    def entergoingtolocation(self, goingto):
        self.goingtolocation().click()
        self.log.info("Clicked on going to")
        self.goingtolocation().send_keys(goingto)
        self.log.info("Typed text in going to field")
        search_result= self.goingtoresult()
        for result in search_result:
            if goingto in result.text:
                result.click()
                break


    def enterdepartdate(self,departuredate):
        self.departuredate().click()
        all_dates= self.getalldate().find_elements(By.XPATH,self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break


    def clicksearchbutton(self):
        self.searchbutton().click()
        time.sleep(4)



    def search_flights(self, departlocation, goingto, departuredate):
        self.enterdepartlocation(departlocation)
        self.entergoingtolocation(goingto)
        self.enterdepartdate(departuredate)
        self.clicksearchbutton()
        search_flights_results=search_flightresult(self.driver)
        return search_flights_results

