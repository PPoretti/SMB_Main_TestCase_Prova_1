import os
import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  #pp
import page

# Add to PATH location of browser specific driver
# os.environ['PATH'] += r"C:/SeleniumSBtest"

# driver = webdriver.Chrome('C:\\Sviluppo\\SMB_Main_TestCases\\DriversSelenium\\chromedriver.exe')


class Sb_Main_TestCases(unittest.TestCase):
    # reading test data from SB_TestData.ini configuration file
    testdata = configparser.ConfigParser()
    testdata.read("SB_TestData.ini")

    PATID = testdata['Patient_Overview']['smartbearID']
    USERNAME = testdata['Login']['username']
    PASSWORD = testdata['Login']['password']

    #testdata.set('Patient_Overview','email' , 'ado@email.it')

    @classmethod
    def setUpClass(cls):
        # inst.driver = webdriver.Firefox()

        s = Service ("//home//io//Progetti//SMB_Main_TestCase_Prova_2//DriversSelenium//chromedriver")
#        s = Service("C:\\Sviluppo\\SMB_Main_TestCases\\DriversSelenium\\chromedriver.exe")  # pp
        cls.driver = webdriver.Chrome(service=s)  # pp
        #cls.driver = webdriver.Chrome() #pp
        cls.driver.implicitly_wait(13)
        cls.driver.maximize_window()
        cls.driver.get("https://cloudtest.smart-bear.eu/")

    def test_sigIn(self):
        sbsignin = page.SbSignIn(self.driver)
        sbsignin.username = self.USERNAME
        sbsignin.password = self.PASSWORD

        assert sbsignin.is_title_matches()
        sbsignin.continue_click()
        sbsignin.sel_en_language()
        assert sbsignin.is_logged("CCM")

    def test_MoveToPatientPage(self):
        sbpatientpage = page.SbPatient(self.driver)
        sbpatientpage.move_to_patient_page()

    def test_search_patient(self):
        sbpatientpage = page.SbPatient(self.driver)
        sbpatientpage.search_patient(self.PATID)

    def test_show_patient_overview(self):
        sbpatientpage = page.SbPatient(self.driver)
        sbpatientpage.show_patient_overview(self.PATID)

    def test_patient_data(self):
        sbpatientpage = page.SbPatient(self.driver)
        self.assertEqual(sbpatientpage.check_pat_birthdate(),self.testdata['Patient_Overview']['birthdate'],
                         "Patient_Overview -> birthdate value NOT correct") ##
        self.assertEqual(sbpatientpage.check_pat_agegroup(),self.testdata['Patient_Overview']['agegroup'],
                         "Patient_Overview -> birthdate value NOT correct") ##
        self.assertEqual(sbpatientpage.check_pat_diabetes(), self.testdata['Medical_History_General_Info']['diabetes'],
                         "Medical_History_General_Info -> diabetes value NOT correct") ##
        self.assertEqual(sbpatientpage.check_pat_balanceDisorder(),self.testdata['Medical_History_General_Info']['balanceDisorder'],
                         "Medical_History_General_Info -> balanceDisorder value NOT correct") ##
        self.assertEqual(sbpatientpage.check_pat_hearingloss(), self.testdata['Medical_History_General_Info']['hearingLoss'],
                         "Medical_History_General_Info -> hearingLoss' value NOT correct") ##

