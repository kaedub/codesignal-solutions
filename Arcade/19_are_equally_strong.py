#
# if your left is as strong as one of your friends'
#    and
# if your weakest are is as weak as one of your friends'
#   then true
#   
# else false

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft == friendsLeft or yourLeft == friendsRight:
        return yourRight == friendsLeft or yourRight == friendsRight
    return False