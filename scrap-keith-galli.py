from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# Load the page
url = "https://keithgalli.github.io/web-scraping/webpage.html"
page = requests.get(url)
# print(page)
# print(page.status_code)

# Convert to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

# Grab all the social links from the webpage (in at least three different ways)
# First way: using select
social_links = soup.select('a') # All the links on the page
socials = soup.select('ul.socials a')
print(socials)
links = [link['href'] for link in socials]
print(links)
for link in socials:
    print(link['href'])
print(social_links)

# Second way: using find_all
ulist = soup.find('ul', attrs={'class': 'socials'})
links = ulist.find_all('a')
print(socials)
actual_links = [link['href'] for link in links]
print(actual_links)
for link in actual_links:
    print(link)

# Third way: using select and find
links = soup.select('li.social a')
print(links)
actual_links = [link['href'] for link in links]
print(actual_links)
for link in links:
    print(link)

# Grab the table
table = soup.select('table.hockey-stats')[0]
# print(table)
columns = table.find('thead').find_all('th')
column_names = [c.string for c in columns]
# print(column_names)

rows = table.find('tbody').find_all('tr')
rows_data = []
for tr in rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    rows_data.append(row)
print(rows_data[0])

# Create a DataFrame from the table data
df = pd.DataFrame(rows_data, columns=column_names)
"""print(df.head())
print(df[['S', 'Team', 'League']])
print(df.loc[df['Team'] != 'Did not play'])
print(df.loc[df['Team'] != 'Did not play'].sum())"""

# Save the DataFrame to a CSV file
"""df.to_csv('hockey_stats.csv', index=False)"""

# Grab all the fun facts that use the word is
# My way
fun_facts = soup.select('ul.fun-facts li')
print([fact.text for fact in fun_facts if 'is' in fact.text.lower()])

# Video's way
facts = soup.select('ul.fun-facts li')
facts_with_is = [fact.find(string=re.compile('is')) for fact in facts]
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]    # Filter out None values
print(facts_with_is)

# Download an image
images = soup.select('div.row div.column img')
# print(images)
for image in images:
    print(image['src'])
image_url = images[0]['src']

base_url = url.rsplit('/', 1)[0]  # Remove 'webpage.html'
print(base_url)
full_url = base_url + '/' + image_url
print(f'Full URL: {full_url}')

img_data = requests.get(full_url).content
with open(images[0]['alt'] + '.jpg', 'wb') as handler:
    handler.write(img_data)

# Find the secret word
files = soup.select('div.block a')
relative_files = [f['href'] for f in files]
print(relative_files)
base_url = url.rsplit('/', 1)[0] + '/'    # Remove 'webpage.html'
print(base_url)

for f in relative_files:
    full_url = base_url + f
    page = requests.get(full_url)
    bs_page = BeautifulSoup(page.content, 'html.parser')
    print(bs_page.body.prettify())
    secret_word_element = bs_page.find('p', attrs={"id": "secret-word"})
    secret_word = secret_word_element.string
    print(secret_word)