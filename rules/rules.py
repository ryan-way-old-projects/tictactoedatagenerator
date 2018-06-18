class Rules:

    ALLMOVES = [1,2,3,4,5,6,7,8,9]

    def PossibleMoves(self, movesMade):
        return list(set(self.ALLMOVES) - set(movesMade))