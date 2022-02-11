import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv('results.csv')

zillennials_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0,
                       2000: 0, 2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

zoomers_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0,
                   2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

millennials_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0,
                       2000: 0, 2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

weirdos_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0,
                   2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

total_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0,
                 2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

for i, each_response in data.iterrows():
    if each_response.birth_year in total_by_year:
        total_by_year[each_response.birth_year] += 1
        if int(each_response.first_cell_year) - int(each_response.birth_year) < 13:
            if each_response.was_smartphone == 'No':
                zillennials_by_year[each_response.birth_year] += 1
            else:
                zoomers_by_year[each_response.birth_year] += 1
        else:
            if each_response.was_smartphone == 'No':
                millennials_by_year[each_response.birth_year] += 1
            else:
                weirdos_by_year[each_response.birth_year] += 1

zoomer_percents = []
zillennial_percents = []
millennial_percents = []
weirdo_percents = []
for each_item in zoomers_by_year:
    zoomer_percents.append(float(zoomers_by_year[each_item]) / float(total_by_year[each_item]))
for each_item in zillennials_by_year:
    zillennial_percents.append(float(zillennials_by_year[each_item]) / float(total_by_year[each_item]))
for each_item in millennials_by_year:
    millennial_percents.append(float(millennials_by_year[each_item]) / float(total_by_year[each_item]))
for each_item in weirdos_by_year:
    weirdo_percents.append(float(weirdos_by_year[each_item]) / float(total_by_year[each_item]))

zoomer_percents = np.array(zoomer_percents)
zillennial_percents = np.array(zillennial_percents)
millennial_percents = np.array(millennial_percents)
weirdo_percents = np.array(weirdo_percents)

plt.style.use('fivethirtyeight')
years = range(1990, 2009, 1)
N = 19
ind = np.arange(N)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])
ax.set_xticks(years)
plt.xticks(rotation=45)
plt.bar(zoomers_by_year.keys(), zoomer_percents, bottom=millennial_percents+zillennial_percents, color='green',
        label='Zoomers')
plt.bar(zillennials_by_year.keys(), zillennial_percents, bottom=millennial_percents, color='red', label='Zillennials')
plt.bar(millennials_by_year.keys(), millennial_percents, color='blue', label='Millennials')
# plt.bar(weirdos_by_year.keys(), weirdo_percents, bottom=millennial_percents+zillennial_percents+zoomer_percents,
#         color='black', label='Weirdos')
plt.legend(loc='best')
plt.title('Calculated generation percents by birth year')
plt.show()
