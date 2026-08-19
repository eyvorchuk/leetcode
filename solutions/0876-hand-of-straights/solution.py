class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        while len(hand) > 0:
            start = hand[0]
            hand.remove(start)
            for i in range(1, groupSize):
                if start+i in hand:
                    hand.remove(start+i)
                else:
                    return False
        return True
