import csv
from selenium import webdriver

import datetime

current_timestamp = str(datetime.date.today())

driver = webdriver.Chrome("D:\Downloads\chromedriver.exe")

driver.get("https://blocktivity.info")


def scrape_data(rows):
    for tr in rows:
        tds = tr.find_elements_by_tag_name('td')
        row_data_list.append([td.text for td in tds])


row_data_list = []


page_source = driver.page_source

table_rows = driver.find_elements_by_tag_name('tr')
scrape_data(table_rows)

button = driver.find_element_by_class_name('v-data-footer__icons-after')
button.click()

table_rows = driver.find_elements_by_tag_name('tr')
scrape_data(table_rows)


with open(f'scraped_data_{current_timestamp}.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for row in row_data_list:
        csv_writer.writerow(row)
