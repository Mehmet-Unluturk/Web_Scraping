from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = 'https://dergipark.org.tr'
page_number = 1
max_pages = 5


df = pd.DataFrame(columns=["Magazine_Name", "Badge", "Issues_Per_Year", "Views_and_Downloads"])

while page_number <= max_pages:
    url = f'https://dergipark.org.tr/tr/search/{page_number}?section=journal'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    magazines = soup.find_all('div', class_='card kt-mb-20 journal-card dp-card-outline')

    data_to_append = []

    for magazine in magazines:
        magazine_name = magazine.find('h5', class_='card-title').text
        badge_element = magazine.find('div', class_='year-badge')
        issues_per_year_element = magazine.find('div', class_='col-6 text-left')
        views_and_downloads_element = magazine.find('div', class_='col-6 text-right')

        badge = badge_element.text.strip() if badge_element else "Veri Yok"
        issues_per_year = issues_per_year_element.text.replace(' ', '') if issues_per_year_element else "Veri Yok"
        views_and_downloads = views_and_downloads_element.text if views_and_downloads_element else "Veri Yok"

        data_to_append.append([magazine_name, badge, issues_per_year, views_and_downloads])

    
    df = pd.concat([df, pd.DataFrame(data_to_append, columns=df.columns)], ignore_index=True)

    page_number += 1


df.to_excel("dergipark_data.xlsx", index=False)

print("Data saved to Excel file: dergipark_data.xlsx")
