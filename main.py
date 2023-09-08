from bs4 import BeautifulSoup
import requests

base_url = 'https://dergipark.org.tr'
page_number = 1  # İlk sayfa
max_pages = 5  # Kaç sayfa taranacak

while page_number <= max_pages:
    
    url = f'https://dergipark.org.tr/tr/search/{page_number}?section=journal'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    
    dergiler = soup.find_all('div', class_='card kt-mb-20 journal-card dp-card-outline')

    
    for dergi in dergiler:
        isim = dergi.find('h5', class_='card-title').text
        badge_element = dergi.find('div', class_='year-badge')
        sayi_element = dergi.find('div', class_='col-6 text-left')
        indir_element = dergi.find('div', class_='col-6 text-right')

        
        badge = badge_element.text.strip() if badge_element else "Veri Yok"
        sayi = sayi_element.text.replace(' ', '') if sayi_element else "Veri Yok"
        indir = indir_element.text if indir_element else "Veri Yok"

        print(isim)
        print(badge)
        print(sayi)
        print(indir)
        print("--------------------------")

    page_number += 1





