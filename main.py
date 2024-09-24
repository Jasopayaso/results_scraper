#!/usr/bin/env python3
import logging
from bs4 import BeautifulSoup

from datetime import datetime
from logger import log_info
from requests import get_results_data
def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    log_info('STARTING JOB:', datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

    #number that goes into link
    number = 1 
    log_info('GETTING RESULT PAGE:' , number)

    '''
    create a function that can increment the number and see if it matches the most
    current season if it does increment again (till it reaches the season?)
    would need base season to be up to date as well as be the base case
    '''

    #html and beautiful soup for results
    result_html = get_results_data(number, 30)
    result_soup = BeautifulSoup(result_html, 'html.parser')

    
    

if __name__ == "__main__":
    main()