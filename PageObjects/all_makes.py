from selenium.webdriver.common.by import By


class Makes:
    def __init__(self,driver):
        self.driver = driver

    ref = (By.XPATH,"(//span[@class='MuiButton-label'])[37]")
    mak = (By.XPATH,"(//span[@class='MuiButton-label'])[41]")
    manufactures = (By.XPATH,"//div[@col-id='manufacturer']")
    store_name = (By.XPATH,"(//h6[contains(@class,'MuiTypography-root jss')])[2]")
    make_datas = (By.XPATH,"//div[@col-id='validMakes']")
    make_filter = (By.XPATH,"(//span[@class='ag-icon ag-icon-filter'])[3]")
    make_name = (By.XPATH,"//label[@class='ag-set-filter-item']")
    exclude_make = (By.XPATH,"(//span[@class='MuiTab-wrapper'])[2]")
    name_send = (By.XPATH,"(//input[@class='ag-input-field-input ag-text-field-input'])[3]")
    reset = (By.XPATH,"(//span[@class='MuiButton-label'])[66]")
    grid = (By.XPATH,"//div[@class='ag-virtual-list-viewport ag-filter-virtual-list-viewport ag-focus-managed']")
    rowdatas = (By.XPATH,"//label[@class='ag-set-filter-item']")
    filtersel = (By.XPATH,"//span[@class='ag-tab ag-tab-selected']")
    ex_manufact = (By.XPATH,"//div[@col-id='manufacturer']")
    ex_make = (By.XPATH, "//div[@col-id='excludedMakes']")


    def reference(self):
        return self.driver.find_element(*Makes.ref)

    def makes(self):
        return self.driver.find_element(*Makes.mak)

    def manufact(self):
        return self.driver.find_elements(*Makes.manufactures)

    def store_names(self):
        return self.driver.find_element(*Makes.store_name)

    def makedatas(self):
        return self.driver.find_elements(*Makes.make_datas)

    def makefilter(self):
        return self.driver.find_element(*Makes.make_filter)

    def makename(self):
        return self.driver.find_element(*Makes.make_name)

    def excludemake(self):
        return self.driver.find_element(*Makes.exclude_make)

    def namesend(self):
        return self.driver.find_element(*Makes.name_send)

    def reset_layout(self):
        return self.driver.find_element(*Makes.reset)

    def ag_grid(self):
        return self.driver.find_element(*Makes.grid)

    def row_data(self):
        return self.driver.find_elements(*Makes.rowdatas)

    def fil_sel(self):
        return self.driver.find_element(*Makes.filtersel)

    def ex_manufac(self):
        return self.driver.find_elements(*Makes.ex_manufact)

    def ex_makes(self):
        return self.driver.find_elements(*Makes.ex_make)



