from selenium import webdriver
import xlsxwriter

lista_initiala = []
lista_date = []


driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")

driver.get("https://www.bnr.ro/files/xml/nbrfxrates2019.htm")

data = driver.find_element_by_id("Data_table").text.split("\n")

lista_date = [data[i:i+33]
              for i in range(0, len(data), 33)]


with xlsxwriter.Workbook('test_bnr.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(lista_date):
        worksheet.write_row(row_num, 0, data)


driver.quit()
