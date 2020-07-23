from time import sleep
from base.selenium_driver import SeleniumDriver





class DSLCalculator(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver_=driver


    # Locators
    _login_link = "//div[@id='navbar']//a[@class='navbar-link fedora-navbar-link']"
    _email_field = "user_email"
    _password_filed = "user_password"
    _login_button = 'commit'
    _search_course = 'search-courses'
    _course_1= '//div[@title="JavaScript Masterclass"]'
    _course_2= '//div[@title="JavaScript for beginners"]'
    _desired_course = '//div[@title="JavaScript for beginners"]'
    _enroll_button = "enroll-button-top"
    _creditcard_number = '//*[@id="root"]//input[@name="cardnumber"]'
    _creditcard_expdate = '//*[@id="root"]//input[@name="exp-date"]'
    _creditcard_cvc = '//*[@id="root"]//input[@name="cvc"]'
    _agree_terms = 'agreed_to_terms_checkbox'
    _postal_code= '//*[@id="root"]//input[@name="postal"]'
    _purchase_button= "confirm-purchase"
    _another_Frame_1 = "__privateStripeFrame16"
    _another_Frame_2 = "__privateStripeFrame17"
    _another_Frame_3 = "__privateStripeFrame18"
    _another_Frame_4 = "__privateStripeFrame19"
    _invalid_creditcard= '//div[@id="new_card"]//div[contains(text(), "The card number is not a valid credit card number.")]'


    def clickLoginLink(self):
        self.clickElement(self._login_link, locatorType='xpath')
        sleep(14)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_filed)

    def clickLoginButton(self):
        self.clickElement(self._login_button, locatorType='name')


    def login(self, username, password): #Ovde je prerbaceno iz MOJ testcase loginlink, username, userpass, loginbutton
        # loginLink = self.driver_.find_element(By.XPATH, "//div[@id='navbar']//a[@class='navbar-link fedora-navbar-link']")
        # loginLink.click()
        self.clickLoginLink()

        self.enterEmail(username)

        self.enterPassword(password)
        sleep(1)

        self.clickLoginButton()


    def verifyLoginSuccessful(self):
        result = self.isElementPresent('search-courses')
        return  result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='alert alert-danger']", 'xpath')
        return  result


    def searchCourse(self, courseName):   # ovo sam se ja igrao
        result= self.sendKeys(courseName, self._search_course)
        sleep(3)
        self.clickElement('//*[@id="search-course-button"]//i', 'xpath')

    def verifySearchButton(self):   # ovo sam se ja igrao
        result = self.isElementPresent('//*[@id="search-course-button"]//i', 'xpath')
        return result

    def takeScreenShot(self):   # ovo se ja igram
        self.screenShot(resultMessage="ScreenShot")

    def selectCourse(self):
        result = self.clickElement(self._desired_course, 'xpath')

    def clickEnroll(self):
        result = self.clickElement(self._enroll_button)

    def switchFrame1(self):
        result= self.switchToFrame(self._another_Frame_1, 'name')

    def switchFrame2(self):
        result= self.switchToFrame(self._another_Frame_2, 'name')

    def switchFrame3(self):
        result = self.switchToFrame(self._another_Frame_3, 'name')

    def switchFrame4(self):
        result = self.switchToFrame(self._another_Frame_4, 'name')

    def defaultIFrame(self):
        result = self.returnDefaultFrame()


    def creditCardCredentials(self, cardNumber, cardExpdate, cardCvcNum, postalCode):
        anotherFrame1 = self.switchFrame1()
        cardNum= self.sendKeys(cardNumber, self._creditcard_number, 'xpath' )
        defIFrame = self.defaultIFrame()
        anotherFrame2 = self.switchFrame2()
        cardExp= self.sendKeys(cardExpdate, self._creditcard_expdate, 'xpath')
        defIFrame= self.defaultIFrame()
        anotherFrame2 = self.switchFrame3()
        cardCvc= self.sendKeys(cardCvcNum, self._creditcard_cvc, 'xpath')
        defIFrame = self.defaultIFrame()
        anotherFrame2 = self.switchFrame4()
        cardCvc = self.sendKeys(postalCode, self._postal_code, 'xpath')
        defIFrame = self.defaultIFrame()
        checkTermsAndPolicy= self.agreeTermsAndPolicy()
        purchaseButton = self.clickElement(self._purchase_button)

    def verifyDemandedCourses(self):
        course1=self.isElementPresent(self._course_1, 'xpath')
        course2 = self.isElementPresent(self._course_2, 'xpath')
        return course1, course2

    def invalidCreditcardMessage(self):
        result = self.isElementPresent(self._invalid_creditcard, 'xpath')
        return result

    def agreeTermsAndPolicy(self):
        result = self.clickElement(self._agree_terms)

    def verifyEnrollCannotbeDone(self):
        result = self.isEnabled(locator=self._purchase_button, locatorType='id',
                                info="Enroll Button is disabled "
                                            "since all the required fields are not completed")
        return not result

    def creditCardCredentialsWithoutPurchase(self, cardNumber, cardExpdate, cardCvcNum, postalCode):
        anotherFrame1 = self.switchFrame1()
        cardNum= self.sendKeys(cardNumber, self._creditcard_number, 'xpath' )
        defIFrame = self.defaultIFrame()
        anotherFrame2 = self.switchFrame2()
        cardExp= self.sendKeys(cardExpdate, self._creditcard_expdate, 'xpath')
        defIFrame= self.defaultIFrame()
        anotherFrame2 = self.switchFrame3()
        cardCvc= self.sendKeys(cardCvcNum, self._creditcard_cvc, 'xpath')
        defIFrame = self.defaultIFrame()
        anotherFrame2 = self.switchFrame4()
        cardCvc = self.sendKeys(postalCode, self._postal_code, 'xpath')
        defIFrame = self.defaultIFrame()
        checkTermsAndPolicy= self.agreeTermsAndPolicy()


