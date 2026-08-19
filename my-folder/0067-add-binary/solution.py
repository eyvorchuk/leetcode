class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_list = list(a)
        b_list = list(b)
        len_a = len(a_list)
        len_b = len(b_list)
        if len_a > len_b:
            diff = len_a - len_b
            for i in range(diff):
                b_list.insert(0, "0")
        else:
            diff = len_b - len_a
            for i in range(diff):
                a_list.insert(0, "0")
        length = len(a_list)
        bin_sum = []
        carry = False
        for i in range(length):
            index = -1*(i+1)
            if carry:
                if a_list[index] == b_list[index] == "1":
                    bin_sum.insert(0, "1")
                elif a_list[index] == b_list[index] == "0":
                    carry = False
                    bin_sum.insert(0, "1")
                else:
                    bin_sum.insert(0, "0")
            else:
                if a_list[index] == b_list[index] == "1":
                    carry = True
                    bin_sum.insert(0, "0")
                else:
                    bin_sum.insert(0, str(int(a_list[index]) + int(b_list[index])))
        if carry:
            bin_sum.insert(0, "1")
        return "".join(bin_sum)
