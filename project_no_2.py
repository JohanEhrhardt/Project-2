# dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from sqlalchemy import create_engine
import time

# table 1

# extract

# setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# define url & visit
url = 'https://www.marketindex.com.au/asx200'
browser.visit(url)
# wait for 5 seconds
time.sleep(5)
# click 'Show All Companies' button
target = 'button[class="btn control-company-display"]'
browser.find_by_tag(target).click()
# wait for 5 seconds
time.sleep(5)
# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
#  retrieve data from table with class 'mi-table', 'mb-4', 'quoteapi-even-items'
table = soup.find('table', class_='mi-table mb-4 quoteapi-even-items')
# define dataframe
asx200_df = pd.DataFrame(columns=['company_code', 'company_name', 'price_29jul22', 'change', 'percent_change', 
                                  'high', 'low', 'volume', 'market_cap', 'one_year_percent_change'])
# collect data
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    if(columns != []):
        company_code = columns[1].text
        company_name = columns[2].span.contents[0]
        price_29jul22 = columns[3].text
        change = columns[4].text
        percent_change = columns[5].text
        high = columns[6].text
        low = columns[7].text
        volume = columns[8].text
        market_cap = columns[9].text
        one_year_percent_change = columns[10].text
        asx200_df = asx200_df.append({'company_code': company_code,  'company_name': company_name, 'price_29jul22': price_29jul22, 
                                      'change': change, 'percent_change': percent_change, 'high': high, 'low':low, 'volume':volume,
                                      'market_cap': market_cap, 'one_year_percent_change': one_year_percent_change }, ignore_index=True)
# end splinter
browser.quit()

# transform

# remove column
transformed_asx200_df = asx200_df[['company_code', 'company_name', 'price_29jul22', 'change','percent_change', 
                                   'one_year_percent_change']].copy()
# drop duplicates
transformed_asx200_df = transformed_asx200_df.drop_duplicates(subset=['company_code'])
# fill na
transformed_asx200_df = transformed_asx200_df.fillna(0)
# remove $ signs
transformed_asx200_df['price_29jul22'] = transformed_asx200_df['price_29jul22'].map(lambda x: x.lstrip('$'))
# change %str to float
transformed_asx200_df['percent_change'] = transformed_asx200_df['percent_change'].str.rstrip('%').astype('float')
transformed_asx200_df['one_year_percent_change'] = transformed_asx200_df['one_year_percent_change'].str.rstrip('%').astype('float')
# change data type
transformed_asx200_df = transformed_asx200_df.astype({'price_29jul22':'float','change':'float'})
# sort by company_code
transformed_asx200_df= transformed_asx200_df.sort_values(by=['company_code'])

# table 2

# extract

# create dataframe from CSV file
asx_company = "companies-list.csv"
asx_company_df = pd.read_csv(asx_company)

# transform

# remove column
transformed_asx_company_df = asx_company_df[['Code', 'Company', 'Market Cap', 'Sector']].copy()
# change column name
transformed_asx_company_df.columns = ['company_code', 'company_name', 'market_cap', 'sector']
# drop duplicates
transformed_asx_company_df = transformed_asx_company_df.drop_duplicates(subset=['company_code'])
# drop na
transformed_asx_company_df = transformed_asx_company_df.dropna(thresh=2)
# remame rows in column "company_code"
transformed_asx_company_df['company_code'] = transformed_asx_company_df['company_code'].map(lambda x: x.lstrip('ASX'))
# remame rows in column "company_code"
transformed_asx_company_df['company_code'] = transformed_asx_company_df['company_code'].map(lambda x: x.lstrip(':'))
# sort by company_code
transformed_asx_company_df = transformed_asx_company_df.sort_values(by=['company_code']).reset_index(drop=True)

# load

# create connection
connection = "postgres:David$1986@localhost:5432/asx_db"
engine = create_engine(f'postgresql://{connection}')
# Confirm tables
engine.table_names()
# # load dataframe
transformed_asx200_df.to_sql(name="asx_200", con=engine, if_exists='append', index=False)
transformed_asx_company_df.to_sql(name="asx_companies", con=engine, if_exists='append', index=False)