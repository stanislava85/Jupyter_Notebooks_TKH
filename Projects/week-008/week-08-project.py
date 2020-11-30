import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

def CovidData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find('tbody').findAll('tr')[2:235]
    th_td_list = []
    for row in rows:
        th = row.findAll('th')[1]
        tds = row.findAll('td')[:-1]
        th_td_data_row = []
        th_td_data_row.append(th.text.strip().split('[')[0])
        for td in tds:
            td_text = td.text.strip()
            td_text = ''.join(td_text.split(','))
            if td_text == 'No data' or td_text=='?':
                td_text = None
            elif '.' in td_text:
                count_digits = len(td_text) - td_text.index('.') - 1
                td_text = int(''.join('9.492'.split('.'))) / 10 ** count_digits
            else:
                td_text = int(td_text)
            th_td_data_row.append(td_text)
        th_td_list.append(th_td_data_row)
    for row_list in th_td_list[:-1]:
        if row_list[2] != None and row_list[1] != None:
            death_rate = float("%.3f" % (row_list[2] / row_list[1]))
        else:
            death_rate = None
        if row_list[3] != None and row_list[1] != None:
            recovery_rate = float("%.3f" % (row_list[3] / row_list[1]))
        else:
            recovery_rate = None
        row_list.append(death_rate)
        row_list.append(recovery_rate)
    return th_td_list

# CovidData(url)

def data_to_csv(url):
    with open("stanislava-covid-report-from-py.csv", "w") as csvfile:
        file = csv.writer(csvfile)
        file.writerow(["Country","Cases","Deaths","Recoveries","Death Rate","Recovery Rate"])
        file.writerows(CovidData(url))
        
#data_to_csv(url)


if __name__ == '__main__':
    CovidData(url)
    data_to_csv(url)
 
    