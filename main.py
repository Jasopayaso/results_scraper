#!/usr/bin/env python3
import logging
import sys
from bs4 import BeautifulSoup

from datetime import datetime
from logger import log_info
from requests import get_results_data
def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    log_info('STARTING JOB:', datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

    #number that goes into link
    number = 719
    log_info('GETTING RESULT PAGE:' , number)

    '''
    create a function that can increment the number and see if it matches the most
    current season if it does increment again (till it reaches the season?)
    would need base season to be up to date as well as be the base case
    '''

    #html and beautiful soup for results
    result_html = get_results_data(number, 15)
    result_soup = BeautifulSoup(result_html, 'html.parser')
    result_body = result_soup.find(class_ = 'match-fixture')
    result_body_text = result_body.text

    result = [word for word in result_body_text.split() if word]
    home_team = result[0]
    home_score = result[2][0]
    away_team = result[3]
    away_score = result[2][2]

    log_info('RESULT BODY: {}'.format(result_body_text))
    log_info('RESULT: {}'.format(result))
    log_info('HOME TEAM: {}'.format(home_team))
    log_info('AWAY TEAM: {}'.format(away_team))
    log_info('HOME SCORE: {}'.format(home_score))
    log_info('AWAY SCORE: {}'.format(away_score))
 
    

if __name__ == "__main__":
    main()