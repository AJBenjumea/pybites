def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    chars = list(string)
    if n > 0:
      swap = list(string[:n])
      result = chars[n:]
      result.extend(swap)
    else:
      swap = list(string[n:])
      res = chars[:n]
      swap.extend(res)
      return ''.join(swap)
    return ''.join(result)

   

print(rotate('hello', -2))










