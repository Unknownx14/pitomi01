from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages.scenario01.scenario_01 import DSLCalculator
import unittest #ovo se importuje da bi se napravili testcasevi
import pytest   # za orderovanje koji ce test prvi da se izvrsi
from utilities.teststatus import TestStatus   # za koriscenje TestStatus classe za vise od jednog assert-ovanja


class loginTests(unittest.TestCase): # u zagradu se upusije kad se importuje unittest
    @pytest.mark.run(order=1)
    def test_resultList(self):
        baseurl = "https://www.verivox.de/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
        # driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.execute_script("window.location = 'https://www.verivox.de/';")
        driver.get(baseurl)
        driver.implicitly_wait(5)

        tstatus = TestStatus(driver)   # tstatus je dobio klasu TestStatus iz teststatus.py
        calcDSL = DSLCalculator(driver) #loginpazh je dobio klasu LoginPage iz login_page.py

        sleep(3)
        searchTariffs=calcDSL.DSLResultList('030')

        availableTariffs= calcDSL.verifyCalculatorWorks()
        tstatus.mark(availableTariffs, "For the requested parameters calculator shows available Tariffs")

        calcDSL.scrollDown()

        firstTariff= calcDSL.verifyTariff01()
        tstatus.mark(firstTariff, "First Tariff is present")
        secondTariff = calcDSL.verifyTariff02()
        tstatus.mark(secondTariff, "Second Tariff is present")
        thirdTariff = calcDSL.verifyTariff03()
        tstatus.mark(thirdTariff, "Third Tariff is present")


        calcDSL.scrollDown()

        fourthTariff = calcDSL.verifyTariff04()
        tstatus.mark(fourthTariff, "Fourth Tariff is present")
        fifthTariff = calcDSL.verifyTariff05()
        tstatus.markFinal("test_resultList", fifthTariff, "Fifth Tariff is present")



        # # searchPlace=driver.find_element(By.ID, 'search-courses')
        # # if searchPlace is not None:
        # #     print("Login Successful, Fuck Yeah")
        # # else:
        # #     print("Login has Failed")
        # searchPlace=loginpazh.verifyLoginSuccessful()   # kad se napravi ova metoda verifyLoginSuccessful onda
        # # se ovo iznad ne koristi vise
        # #assert searchPlace == True   # umesto assert se sad koriste metode iz TestStatus classe
        # tstatus.mark(searchPlace,"Login was successful")
        #
        # searchButton= loginpazh.verifySearchButton()
        # #assert searchButton == True   # umesto assert se sad koriste metode iz TestStatus classe
        # tstatus.markFinal("test_validLogin", searchButton, "SearchButton was verified")
        #
        #
        # searchCourse=loginpazh.searchCourse('JavaScript')   # ovo menja ove linije koda ispod
        # # searchPlace.send_keys('JavaScript')
        # # driver.find_element(By.XPATH, '//*[@id="search-course-button"]//i').click()
        # loginpazh.takeScreenShot() # moj kod
        # sleep(5)
        # driver.quit()

    @pytest.mark.run(order=2)
    def test_offerDetail(self):
        baseurl = "https://www.verivox.de/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
        # driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.execute_script("window.location = 'https://www.verivox.de/';")
        driver.get(baseurl)
        driver.implicitly_wait(5)

        tstatus = TestStatus(driver)
        calcDSL = DSLCalculator(driver)

        sleep(3)
        searchTariffs = calcDSL.DSLResultList('030')

        calcDSL.scrollDown()

        firstTariff = calcDSL.verifyTariff01()
        tstatus.mark(firstTariff, "First Tariff is present")


        useGlobalVariable_1 = calcDSL.globNameTariff()   # ovo koristim da pokrenem tu global variable
        useGlobalVariable_2 = calcDSL.globProviderName()
        useGlobalVariable_3 = calcDSL.globPriceTariff()

        enterIn5Min = calcDSL.clickZumAngebot()
        sleep(3)

        In5MinUp= calcDSL.verifyIn5MinUp()
        tstatus.mark(In5MinUp, "In 5 Minuten Online Wechseln is present -up")
        sleep(1)

        h3text= calcDSL.getH3TextCheck()
        tstatus.mark(h3text, 'The right name of a Tariff - present')

        providerName = calcDSL.checkProviderName()
        tstatus.mark(providerName, 'The right name of a Provider - present')

        priceOfTariff = calcDSL.checkPrice()
        tstatus.mark(priceOfTariff, 'The right price of a Tariff - present')

        smallLetters = calcDSL.getSmallLetters()
        tstatus.mark(smallLetters, 'Durchschnittspreis Monat - present')

        calcDSL.scrollDownHalfPage()
        In5MinDown = calcDSL.verifyIn5MinDown()
        tstatus.markFinal("test_offerDetail", In5MinDown, "In 5 Minuten Online Wechseln is present -down")
    #
    @pytest.mark.run(order=3)
    def test_lazyLoading(self):
        baseurl = "https://www.verivox.de/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dusan\\Desktop\\Udemy\\Drivers\\chromedriver.exe")
        # driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.execute_script("window.location = 'https://www.verivox.de/';")
        driver.get(baseurl)
        driver.implicitly_wait(5)

        tstatus = TestStatus(driver)  # tstatus je dobio klasu TestStatus iz teststatus.py
        calcDSL = DSLCalculator(driver)  # loginpazh je dobio klasu LoginPage iz login_page.py

        sleep(3)
        searchTariffs = calcDSL.DSLResultList('030')

        availableTariffs = calcDSL.verifyCalculatorWorks()
        tstatus.mark(availableTariffs, "For the requested parameters calculator shows available Tariffs")

        moreTariffs= calcDSL.clickMoreTariffs()
        sleep(1)

        noMoreTariffs= calcDSL.verify20MoreTariffs()
        tstatus.markFinal("test_lazyLoading", noMoreTariffs, "All Tariffs are loaded")






    #
    #     loginpazh.takeScreenShot() # moj kod
    #     sleep(3)
    #     searchPlace = loginpazh.verifyLoginFailed()
    #     assert searchPlace == True
    #
    #     loginpazh.takeScreenShot() # moj kod
    #     sleep(3)
    #     driver.quit()


        # DelBoy vise ne treba kad se importuje unittest
# DelBoy= loginTests()
# DelBoy.test_validLogin()