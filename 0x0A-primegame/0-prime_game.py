#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    def sieve(n):
        """Returns a list of primes up to n"""
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]

    def game_winner(n):
        """Determine the winner for a single game with number range 1 to n"""
        if n < 2:
            return "Ben"

        primes = sieve(n)
        prime_set = set(primes)

        turn = 0  # 0 for Maria, 1 for Ben

        while prime_set:
            current_prime = min(prime_set)
            multiples = set(range(current_prime, n + 1, current_prime))
            prime_set -= multiples
            turn = 1 - turn

        return "Ben" if turn == 0 else "Maria"

    maria_wins, ben_wins = 0, 0

    for n in nums:
        winner = game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
