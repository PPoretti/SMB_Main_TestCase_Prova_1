from locator import *
from selenium.webdriver.common.action_chains import ActionChains
from element import BasePageElement
from locator import SbSigInLocator

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserLocator(BasePageElement):
    locator = SbSigInLocator.USER[1]


class PasswordLocator(BasePageElement):
    locator = SbSigInLocator.PASSWORD[1]

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SbSignIn(BasePage):
    # Declares text input fields
    username = UserLocator()
    password = PasswordLocator()

    def is_title_matches(self):
        return "WSO2 Identity Server" in self.driver.title

    def continue_click(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SbSigInLocator.CONTINUEBUTTON)).click()

    def is_logged(self, role):
        # Verify Login and role is valid
        self.role = role
        return self.driver.find_element(*SbMainPageLocator.ROLEBOX).text == self.role

    def sel_en_language(self):
        # change language setting
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SbMainPageLocator.LANG_SELECTOR)).click()
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SbMainPageLocator.LANG_LIST))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SbMainPageLocator.FLAG_GB)).click()

class SbPatient(BasePage):
    def move_to_patient_page(self):
        # press patient menu item -  mandatory execution for accessin AddPatient and SerchPatient
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SbPatientPageLocator.PATMENU)).click()

    def add_new_patient(self):
        pass

    def search_patient(self, id):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SbPatientPageLocator.PATSERCH4ID)).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SbPatientPageLocator.PATSERCH4ID)).send_keys(id)
        SbPatientPageLocator.SHOWPATBYID[1] = SbPatientPageLocator.SHOWPATBYID[1] + str(id)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SbPatientPageLocator.SHOWPATBYID)).click()

    def show_patient_overview(self, id):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SbPatientPageLocator.PATMEDHISTORY))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

    def check_pat_birthdate(self):
        birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.BIRTHDATE))).get_attribute('value')
        return birthdate

    def check_pat_agegroup(self):
        agegroup = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.AGEGROUP))).get_attribute('value')
        return agegroup

    def check_pat_diabetes(self):
        diabetes = WebDriverWait(self.driver, 20).until(
            #EC.presence_of_element_located((By.XPATH, "//input[@id='" + str(SbPatData.GENDIABETES[1]) + "']/preceding-sibling::div"))).text
            EC.element_to_be_clickable((By.XPATH, "//input[@id='" + str(SbPatData.GENDIABETES[1]) + "']/preceding-sibling::div"))).text
        return diabetes

    def check_pat_balanceDisorder(self):
        balanceDisorder = self.driver.find_element(By.XPATH, "//input[@id='balanceDisorder']/preceding-sibling::span").text
        return balanceDisorder

    def check_pat_hearingloss(self):
        hearingloss = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENHEARINGLOSS))).get_attribute('aria-checked')
        return hearingloss
## PP
    def check_pat_hearingAid(self):
        hearingAid = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENHEARINGAID))).get_attribute('aria-checked')
        return hearingAid
    def check_pat_cognitiveIssue(self):
        cognitiveIssue = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENCOGNITIVEISSUE))).get_attribute('aria-checked')
        return cognitiveIssue
    def check_pat_saltIntake(self):
        saltIntake = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENHEARINGLOSS))).get_attribute('value')
        return saltIntake
    def check_pat_weightLoss(self):
        weightLoss = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENWEIGHTLOSS))).get_attribute('value')
        return weightLoss
    def check_pat_depressionDisorder(self):
        depressionDisorder = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENDEPRESSIONDISORDER))).get_attribute('value')
        return depressionDisorder
    def check_pat_anxietyDisorder(self):
        anxietyDisorder = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENANXIETYDISORDER))).get_attribute('value')
        return anxietyDisorder
    def check_pat_cardiovascularDisease(self):
        cardiovascularDisease = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENCARDIOVASCULARDISEASE))).get_attribute('value')
        return cardiovascularDisease
    def check_pat_historySubstanceAbuse(self):
        historySubstanceAbuse = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENHISTORYSUBSTANCEABUSE))).get_attribute('value')
        return historySubstanceAbuse
    def check_pat_historyBrainInjury(self):
        historyBrainInjury = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.GENHISTORYBRAININJURY))).get_attribute('value')
        return historyBrainInjury

## PP

    def check_pat_falls(self):
        falls = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.FALLS))).get_attribute('value')
        return falls

    def check_pat_drinkingUnits(self):
        drinkingUnits = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.DRINKINGUNITS))).get_attribute('value')
        return drinkingUnits

    def check_pat_height(self):
        height = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.PHYEXAHEIGHT))).get_attribute('value')
        return height

    def check_pat_supineDiastolic(self):
        height = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((SbPatData.PHYEXAHEIGHT))).get_attribute('value')
        return height


#    def check_pat_hearingloss(self):
#        hearingloss = WebDriverWait(self.driver, 20).until(
#            EC.presence_of_element_located((SbPatData.GENHEARINGLOSS))).get_attribute('aria-checked')
#        return hearingloss

#    def check_pat_diabetes(self):
#        diabetes = WebDriverWait(self.driver, 20).until(
#            #EC.presence_of_element_located((By.XPATH, "//input[@id='" + str(SbPatData.GENDIABETES[1]) + "']/preceding-sibling::div"))).text
#            EC.element_to_be_clickable((By.XPATH, "//input[@id='" + str(SbPatData.GENDIABETES[1]) + "']/preceding-sibling::div"))).text
#        return diabetes

#    def check_pat_balanceDisorder(self):
#        balanceDisorder = self.driver.find_element(By.XPATH, "//input[@id='balanceDisorder']/preceding-sibling::span").text
#        return balanceDisorder

#    def check_pat_drinkingUnits(self):
#        drinkingUnits = WebDriverWait(self.driver, 20).until(
#            EC.presence_of_element_located((SbPatData.DRINKINGUNITS))).get_attribute('value')
#        return drinkingUnits
