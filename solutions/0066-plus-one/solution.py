class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)):
            index = -1*(i+1)
            digits[index] = (digits[index] + 1) % 10
            carry = digits[index] == 0
            if not carry:
                break
        if carry:
            digits.insert(0, 1)
        return digits
