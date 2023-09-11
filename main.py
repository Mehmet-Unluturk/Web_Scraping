
from bs4 import BeautifulSoup
import requests

base_url = 'https://dergipark.org.tr'
page_number = 1  
max_pages = 5  

with open('dergipark_files.txt', 'w', encoding='utf-8') as file:
    while page_number <= max_pages:
        
        url = f'https://dergipark.org.tr/tr/search/{page_number}?section=journal'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')

        
        magazines = soup.find_all('div', class_='card kt-mb-20 journal-card dp-card-outline')

        
        for magazine in magazines:
            magazine_name = magazine.find('h5', class_='card-title').text
            badge_element = magazine.find('div', class_='year-badge')
            issues_per_year_element = magazine.find('div', class_='col-6 text-left')
            views_and_downloads_element = magazine.find('div', class_='col-6 text-right')

            
            badge = badge_element.text.strip() if badge_element else "Veri Yok"
            issues_per_year = issues_per_year_element.text.replace(' ', '') if issues_per_year_element else "Veri Yok"
            views_and_downloads = views_and_downloads_element.text if views_and_downloads_element else "Veri Yok"

            print(magazine_name)
            print(badge)
            print(issues_per_year)
            print(views_and_downloads)
            print("--------------------------")

            file.write(f'Magazine_Name: {magazine_name}\n\n')
            file.write(f'Badge: {badge}\n\n')
            file.write(f'İssues_Per_Year: {issues_per_year}\n\n')
            file.write(f'Views_And_Downloads: {views_and_downloads}\n\n')
            file.write("--------------------------\n\n")

        page_number += 1

print("Data saved to file: dergipark_files.txt")




