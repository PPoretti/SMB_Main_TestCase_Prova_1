from selenium.webdriver.common.by import By

class SbSigInLocator(object):
    USER = (By.NAME, "usernameUserInput")
    PASSWORD = (By.NAME, "password")
    CONTINUEBUTTON = (By.CSS_SELECTOR, ".primary")

class SbMainPageLocator(object):
    ROLEBOX = (By.CSS_SELECTOR, ".mr-6")
    LANG_SELECTOR = (By.CSS_SELECTOR,".ma-4:nth-child(7) > .v-btn__content")
    LANG_LIST = (By.CSS_SELECTOR, ".ma-4:nth-child(7)")
    FLAG_GB = (By.CSS_SELECTOR, ".f-gb")
    FLAG_PT = (By.CSS_SELECTOR, ".f-pt")

class SbPatientPageLocator(object):
    PATMENU = (By.CSS_SELECTOR,"div:nth-child(3) > .v-list-item--link > .v-list-item__content")
    PATSERCH4ID = (By.ID, "searchPatientById")
    PATNUM4PAGEMENU = (By.CSS_SELECTOR, ".mdi-menu-down")
    SHOWPATBYID = [By.ID, "showPatient_"]
    PATMEDHISTORY = (By.CSS_SELECTOR, ".mx-2 > .v-btn__content")

class SbPatData(object):
    BIRTHDATE = (By.ID, "birthDate")
    AGEGROUP  = (By.ID, "ageGroup")
    FALLS = (By.ID, "falls")
    PHYEXAHEIGHT = (By.ID, "height")
    GENHEARINGLOSS = (By.ID, "hearingLoss")

    GENHEARINGAID = (By.ID, "hearingAid") ## PP
    GENCOGNITIVEISSUE = (By.ID, "cognitiveIssue") ## PP
    GENWEIGHTLOSS = (By.ID, "weightLoss") ## PP
    GENDEPRESSIONDISORDER = (By.ID, "depressionDisorder") ## PP
    GENANXIETYDISORDER = (By.ID, "anxietyDisorder") ## PP
    GENCARDIOVASCULARDISEASE = (By.ID, "cardiovascularDisease") ## PP
    GENHISTORYSUBSTANCEABUSE = (By.ID, "historySubstanceAbuse") ## PP
    GENHISTORYBRAININJURY = (By.ID, "historyBrainInjury") ## PP

    GENDIABETES   = (By.ID, "diabetes")
    DRINKINGUNITS = (By.ID, "drinkingUnits")
    SUPINEDIASTOLIC = (By.ID, "supineDiastolic")
    COGNITIVE_DISORDER_MENU = (By.CSS_SELECTOR, ".v-tab:nth-child(7)")
    DEXTERITY_EDIT = (By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/"
                                "div/div/div/div/div[4]/div/div[4]/button/div[1]/div[2]/button[1]")
    DEXTERITY_NEXT = (By.XPATH, "/html/body/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/button")
    DEXTERITY_FULL_USE_OF = (By.XPATH, "/html/body/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]"
                                       "/div/form/div/div/div/div/div/div[1]")

    DEXTERITY_HELP_FOR_MOST_TASK = (By.XPATH, "/html/body/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/form/div/div/div/div/div/div[5]")
    DEXTERITY_CLOSE_BUTTON = (By.XPATH, "/html/body/div/div[3]/div/div/header/div/div[3]/button/span")
    HEARINGLOSS_MENU = (By.CSS_SELECTOR, ".v-tabs:nth-child(2) .v-tab:nth-child(3)")

    HEARINGLOSS_noiseExposure = (By.ID, "noiseExposure")
    HEARINGLOSS_pureToneAudiometry = (By.ID, "pureToneAudiometry")

    MOCA_EDIT = (By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[4]"
                           "/div/div[6]/button/div[1]/div[2]/button[1]")
    MOCA_NEXT = (By.XPATH,"/html/body/div/div[4]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/button")

    MOCA_NAMED_LION = (By.XPATH, "/html/body/div/div[4]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/form/div/div[8]/div/div[2]/div/div/div/div[2]")
    MOCA_ORIENTATION_ALL_CORRECT = (By.XPATH,"/html/body/div/div[4]/div/div/div/div/div/div/div[2]/div[2]/div[2]"
                                             "/div/form/div/div[28]/div/div[2]/div/div/div/div[1]")
    MOCA_CLOSE_BUTTON = (By.XPATH, "/html/body/div/div[4]/div/div/header/div/div[3]/button/span")

    CARDIO_VASCULAR_MENU = (By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[5]")
    CARDIOVASCULAR_numberOfNonScheduledVisit  = (By.ID, "numberOfNonScheduledVisit")
    CARDIOVASCULAR_usualPhysicalActivity = (By.ID, "usualPhysicalActivity")
    CARDIOVASCULAR_heartRateObs = (By.ID, "heartRateObs")
    CARDIOVASCULAR_standingSystolicObs = (By.ID, "standingSystolicObs")
    CARDIOVASCULAR_hypertension = (By.ID, "hypertension")
    CARDIOVASCULAR_heartFailurePreserved = (By.ID, "heartFailurePreserved")
    CARDIOVASCULAR_prInterval = (By.ID, "prInterval")
    CARDIOVASCULAR_qtcInterval = (By.ID, "qtcInterval")
    CARDIOVASCULAR_hdlCholesterol = (By.ID, "hdlCholesterol")
    CARDIOVASCULAR_ldlCholesterol = (By.ID, "ldlCholesterol")

    MEDICAL_HISTORY_MENU = (By.XPATH,"/html/body/div/div[1]/main/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]")
    DIET_SUPPLEMENT_EDIT = (By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/"
                                      "div[2]/div/div/div/div[2]/table/tbody/tr/td[5]/div[2]/button[1]/span")