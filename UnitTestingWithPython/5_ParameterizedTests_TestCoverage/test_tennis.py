import pytest

from tennis import score_tennis

@pytest.mark.parametrize('player1_points, player2_points, expected_score',
    [(0, 0, 'Love-All'),
     (1, 1, 'Fifteen-All'),
     (2, 2, 'Thirty-All')
     ])
def test_score_tennis(player1_points, player2_points, expected_score):
    assert score_tennis(player1_points, player2_points) == expected_score

# example using unittest
# def test_score_tennis(self):
#     test_cases = [
#         (0, 0, 'Love-All'),
#         (1, 1, 'Fifteen-All')
#     ]
#     for player1_points, player2_points, expected_score in test_cases:
#         with self.subTest(f'{player1_points}, {player2_points}, {expected_score}'):
#             self.assertEqual(expected_score, score_tennis(player1_points, player2_points))