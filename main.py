import csv
from selenium import webdriver

driver = webdriver.Chrome("D:\Downloads\chromedriver.exe")

driver.get("https://blocktivity.info")

page_source = driver.page_source

table_rows = driver.find_elements_by_tag_name('tr')
row_data_list = []
for tr in table_rows:
    tds = tr.find_elements_by_tag_name('td')
    row_data_list.append([td.text for td in tds])

with open('scraped_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for row in row_data_list:
        csv_writer.writerow(row)
