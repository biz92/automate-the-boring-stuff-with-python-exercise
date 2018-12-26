print("Enter number")
def collatz(number):
    if number % 2 == 1:
        return 3 * number + 1
    else:
        return number // 2
r = int(input())
while r > 1:
        r = collatz(r)
        print(r)