## PP
        input("hearingAid - beg -")
        self.assertEqual(sbpatientpage.check_pat_hearingAid(), self.testdata['Medical_History_General_Info']['hearingAid'],
                         "Medical_History_General_Info -> hearingAid value NOT correct")
        input("hearingAid - end -")

        input("cognitiveIssue - beg -")
        self.assertEqual(sbpatientpage.check_pat_cognitiveIssue(), self.testdata['Medical_History_General_Info']['cognitiveIssue'],
                         "Medical_History_General_Info -> cognitiveIssue value NOT correct")
        input("cognitiveIssue - end -")

        input("weightLoss - beg -")
        self.assertEqual(sbpatientpage.check_pat_weightLoss(), self.testdata['Medical_History_General_Info']['weightLoss'],
                         "Medical_History_General_Info -> weightLoss value NOT correct")
        input("weightLoss - end -")

        input("depressionDisorder - beg -")
        self.assertEqual(sbpatientpage.check_pat_depressionDisorder(), self.testdata['Medical_History_General_Info']['depressionDisorder'],
                         "Medical_History_General_Info -> depressionDisorder value NOT correct")
        input("depressionDisorder - end -")

        input("anxietyDisorder - beg -")
        self.assertEqual(sbpatientpage.check_pat_anxietyDisorder(), self.testdata['Medical_History_General_Info']['anxietyDisorder'],
                     "Medical_History_General_Info -> anxietyDisorder value NOT correct")
        input("anxietyDisorder - end -")

        input("cardiovascularDisease - beg -")
        self.assertEqual(sbpatientpage.check_pat_cardiovascularDisease(), self.testdata['Medical_History_General_Info']['cardiovascularDisease'],
                     "Medical_History_General_Info -> cardiovascularDisease value NOT correct")
        input("cardiovascularDisease - end -")

        input("historySubstanceAbuse - beg -")
        self.assertEqual(sbpatientpage.check_pat_historySubstanceAbuse(), self.testdata['Medical_History_General_Info']['historySubstanceAbuse'],
                     "Medical_History_General_Info -> historySubstanceAbuse value NOT correct")
        input("historySubstanceAbuse - end -")

        input("historyBrainInjury - beg -")
        self.assertEqual(sbpatientpage.check_pat_historyBrainInjury(), self.testdata['Medical_History_General_Info']['historyBrainInjury'],
                     "Medical_History_General_Info -> historyBrainInjury value NOT correct")
        input("historyBrainInjury - end -")


        input("saltIntake - beg -")
        self.assertEqual(sbpatientpage.check_pat_saltIntake(), self.testdata['Medical_History_Life_Habits']['saltIntake'],
                     "Medical_History_Life_Habits -> saltIntake value NOT correct")
        input("saltIntake - end -")

