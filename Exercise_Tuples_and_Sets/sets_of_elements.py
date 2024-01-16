n, m = input().split()

n_set = set(input() for _ in range(int(n)))
m_set = set(input() for _ in range(int(m)))

print(*(n_set & m_set), sep="\n")



