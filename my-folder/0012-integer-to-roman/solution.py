class Solution:
    def intToRoman(self, num: int) -> str:
        def digitToRoman(digit, first, mid, last):
            if digit == "4":
                return first + mid
            elif digit == "9":
                return first + last
            else:
                roman_digit = ""
                if int(digit) >= 5:
                    roman_digit = mid
                remainder = int(digit) % 5
                roman_digit += first * remainder
                return roman_digit

        str_num = str(num)
        roman = ""
        for i in range(len(str_num)):
            digit = str_num[-1*(i+1)]
            if i == 0:
                roman_digit = digitToRoman(digit, "I", "V", "X")
            elif i == 1:
                roman_digit = digitToRoman(digit, "X", "L", "C")
            elif i == 2:
                roman_digit = digitToRoman(digit, "C", "D", "M")
            else:
                roman_digit = "M" * (int(digit) % 5)
            roman = roman_digit + roman
        return roman
