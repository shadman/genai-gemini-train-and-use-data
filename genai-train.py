import requests
import csv
from bs4 import BeautifulSoup

def scrape_article_data(urls):
    articles_data = []  # empty list

    for url in urls:
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the title of the article
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.text
        else:
            title = 'N/A'

        # Extract text from all paragraphs within the main article content
        paragraphs = soup.find_all('div', attrs={'data-component': 'text-block', 'class': 'sc-43e6b7ba-0 bWSguZ'})

        # If news source is BCC:
        '''
        paragraphs = soup.find_all('div', attrs={'data-component': 'text-block', 'class': 'sc-43e6b7ba-0 bWSguZ'})
        '''
        #If News source is CNN, replace 'paragraphs' by using code below:
        '''
        paragraphs = soup.find_all('div', class_=lambda x: x and 'article' in x)
        '''
        #If News source is CNBC, replace 'paragraphs' by using code below:
        '''
        paragraphs = soup.find_all('div', class_ = 'group')
        '''


        content = []
        for div in paragraphs:
            content.extend([p.text for p in div.find_all('p')])

        content = '\n'.join(content)

        articles_data.append({'URL': url, 'Title': title, 'Content': content})

    return articles_data



# List of URLs
urls = [
    'https://www.bbc.com/news/articles/c0vveg0x594o',
    'https://www.bbc.com/news/articles/cn00e8dzq46o',
    'https://www.bbc.com/news/articles/cv2gx7d0qwdo',
    'https://www.bbc.com/news/articles/cp66xljl5p2o',
    'https://www.bbc.com/news/articles/cnllvxwpr0eo',
    'https://www.bbc.com/news/articles/cjkk7d52yvvo',
    'https://www.bbc.com/news/articles/czrrz4e33eno',
    'https://www.bbc.com/news/articles/c511pyn3xw3o',
    'https://www.bbc.com/news/articles/c6pp596y2q1o',
    'https://www.bbc.com/news/articles/cv22e75g4n4o',
    'https://www.bbc.com/news/articles/cz440j1x4xno',
    'https://www.bbc.com/news/articles/cp008qzzee1o',
    'https://www.bbc.com/news/articles/cqll89j98zko',
]

# Scrape article data
articles_data = scrape_article_data(urls)

# Define the CSV file path
csv_file_path = './us_elections.csv'

# Write scraped data to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['URL', 'Title', 'Content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write each row of scraped data
    writer.writerows(articles_data)

print("Scraped data has been written to", csv_file_path)

