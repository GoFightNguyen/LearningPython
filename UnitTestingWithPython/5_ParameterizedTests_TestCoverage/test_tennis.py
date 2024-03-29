import pytest

from tennis import score_tennis

@pytest.mark.parametrize('player1_points, player2_points, expected_score',
    [(0, 0, 'Love-All'),
     (1, 1, 'Fifteen-All'),
     (2, 2, 'Thirty-All'),
     (2, 1, 'Thirty-Fifteen'),
     (3, 1, 'Forty-Fifteen'),
     (4, 1, 'Win for Player 1'),
     (4, 3, 'Advantage Player 1'),
     (3, 4, 'Advantage Player 2') # take this line out to see a branch not covered
     ])
def test_score_tennis(player1_points, player2_points, expected_score):
    assert score_tennis(player1_points, player2_points) == expected_score

# to get coverage using pytest
# pytest --cov-report html:directory --cov-branch --cov=tennis .

# example using unittest
# def test_score_tennis(self):
#     test_cases = [
#         (0, 0, 'Love-All'),
#         (1, 1, 'Fifteen-All')
#     ]
#     for player1_points, player2_points, expected_score in test_cases:
#         with self.subTest(f'{player1_points}, {player2_points}, {expected_score}'):
#             self.assertEqual(expected_score, score_tennis(player1_points, player2_points))