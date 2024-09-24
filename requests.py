import time


from logger import log_info
from conf import Config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions\


def get_results_data(page_id, sleep):
    """
    Get the results from a given season
    
    :param page_id: The number after se in order to pull the correct results
    :return html: html portion that will be used in beautiful soup
    """

    try:
        result_url = "https://www.premierleague.com/results?co=1&se={}&cl=-1".format(page_id)
    except Exception as e:
        log_info('RESULT URL BROKEN: ', e)
        
    options = ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Remote(command_executor=Config.REMOTE_SELENIUM, options=options)
    driver.get(result_url)

    time.sleep(sleep)

    html = driver.page_source

    driver.quit()

    return html