########## Odavde krecem da pravim svoje metode #########

    # Locators
    _dsl = '//label[@id="mps-label-5"]//span[@class="mps-label-text"]'
    _ihre_vorvahl = '//*[@id="mps-tab-box-5"]/form/div[2]/div[1]/input[1]'
    #_ihre_vorvahl = "90934b1d-prefix"
    _mbit_16 = '//*[@id="mps-tab-box-5"]/form/div[2]/div[2]/label[1]'
    #_mbit_16 = "90934b1d-calc-dsl-option-1"
    _jetzt_vergleichen= '//*[@id="mps-tab-box-5"]/form/div[2]/button'
    _tarifempfehlung = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[1]'
    _01Tariff = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[3]'
    _02Tariff = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[4]'
    _03Tariff = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[5]'
    _04Tariff = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[6]'
    _05Tariff = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[7]'
    _zum_angebot = "/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[3]//a[contains(text(), 'Zum Angebot')]"
    _in_funf_minuten_up = '//*[@id="sticky-wrapper"]//a'
    _in_funf_minuten_down = '//*[@id="verivoxBroadbandCalculatorContent"]/div[1]/div/div[1]/offer-summary-page-bottom/div/div[2]/a'
    #_h3_header = '//*[@id="verivoxBroadbandCalculatorContent"]//h3[text()="Magenta Zuhause M Young"]'
    _h3_heading = '//*[@id="verivoxBroadbandCalculatorContent"]/div[1]/div/div[1]/offer-tariff-info/div/h3'
    _small_letters = '//*[@id="sticky-wrapper"]//small'
    _please_work = 'Durchschnittspreis/Monat'
    '                    '
    _x_weiteretarifeladen = '//button[@class="btn btn-primary text-uppercase"]'
    _name_ofTariff = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[3]/div/app-tariff/div[1]/div/div[1]/div/div[3]/app-tariff-provider/div/div[2]/div[2]'
    _name_ofProviderGlobal = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[3]/div/app-tariff/div[1]/div/div[1]/div/div[3]/app-tariff-provider/div/div[2]/strong'
    _name_ofProvider = '//*[@id="verivoxBroadbandCalculatorContent"]/div[1]/div/div[1]/offer-tariff-info/div/div/div[1]/div[2]/strong'
    _price_firstPage = '/html/body/div[3]/main/div/vx-telco-broadband/div/app-tariff-list/div/div[2]/div[2]/div[3]/div/app-tariff/div[1]/div/div[2]/div[2]/div[2]/app-tariff-price/div/div[1]/strong'
    _price_secondPage = '//*[@id="sticky-wrapper"]/div/div/div[1]/div[1]/div'

    _gas = '//*[@id="mps-label-3"]//span[@class="mps-label-text"]'
    _gas_something = '//*[@id="mps-tab-box-3"]/form/div[2]/div[1]/input[1]'






    def clickDSL(self):
        self.clickElement(self._dsl, locatorType='xpath')
        sleep(3)

    def enterPrefix(self, prefix):
        self.sendKeys(prefix, self._ihre_vorvahl, locatorType='xpath')
        sleep(1)

    def selectBandwidth(self):
        self.clickElement(self._mbit_16, locatorType='xpath')

    def clickJetztVerg(self):
        self.clickElement(self._jetzt_vergleichen, locatorType='xpath')

    def DSLResultList(self, prefix):
        self.clickDSL()
        self.enterPrefix(prefix)
        self.selectBandwidth()
        self.clickJetztVerg()
        sleep(10)

    def verifyCalculatorWorks(self):
        result = self.isElementPresent(self._tarifempfehlung, locatorType='xpath')
        return result

    def verifyTariff01(self):
        result = self.isElementPresent(self._01Tariff, locatorType='xpath')
        return result
    def verifyTariff02(self):
        result = self.isElementPresent(self._02Tariff, locatorType='xpath')
        return result
    def verifyTariff03(self):
        result = self.isElementPresent(self._03Tariff, locatorType='xpath')
        return result
    def verifyTariff04(self):
        result = self.isElementPresent(self._04Tariff, locatorType='xpath')
        return result
    def verifyTariff05(self):
        result = self.isElementPresent(self._05Tariff, locatorType='xpath')
        return result


    def clickZumAngebot(self):
        self.clickElement(self._zum_angebot, locatorType='xpath')

    def verifyIn5MinUp(self):
        result = self.isElementPresent(self._in_funf_minuten_up, locatorType='xpath')
        return result

    def verifyIn5MinDown(self):
        result = self.isElementPresent(self._in_funf_minuten_down, locatorType='xpath')
        return result

    def getH3Text(self):
        result = self.getElement(self._h3_header, locatorType='xpath').text
        if 'Magenta Zuhause M Young' in result:
            return True
        else:
            return False

    def getSmallLetters(self):
        result = self.getElement(self._small_letters, locatorType='xpath').text
        if self._please_work in result:
            return True
        else:
            return False

    def loadMoreTariffs(self):
        self.scrollDownFullPage()
        result = self.isElementPresent(self._x_weiteretarifeladen, locatorType='xpath')
        return result


    def clickMoreTariffs(self):
        abcde= self.loadMoreTariffs()
        self.takeScreenShot()
        while abcde == True:
            self.clickElement(self._x_weiteretarifeladen, locatorType='xpath')
            sleep(3)
            abcde= self.loadMoreTariffs()
            self.takeScreenShot()
            sleep(3)
        else:
            self.takeScreenShot()

    def verify20MoreTariffs(self):
        result = self.isElementPresent(self._x_weiteretarifeladen, locatorType='xpath')
        return not result

    def globNameTariff(self):   # pokusaj da uvezem elemente sa prve stranice - pravim global variablu
        global tariffName
        tariffName = self.getElement(self._name_ofTariff, locatorType='xpath').text

    def getH3TextCheck(self):   # pokusaj da uvezem elemente sa prve na drugu stranicu - metod za chekiranje global variable
        result = self.getElement(self._h3_heading, locatorType='xpath').text
        if tariffName in result:
            return True
        else:
            return False

    def globProviderName(self):
        global providerName
        providerName = self.getElement(self._name_ofProviderGlobal, locatorType='xpath').text

    def checkProviderName(self):
        result = self.getElement(self._name_ofProvider, locatorType='xpath').text
        if providerName in result:
            return True
        else:
            return False

    def globPriceTariff(self):
        global priceTariff
        priceTariff = self.getElement(self._price_firstPage, locatorType='xpath').text

    def checkPrice(self):
        result = self.getElement(self._price_secondPage, locatorType='xpath').text
        if priceTariff in result:
            return True
        else:
            return False

    ##### Zbog Unpack CSV
    def clickGas(self):
        self.clickElement(self._gas, locatorType='xpath')
        sleep(3)

    def enterSomething(self, slova):
        self.sendKeys(slova, self._gas_something, locatorType='xpath')
        sleep(1)

    def Gasnesto(self, slova):
        self.clickGas()
        self.enterSomething(slova)
        sleep(3)
    #####



