def test_updateHand():
    """
    Unit test for updateHand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l':1, 'm':1}
    expectedHand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function
    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function
        
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v':1, 'n':1, 'l':1}
    expectedHand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)
        
        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    print("SUCCESS: test_updateHand()")
        
def updateHand(hand, word):
    copy_hand = hand.copy()
    for i in word:
        if i in copy_hand:
            if copy_hand[i]!=0:
                copy_hand[i]-=1
#            else:
#                del copy_hand[str(i)]  
    hand=copy_hand
    return hand

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

test_getWordScore()