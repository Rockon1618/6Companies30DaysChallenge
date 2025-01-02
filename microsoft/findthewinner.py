class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        game = list(range(1, n+1))

        start = 0

        while len(game) > 1: 
            elimination_index = (start + k - 1) % len(game)

            game.pop(elimination_index)

            start = elimination_index

        return game[0]
        