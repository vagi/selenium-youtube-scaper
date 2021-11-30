# The tutorial is here: https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test

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

