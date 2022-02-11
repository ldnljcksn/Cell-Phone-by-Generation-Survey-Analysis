import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('results.csv')

members_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0,
                   2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

responses_by_year = {1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 1997: 0, 1998: 0, 1999: 0, 2000: 0,
                     2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0}

for i, each_response in data.iterrows():
    if each_response.birth_year in members_by_year:
        responses_by_year[each_response.birth_year] += 1
        if int(each_response.first_cell_year) - int(each_response.birth_year) < 13:
            if each_response.was_smartphone == 'No':
                members_by_year[each_response.birth_year] += 1

print(members_by_year)

# with plt.xkcd():
fig = plt.figure()
plt.bar(members_by_year.keys(), members_by_year.values())
plt.show()
