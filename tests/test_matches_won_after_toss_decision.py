from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from main import read_mock_matches
from ipl_analytics.csv.matches_won_after_toss_decision import matches_won_after_toss_decision


def test_matches_won_after_toss_decision():
    '''test case of matches_won_after_toss_decision() function for matches won after toss decision'''

    expected_output = {2008: {}, 
                    2009: {}, 
                    2010: {}, 
                    2011: {'bat': 1, 'field': 1}, 
                    2015: {'field': 1}, 
                    2016: {'field': 1}, 
                    2017: {'field': 3, 'bat': 2}}

    mock_matches = read_mock_matches()
    output = matches_won_after_toss_decision(mock_matches)

    assert expected_output == output