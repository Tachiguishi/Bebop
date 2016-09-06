# Uses python2

def election(candidates):
    #if type(candidates) != 'list':
    #    return;

    winner = candidates[0]
    vote   = 0

    for candidate in candidates:
        if winner == candidate:
            vote += 1
        else:
            vote -= 1
        if 0 == vote:
            winner = candidate
            vote = 1

    return winner

def isMajority(candidates, winner):
    counter = 0
    for candidate in candidates:
        if winner == candidate:
            counter += 1
    if counter > len(candidates)/2.0:
        return True
    else:
        return False

def get_majority_element(a):
    candidate = election(a)
    if isMajority(a, candidate):
        print candidate
    else:
        print 0

input = raw_input();
a = list(map(int, input.split()))
get_majority_element(a)
