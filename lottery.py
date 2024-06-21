import requests
import random
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://lotostats.ro/arhiva-tabel-loto-6-49-ro'

# Send request to fetch the page contents
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html5lib')

tables = soup.find_all('table', attrs= {'class': 'table table-striped dataTable no-footer example2-content', 'style': 'table-layout: fixed;'})

data = []

for table in tables:
    for row in table.find_all('tr', class_ = 'arhvatbel_brdbtt'):

        cols = row.find_all('td')
        if cols:
            date = cols[0].get_text(strip= True)
            numbers = [int(col.get_text(strip= True)) for col in cols[1:50] if col.get_text(strip= True)] #the last if statement to avoid empty cells

            data.append([date] + numbers)


df = pd.DataFrame(data, columns= ['Date'] + [f"Num_{i}" for i in range(1,7)])
#print(df)

# Save to CSV
df.to_csv("loto_polonia_history.csv", index=False)
# Load the historical data
df = pd.read_csv("loto_polonia_history.csv")

# Calculate the frequency of each number
frequency = df.iloc[:, 1:].stack().value_counts().reset_index()
frequency.columns = ['Number', 'Frequency']
#print(frequency)


# Identify the most and least frequent numbers
most_frequent = frequency.head(10)
least_frequent = frequency.tail(10)

#print(most_frequent)


# Select numbers from most frequent
best_combination = random.sample(most_frequent['Number'].tolist(), 6)


# Print the best combination
print(f"Next combination: {best_combination}")




















#for tags in html.find_all('table', attrs= {'class': 'table table-striped dataTable no-footer example2-content', 'style': 'table-layout: fixed;'}):
'''

data = []
# <div class="col-lg-3 col-md-4 col-sm-6 col-xs-12">
for row in table.find_all('div', class_ = 'col-lg-3 col-md-4 col-sm-6 col-xs-12'):
    info = {}
    panel_heading = row.find('div', class_ = 'panel-heading')
    if panel_heading:
        panel_title = panel_heading.find('span', class_ = 'panel-title')
        if panel_title:
            info['country'] = panel_title.get_text(strip= True)

#<a class="btn btn-primary btn-lg fnt16" href="https://lotostats.ro/rezultate-loto-6-49-ro" role="button">
    panel_body = row.find('div', class_ = 'panel-body')
    if panel_body:
        link_tag = panel_body.find('a', class_ = 'btn btn-primary btn-lg fnt16')
        if link_tag:
            info['link'] = link_tag['href']

    if info:
        data.append(info)


print(data)
    


    x = {}
    x['url'] = row.a['href']
    cols = row.find_all("td")
    date = cols[0].text.strip()
    numbers = [int(col.text.strip()) for col in cols[1:21]]
    data.append([date] + numbers)

    
    # Append the links to the list



df = pd.DataFrame(data, columns=["Date"] + [f"Num_{i}" for i in range(1, 21)])
print(df)

'''


