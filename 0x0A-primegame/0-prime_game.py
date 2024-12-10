#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_primes_up_to(n):
        return sum(1 for i in range(2, n + 1) if is_prime(i))

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = count_primes_up_to(n)
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# مثال للتشغيل
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
