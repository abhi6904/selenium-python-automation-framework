import pytest
import softest
from pages.yatra_launch_page import Launcpage
from utilies.utils import utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlightAndFilter(softest.TestCase):
    log = utils.Custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Launcpage(self.driver)
        self.ut = utils()

    # @data(("New Delhi", "BLR", "28/12/2023", "1 Stop"), ("BOM", "DEL", "29/12/2023", "2 Stop"))
    # @file_data("..//testdata/testdata.json")
    # @file_data("..//testdata/testdadayml.yaml")
    # @data(*utils.read_data_xlsx("C:\\Users\\Abhishek\\Desktop\\selenium\\pythonProject\\TestFrameDemo\\testdata\\testdataxl.xlsx","Sheet1"))
    @data(*utils.read_data_from_csv("C:\\Users\\Abhishek\\Desktop\\selenium\\pythonProject\\TestFrameDemo\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flight_and_filter_1_stop(self, goingfrom , goingto, date, stops):
        search_flight_results=self.lp.search_flights(goingfrom, goingto, date)
        self.lp.page_scroll()
        search_flight_results.filter_flight_by_stop(stops)
        allstop = search_flight_results.get_search_flight_result()
        self.log.info(allstop)
        self.ut.assertlistitemtext(allstop, stops)

