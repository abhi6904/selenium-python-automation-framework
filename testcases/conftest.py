import os
import time

import pytest
import pytest_html
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions
        driver = webdriver.Edge(options=options)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # Always add a URL to the report
        extras.append(pytest_html.extras.url("http://www.example.com"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Only add additional HTML on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = str(int(round(time.time() * 1000))) + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            # Use the Selenium driver from the request fixture
            driver = item.funcargs.get("request").cls.driver
            driver.save_screenshot(destinationFile)
            if file_name:
                html = f'<div><img src="{file_name}" alt="screenshot" style="width:300px;height:200px" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extras.append(pytest_html.extras.html(html))
        report.extras = extras

def pytest_html_report_title(report):
    report.title = "Abhi academy Automation Report"
