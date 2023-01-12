def is_palindrome(word):
  # A szót visszafelé írjuk és összehasonlítjuk az eredetivel
  return word == word[::-1]

# Példa használat
print(is_palindrome("racecar"))  # kiírja: True
print(is_palindrome("hello"))  # kiírja: False
