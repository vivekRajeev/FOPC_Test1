from selenium.webdriver.common.by import By


class Login_objects:

    def __init__(self, driver):
        self.driver = driver

    sign_in_dash = (By.CSS_SELECTOR, '#login')
    user = (By.CSS_SELECTOR, '#username')
    pwd = (By.CSS_SELECTOR, '#password')
    submit = (By.CSS_SELECTOR, '#kc-login')

    def sign_in_dashboard(self):
        return self.driver.find_element(*Login_objects.sign_in_dash)

    def username(self):
        return self.driver.find_element(*Login_objects.user)

    def password(self):
        return self.driver.find_element(*Login_objects.pwd)

    def sign_in(self):
        return self.driver.find_element(*Login_objects.submit)

