from operator import itemgetter

def small_straight(dice):
    """Score the given roll in the 'small straight' yatzy category.
    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,5,5])
    0

    It also handles sets and unsorted lists
    >>> small_straight({1,2,3,4,5})
    15
    >>> small_straight([1,2,3,5,4])
    15
    """
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return sum(dice)
    return 0

def chance(dice):
    """Score the given role in the 'Chance' yatzy category

    >>> chance([5,5,5,5,5])
    25
    >>> chance([1,2,3,4,5])
    15
    """
    return sum(dice)

def scores_in_categories(dice, categories=(small_straight, chance)):
    """Score the dice in each category, with the hightest scoring cateogry first.

    >>> scores = scores_in_categories([1,1,2,2,2],
    ... (small_straight, chance)) #doctest +ELLIPSIS
    >>> [(score, category.__name__) for (score, category) in scores]
    [(8, 'chance'), (0, 'small_straight')]
    """
    scores=[(category(dice), category)
        for category in categories]
    return sorted(scores, reverse=True, key=itemgetter(0))
