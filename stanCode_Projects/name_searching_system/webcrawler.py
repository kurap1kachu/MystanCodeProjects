"""
File: webcrawler.py
Name: Jerry Yu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        # code is under <table> class="t-stripe"
        tags = soup.find_all("table", {"class": "t-stripe"})
        # number of male
        m_num = 0
        # number of female
        f_num = 0
        lst = []
        for tag in tags:
            # getting every variables in tbody using .text
            info = tag.tbody.text.split()
            lst += info
            # cleaning the lst by taking the index of ele from 0 to 1000
            lst = lst[0:1000]
            for i in range(2, 1001, 5):
                # turning str to float, by replacing the "," in num, in order to count
                num = float(lst[i].replace(",", ""))
                m_num += num
            for i in range(4, 1001, 5):
                num = float(lst[i].replace(",", ""))
                f_num += num
            print(f"Male Number: {int(m_num)}")
            print(f"Female Number: {int(f_num)}")


if __name__ == '__main__':
    main()
