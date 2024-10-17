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
    #every game starts with the class match-fixture
    result_body = result_soup.find_all(class_ = 'match-fixture', limit= None)
    # log_info('RESULT BODY: {}'.format(result_body))
    #gets the length of the result_body which should be the same as the amount of games in that season
    count = len(result_body)

    #iterates over the match-fixture that holds the info about the game
    for teams in result_body:
        #finds all the teams names in result_body
        
        team_names = teams.find_all('span', class_ = 'match-fixture__short-name')
        team_names_text = [team.get_text() for team in team_names]
        
       #gets the respective teams names from the text array
        home_team = team_names_text[0]
        away_team = team_names_text[1]

        #finds the scores for the respective team
        team_scores = teams.find_all('span', class_ = 'match-fixture__score')
        team_scores_text = [score.get_text() for score in team_scores]
        home_score = team_scores_text[0][0]
        away_score = team_scores_text[0][2]
        
        #compares the scores to see who won
        if int(home_score) > int(away_score):
            winner = home_team
        elif int(home_score) < int(away_score):
            winner = away_team
        else: 
            winner = 'DRAW'
        log_info('{} {}-{} {}. Winner: {}'.format(home_team, home_score, away_score, away_team, winner))

        game_id = teams['data-comp-match-item']

        log_info('GAME ID: {}'.format(game_id))
    
    
    log_info('TOTAL AMOUNT OF GAMES: {}'.format(count))
 
 
    #test comment

if __name__ == "__main__":
    main()