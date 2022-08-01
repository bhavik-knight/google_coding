def get_ruler(kingdom):
  if kingdom[-1] in "AEIOUaeiou":
    return "Alice"
  elif kingdom[-1] in "Yy":
    return "Nobody"
  else:
    return "Bob"


def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()
