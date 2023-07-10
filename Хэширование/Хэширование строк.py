def string_hash(s): #O(n)
    p = 31
    m = 1e9 + 7
    hash_num = 0
    prime_pow = 1
    for char in s:
        hash_num = (hash_num + (hash(char) - hash('a') + 1) * prime_pow) % m
        prime_pow = (prime_pow * p) % m
    return hash_num


def string_hash2():
    s = 'alsnkjdnkejabfaekjfbae'
    hashes = [_ for _ in range(len(s) + 1)]
    hashes[0] = 0
    primes = [_ for _ in range(len(s) + 1)]
    primes[0] = 1
    p = 301
    m = 1e9 + 7
    for i in range(len(s)):
        hashes[i + 1] = hashes[i] * p +(hash(s[i]) - hash('a') + 1)
        hashes[i + 1] %= m
        primes[i + 1] = primes[i] * p
        primes[i + 1] %= m
    i = 3
    j = 7

    substr_hash = (hashes[j + 1] - (hashes[i] * primes[j -i + 1]) % m) % m
    if substr_hash < 0:
        substr_hash += m
    return print(substr_hash)



def test():
    s1 = 'aaa'
    s2 = 'abb'
    s3 = 'abb'

    print(string_hash(s1))
    print(string_hash(s2))
    print(string_hash(s3))
    print(string_hash(s2) == string_hash(s3))

#test()
string_hash2()
