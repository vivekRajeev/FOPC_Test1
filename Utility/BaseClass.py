import inspect
import time

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.login_obj import Login_objects
from TestData.admin_roles import Roles


@pytest.mark.usefixtures("setup")
class Baseclass:
    def getlogger(self):

        loggername=inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler('C:/Users/windows/PycharmProjects/FOPC/Utility/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    def initialization(self):

        logingpage=Login_objects(self.driver)
        admin_role = Roles(self.driver)
        logingpage.sign_in_dashboard().click()
        logingpage.username().send_keys(admin_role.admin_username())
        logingpage.password().send_keys(admin_role.admin_password())
        logingpage.sign_in().click()
        time.sleep(2)
        logingpage.sign_in_dashboard().click()
        time.sleep(8)

        # self.driver.find_element(By.XPATH, "//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline']").click()
        # time.sleep(2)
        # stores = self.driver.find_elements(By.XPATH, f"(//ul[@class='MuiList-root MuiMenu-list MuiList-padding']//li)")
        # for i in range (1,len(stores)):
        #     stores[i].click()
        #     time.sleep(2)
        #     logingpage.sign_in_dashboard().click()
        #     time.sleep(8)
        #     self.driver.find_element(By.XPATH, "(//span[@class='MuiButton-label'])[9]").click()
        #     time.sleep(3)
        #     self.driver.find_element(By.XPATH,"//span[@class='MuiTypography-root MuiListItemText-primary MuiTypography-body1 MuiTypography-displayBlock']").click()
        #     time.sleep(3)
        #     self.driver.find_element(By.XPATH, "(//div[@role='presentation']//div[3]//div)[4]//button[2]").click()

            # logingpage.username().send_keys(admin_role.admin_username())
            # logingpage.password().send_keys(admin_role.admin_password())
            # logingpage.sign_in().click()