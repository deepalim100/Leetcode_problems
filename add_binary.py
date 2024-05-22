

class solution():
    def add_bin(self, num1, num2):
        num1 = int(num1, 2)
        num2 = int(num2, 2)

        s = num1 + num2
        print(bin(s))
        print('binary :', bin(s)[2:])
        return 0
    

if __name__ == '__main__':
    n1, n2 = "11" , "1"
    res = solution().add_bin(n1, n2)