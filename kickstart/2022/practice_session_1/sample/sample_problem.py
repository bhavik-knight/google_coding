T = int(input().strip())

for test in range(1, T + 1):
    N, M = [int(e) for e in input().strip().split()]
    C = [int(e) for e in input().strip().split()]

    total_candy = sum(C)
    print(f"Case #{test}: {total_candy % M}")
