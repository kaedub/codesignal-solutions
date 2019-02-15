def get_bad_pair(s):
   for i in range(len(s)-1):
      if s[i] >= s[i+1]:
         return i
   return -1

def almostIncreasingSequence(sequence):
   s = sequence
   j = get_bad_pair(s)
   if j == -1:
      return True
   if get_bad_pair(s[j-1:j] + s[j+1:]) == -1:
      return True
   if get_bad_pair(s[j:j+1] + s[j+2:]) == -1:
      return True
   return False