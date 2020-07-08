def primes_generator(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for idx, _ in enumerate(prime):
        if (prime[idx] is True) and (idx >= 2):
            yield idx
