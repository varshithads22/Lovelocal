#Hard-3:

#Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.


def count_digit_one(n):
    count = 0

    for i in range(1, n + 1):
        count += str(i).count('1')

    return count


n=int(input("enter a number"))
print(count_digit_one(n))