## PP

        self.assertEqual(sbpatientpage.check_pat_falls(), self.testdata['Medical_History_Life_Habits']['falls'],
                     "Medical_History_Life_Habits -> falls over last 12 months value NOT correct") ##
        self.assertEqual(sbpatientpage.check_pat_drinkingUnits(), self.testdata['Medical_History_Life_Habits']['drinkingUnits'],
                     "Medical_History_Life_Habits -> drinkingUnits value NOT correct") ##
        try:
            self.assertEqual(sbpatientpage.check_pat_height(), self.testdata['Medical_History_Physical_Examinations']['height'],
                             "Medical_History_Physical_Examinations -> height value NOT correct") ##
        except AssertionError as msg:
            print(msg)
        input("Premi un tasto per continuare… (09)")
        self.assertEqual(sbpatientpage.check_pat_supineDiastolic(), self.testdata['Medical_History_Physical_Examinations']['supineDiastolic'],
                         "Medical_History_Physical_Examinations -> supineDiastolic value NOT correct")
        input("Premi un tasto per continuare… (10)")

        #sbpatientpage.show_diet_suppllement_edit()
        # # Shows Hearing Loss data by clicking on HL menu item
        sbpatientpage.show_hearing_loss_data()
        self.assertEqual(sbpatientpage.check_hearing_loss_noiseExposure(), self.testdata['Hearing_Loss_General_Info']['noiseExposure'],
                         "Hearing_Loss_General_Info -> noiseExposure value NOT correct")

        self.assertEqual(sbpatientpage.check_hearing_loss_pureToneAudiometry(), self.testdata['Hearing_Loss_General_Info']['pureToneAudiometry'],
                         "Hearing_Loss_General_Info -> pureToneAudiometry value NOT correct")


        # Shows Cardio Vascular data
        sbpatientpage.show_cardio_vascular_data()
        # Chacks some cardio vascular data
        self.assertEqual(sbpatientpage.check_cardio_vascular_numberOfNonScheduledVisit(),
                         self.testdata['Cardiovascular_General_Info']['numberOfNonScheduledVisit'],
                         "Cardiovascular_General_Info -> numberOfNonScheduledVisit value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_usualPhysicalActivity(),
                         self.testdata['Cardiovascular_General_Info']['usualPhysicalActivity'],
                         "Cardiovascular_General_Info -> usualPhysicalActivity value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_heartRateObs(),
                         self.testdata['Cardiovascular_Observations']['heartRateObs'],
                         "Cardiovascular_Observations -> heartRateObs value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_standingSystolicObs(),
                         self.testdata['Cardiovascular_Observations']['standingSystolicObs'],
                         "Cardiovascular_Observations -> standingSystolicObs value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_hypertension(),self.testdata['Cardiovascular_History']['hypertension'],
                         "Cardiovascular_History -> hypertension value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_heartFailurePreserved(), self.testdata['Cardiovascular_History']['heartFailurePreserved'],
                         "Cardiovascular_History -> heartFailurePreserved value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_prInterval(),self.testdata['Cardiovascular_ECG']['prInterval'],
                         "Cardiovascular_ECG-> prInterval value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_qtcInterval(),self.testdata['Cardiovascular_ECG']['qtcInterval'],
                         "Cardiovascular_ECG-> qtcInterval value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_hdlCholesterol(),self.testdata['Cardiovascular_Cholesterol_and_Scores']['hdlCholesterol'],
                         "Cardiovascular_Cholesterol_and_ScoresG-> qtcInterval value NOT correct")
        self.assertEqual(sbpatientpage.check_cardio_vascular_ldlCholesterol(),self.testdata['Cardiovascular_Cholesterol_and_Scores']['ldlCholesterol'],
                         "Cardiovascular_Cholesterol_and_Scores-> ldlCholesterol value NOT correct")

        # back to Medical History data
        sbpatientpage.show_medical_history_data()

        # Shows Dexterity questionanire
        sbpatientpage.show_dexterity()
        # Cheks some Dexterity values
        self.assertEqual(sbpatientpage.check_pat_dexterity_fulluseof(), self.testdata['DEXTERITY']['fulluseof'],
                         "DEXTERITY -> Full use of two hands and ten fingers value NOT correct")

        self.assertEqual(sbpatientpage.check_pat_dexterity_help_for_most_task(), self.testdata['DEXTERITY']['help_for_most_task'],
                         "DEXTERITY -> Limitations in use of hands or fingers, requires the help of another person for most tasks "
                         "(not independent even with use of special tools) value NOT correct")


        # # Closes Dexterity questionnaire
        sbpatientpage.close_dexterity()

        # Shows MOCA questionanire
        sbpatientpage.show_moca()  # # Opens Dexterity questionanre
        # Cheks some Dexterity values
        self.assertEqual(sbpatientpage.check_pat_moca_named_lion(), self.testdata['MOCA']['named_lion'],
                         "MOCA -> Ask patient to name the first animal - Namded Lion value NOT correct")
        self.assertEqual(sbpatientpage.check_pat_moca_orientation_all_correct(), self.testdata['MOCA']['orientation_all_correct'],
                         "MOCA -> Orientation - Ask patient the date, month, year, day, place, and city - All correct value NOT correct")
        # # Closes MOCA questionnaire

        sbpatientpage.close_moca()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    #organizes test suite, ordering tests to be executed
    suite = unittest.TestSuite()
    suite.addTest(Sb_Main_TestCases('test_sigIn'))
    suite.addTest(Sb_Main_TestCases('test_MoveToPatientPage'))
    suite.addTest(Sb_Main_TestCases('test_search_patient'))
    suite.addTest(Sb_Main_TestCases('test_show_patient_overview'))
    suite.addTest(Sb_Main_TestCases('test_patient_data'))
    # suite.addTest(Sb_Main_TestCases(''))

    # run the suite
    input("Premi un tasto per vedere il film")
    unittest.TextTestRunner(verbosity=2).run(suite)

