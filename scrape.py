from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

base_url = "https://www.wunderground.com/history/monthly/br/bel%C3%A9m/SBBE/date/"

# we are only trying this for one year
years = list(range(1999,2000))
months = list(range(1,13))

list_of_dates = []
for year in years:
  for month in months:
    date = F"{year}-{month}"
    print(date)
    list_of_dates.append(date)





# Set up options for the Chrome webdriver
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# Set up the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)


for date in list_of_dates:
    temp_url = base_url + date
    # Navigate to the web page you want to scrape
    driver.get(temp_url)

    # Get the page source and pass it to Beautiful Soup for parsing


    sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")


    table_div = soup.find_all(class_="summary-table")


    # Do your scraping here...
    print(table_div)

    table_for_df = table_div[0].find("table")

    df = pd.read_html(str(table_for_df))[0]

    print(df.head())

    temp_path = F'weather_data/data-{date}.csv'
    df.to_csv(temp_path,index=False)