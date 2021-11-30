# The tutorial is here: https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


YOUTUBE_TRENDING_URL = \
'https://www.youtube.com/feed/trending'

# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome('./chromedriver')







if __name__ == "__main__":
    driver.get(YOUTUBE_TRENDING_URL)
    print('Page title:', driver.title)



# HERE IS THE STANDARD APPROACH W/O SELENIUM:

# response = requests.get(YOUTUBE_TRENDING_URL)
#
# print('Status Code', response.status_code)
#
# # with open('trending.html', 'w') as f:
# #     f.write(response.text)
#
# doc = BeautifulSoup(response.text, 'html.parser')
#
# print('Page title:', doc.title.text)
#
# # Find all the video divs
# video_divs = doc.find_all('div', class_='ytd-video-renderer')
# print(f'Found {len(video_divs)} videos')
