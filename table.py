from selenium.webdriver.common.by import By

class WebTable:
    def __init__(self, webtable):
       self.table = webtable

    def get_row_count(self):
        # return len(self.table.find_elements_by_tag_name("tr")) - 1
        return len(self.table.find_element(By.NAME, ("tr"))) - 1

    def get_column_count(self):
        # return len(self.table.find_elements_by_xpath("//tr[2]/td"))
        return len(self.table.find_element(By.XPATH, ("//tr[2]/td")))


    def get_table_size(self):
        return {"rows": self.get_row_count(),
                "columns": self.get_column_count()}

    def presence_of_data(self, data):

        # verify the data by getting the size of the element matches based on the text/data passed
        # dataSize = len(self.table.find_elements_by_xpath("//td[normalize-space(text())='" + data + "']"))
        dataSize = len(self.table.find_element(By.XPATH, ("//td[normalize-space(text())='" + data + "']")))
        presence = False
        if (dataSize > 0):
            presence = True
        return presence

    def find_row(self, patId):
        # get number of rows
        noOfRows = len(self.table.find_elements_by_xpath("//tr")) - 1
        # noOfRows = len(self.table.find_element(By.XPATH, ("//tr"))) - 1

        # get number of columns
        if noOfRows <= 2:
            noOfColumns = len(self.table.find_elements_by_xpath('//tr[1]/td'))
            #noOfColumns = len(self.table.find_element(By.XPATH, ('//tr[1]/td')))
        else:
            # noOfColumns = len(self.table.find_elements_by_xpath("//tr[2]/td"))
            noOfColumns = len(self.table.find_element(By.XPATH, ("//tr[2]/td")))

        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(1, noOfRows+1):
            # reset the row data every time
            # iterate over columns
            for j in range(1, noOfColumns):
                cmd = "//tr[" + str(i) + "]/td[" + str(j) + "]"
                # cellData = self.table.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text
                cellData = self.table.find_element(By.XPATH, ("//tr[" + str(i) + "]/td[" + str(j) + "]")).text
                if cellData == patId:
                    break
                return i
        return None