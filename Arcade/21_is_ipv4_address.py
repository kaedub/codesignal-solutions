#
# Split string by '.',
# if string is length 4 and if each item is in range 0-255
#   true
# false

def isIPv4Address(inputString):
    s = inputString.split('.')
    [n for n in s if int(n) >= 0 and int(n) <]

