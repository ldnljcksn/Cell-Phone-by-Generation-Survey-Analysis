import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('results.csv')

millennials_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0,
                       2000: 0, 2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

zoomers_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0,
                   2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

other_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0,
                 2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

total_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0,
                 2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

for i, each_response in data.iterrows():
    if each_response.birth_year in total_by_year:
        total_by_year[each_response.birth_year] += 1
        if each_response.generation == 'Millennial':
            millennials_by_year[each_response.birth_year] += 1
        elif each_response.generation == 'Gen Z':
            zoomers_by_year[each_response.birth_year] += 1
        else:
            other_by_year[each_response.birth_year] += 1

millennial_percents = []
zoomer_percents = []
other_percents = []
for each_item in millennials_by_year:
    millennial_percents.append(float(millennials_by_year[each_item]) / float(total_by_year[each_item]))
for each_item in zoomers_by_year:
    zoomer_percents.append(float(zoomers_by_year[each_item]) / float(total_by_year[each_item]))
for each_item in other_by_year:
    other_percents.append(float(other_by_year[each_item]) / float(total_by_year[each_item]))

millennial_percents = np.array(millennial_percents)
zoomer_percents = np.array(zoomer_percents)
other_percents = np.array(other_percents)

plt.style.use('fivethirtyeight')
years = range(1990, 2009, 1)
N = 19
ind = np.arange(N)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])
ax.set_xticks(years)
plt.xticks(rotation=45)
plt.bar(millennials_by_year.keys(), millennial_percents, color='blue', label='Millennials')
plt.bar(other_by_year.keys(), other_percents, bottom=millennial_percents, color='orange', label='Other')
plt.bar(zoomers_by_year.keys(), zoomer_percents, bottom=millennial_percents+other_percents, color='green',
        label='Gen Z')
plt.legend(loc='best')
plt.title('Self-identified generation percents by birth year')
plt.show()
