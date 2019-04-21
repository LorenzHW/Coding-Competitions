def palindromes(N, Q, str, L_Rs):
  number_or_palindromes = 0
  for l_r in L_Rs:
    l = l_r[0] - 1
    r = l_r[1]
    number_or_palindromes += is_palindrome(str[l:r])
  return number_or_palindromes


def is_palindrome(str):
  chars = {}
  for c in str:
    chars[c] = (chars.get(c, 0) + 1) % 2

  if (len(str) % 2) == 0:
    # even number of chars --> all chars in dict must appear in pairs
    str_is_palindrome = all(True if v == 0 else False for k, v in chars.items())
    return str_is_palindrome
  else:
    # odd number of chars --> one char may appear only once
    counter = 0
    for k, v in chars.items():
      if v == 1:
        counter += 1

      if counter == 2:
        return False
    return True

number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N, Q = input().split()
    N = int(N)
    Q = int(Q)

    str_inp = input()
    L_Rs = []
    for _ in range(Q):
      l, r = input().split()
      l = int(l)
      r = int(r)
      L_Rs.append((l, r))
    result = palindromes(N, Q, str_inp, L_Rs)
    print("Case #{}: {}".format(i, result))

if __name__ == "__main__":
  N = 7
  Q = 5
  input_str = "ABAACCA"
  L_Rs = [(3, 6), (4, 4), (2, 5), (6, 7), (3, 7)]
  print(palindromes(N, Q, input_str, L_Rs))
