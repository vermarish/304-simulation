import random
##from matplotlib import pyplot as plt
import numpy as np
## import seaborn as sns

## Create constants.
PLAYER_NAMES = ["South", "East", "North", "West"]  
ALL_CARDS = {}
ranks = ["J", "9", "A", "10", "K", "Q", "8", "7"]
suits = ["H", "D", "S", "C"]
values = [30, 20, 11, 10, 3, 2, 0, 0]
ALL_CARDS = {(r,s,values[i]) for i, r in enumerate(ranks) for s in suits}
# del ranks; del suits; del values


## Avoid index hell.

# returns rank of a card 
def rank(card):
    return(card[0])
# returns suit of a card
def suit(card):
    return(card[1])
# returns value of a card/set of cards
def value(cards):
    """
    Input one card and get its value.
    Input a collection of cards and get the TOTAL value.
    """
    if isinstance(cards, tuple):  # single card
        return(cards[2])
    elif isinstance(cards, list):  # list of cards
        return(sum([card[2] for card in cards]))
    else:
        raise Exception("value() expects a single card (tuple) or a list of cards (list).")


class Player:
    """
    A base class for a player.
    Keeps track of cards in the player's hand.
    """

    hand = []   
    name = None
    gs = None
    suitDic = {}   # map suit to an integer count
    handsDic = {}  # map suit to a list of ranks

    def __init__(self):
        self.handsDic = {"H": [], "D": [], "S": [], "C": []}  #dictionary storing all cards of a certain suit
        self.suitDic = {"H": 0, "D": 0, "S": 0, "C": 0}  #dictionary storing distribution of each suit 


    def giveCards(self, cards):
        if isinstance(cards, tuple):
            cards = [cards]
        # Now treat it as a list
        self.hand += cards
        for card in cards:
            self.handsDic[suit(card)].append(rank(card))
            self.suitDic[suit(card)] += 1

    """The player plays a card, moving it from their hand to the table"""
    def playCard(self, card):
        self.hand.remove(card)
        self.handsDic[suit(card)].remove(rank(card))
        self.suitDic[suit(card)] -= 1
        self.gs.table += [card]


    """Remove all cards from a player's hand"""
    def clearHand(self):
        self.hand = []
        self.handsDic = {"H": [], "D": [], "S": [], "C": []}
        self.suitDic = {"H": 0, "D": 0, "S": 0, "C": 0}

    """Set a players hand to the given list of cards"""
    def setHand(self, cards):
        self.clearHand()
        self.giveCards(cards)

    """Count the distribution of the four suits in your hand"""
    def getSuits(self):
        #suitDic = {"H": 0, "D": 0, "S": 0, "C": 0}
        #for s in suits:
        #    suitDic.update({s: len(self.handsDic.get(s))})
        #return(suitDic)
        return(self.suitDic)

    ## Decisions for child classes to make
    ## This parent class makes naive decisions.
    ##
    ## DO NOT WASTE YOUR TIME trying to improve these.
    ## These are just placeholders so that the code can
    ## run without actually implementing each decision.

    def makeBid(self):
        """
        Evaluate the 4 cards in self.hand,
        then make a bid between 160 and 200.
        """
        bid = 160
        self.bidInFirstRound = bid
        return(bid)


    def pickTrump(self):
        """
        Evaluate the 8 cards in self.hand,
        then decide which card to make a trump.
        """
        return(self.hand[0])

    def makeMove(self, gs):
        """
        Evaluate gs.table and self.hand,
        then make a move.
        """

        # TODO write a function to get
        #      all LEGAL moves available
        #      before making a decision
        # TODO you also need to consider opening
        #      the trump in this function.
        self.playCard(self.hand[0])

    def __str__(self):
        return(f"Name: {self.name}\nHand:{self.hand}")

class smallPlayer(Player): 
    def __init__(self):
        super().__init__()


    # makeMoveSmall
    def makeMove(self, gs):
        current = ""    ## gets the top card on the pile 
        suits = ""    ## suit of the top card
        
        if (len(gs.table) == 0):  #if a card has not been played on the table 
            hand = ()     
            # goes through each of the cards in a players hand to use the smallest card 
            for s in self.handsDic.keys():
                if ("8" in self.handsDic.get(s)): 
                    hand = ("8",s,0)
                elif ("7" in self.handsDic.get(s)): 
                    hand = ("7",s,0)
                elif ("K" in self.handsDic.get(s)): 
                    hand = ("K",s,3)
                elif ("Q" in self.handsDic.get(s)): 
                    hand = ("Q",s,2)
                elif ("10" in self.handsDic.get(s)): 
                    hand = ("10",s,10)
                elif ("A" in self.handsDic.get(s)): 
                    hand = ("A",s,11)
                elif ("9" in self.handsDic.get(s)): 
                    hand = ("9",s,20)
                elif ("J" in self.handsDic.get(s)): 
                    hand = ("J",s,30)
            current = hand 
            suits = suit(current)
                
        else:
            current = gs.table[-1]    ## gets the top card on the pile 
            suits = suit(current)    ## suit of the top card

        suitDic = self.getSuits()  
         

        if (suitDic.get(suits) == 0): #if the player does not have that suit in their hand 
            if (not gs.trumpIsOpen):     
                gs.trumpIsOpen = True   ## trump card is now open 
                suits = gs.trumpSuit

                # if the player doesn't have the suit or the trump suit in their hand 
                if (suitDic.get(suits) == 0): 
                    if (not suitDic.get("H") == 0): 
                        suits = "H"
                    elif (not suitDic.get("D") == 0):
                        suits = "D"
                    elif (not suitDic.get("C") == 0):
                        suits = "C"
                    elif (not suitDic.get("S") == 0):
                        suits = "S"
                                
        # gets the cards in a player's hands     
        cards = self.handsDic.get(suits)
       
        # if the player's hand isn't empty 
        if (isinstance(cards,list) and len(cards) != 0): 
            # goes through in order of rank, playing smaller cards with more preference 
            if ("8" in cards): 
                hand = ("8",suits,0)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("8")
                self.hand.remove(hand)
            elif ("7" in cards): 
                hand = ("7",suits,0)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("7")
                self.hand.remove(hand)
            elif ("K" in cards): 
                hand = ("K",suits,3)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("K")
                self.hand.remove(hand)
            elif ("Q" in cards): 
                hand = ("Q",suits,2)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("Q")
                self.hand.remove(hand)
            elif ("10" in cards): 
                hand = ("10",suits,10)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("10")
                self.hand.remove(hand)
            elif ("A" in cards): 
                hand = ("A",suits,11)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("A")
                self.hand.remove(hand)
            elif ("9" in cards): 
                hand = ("9",suits,20)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("9")
                self.hand.remove(hand)
            elif ("J" in cards): 
                hand = ("J",suits,30)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("J")
                self.hand.remove(hand)
            
           
''' class that has a player playing only the big move strategy'''
class bigPlayer(Player): 
    def __init__(self):
        super().__init__()

    # makeMoveBig
    def makeMove(self, gs):
        current = ""
        suits = ""

        if (len(gs.table) == 0): ##if no card is on the table yet 
            hand = ()
            ## goes through the hand, getting the largest card from the suits and using that as the hand to play
            for s in self.handsDic.keys():
                if ("J" in self.handsDic.get(s)): 
                    hand = ("J",s,30)
                elif ("9" in self.handsDic.get(s)): 
                    hand = ("9",s,20)
                elif ("A" in self.handsDic.get(s)): 
                    hand = ("A",s,11)
                elif ("10" in self.handsDic.get(s)): 
                    hand = ("10",s,10)
                elif ("Q" in self.handsDic.get(s)): 
                    hand = ("Q",s,2)
                elif ("K" in self.handsDic.get(s)): 
                    hand = ("K",s,3)
                elif ("7" in self.handsDic.get(s)): 
                    hand = ("7",s,0)
                elif ("8" in self.handsDic.get(s)): 
                    hand = ("8",s,0)
            current = hand 
            suits = suit(current)
        
        else:
            current = gs.table[-1]    ## gets the top card on the pile 
            suits = suit(current)    ## suit of the top card


        suitDic = self.getSuits()

        if (suitDic.get(suits) == 0): #if the player does not have that suit in their hand 
            if (not gs.trumpIsOpen):     
                gs.trumpIsOpen = True   ## trump card is now open 
                suits = gs.trumpSuit

                # checks to see which suits are remaining in the hand if hand doesn't have trump suit or current suit 
                if (suitDic.get(suits) == 0): 
                    if (not suitDic.get("H") == 0):
                        suits = "H"
                    if (not suitDic.get("D") == 0):
                        suits = "D"
                    if (not suitDic.get("C") == 0):
                        suits = "C"
                    if (not suitDic.get("S") == 0):
                        suits = "S"

        # gets cards in hand           
        cards = self.handsDic.get(suits)
 
        # goes through in order of rank, playing larger cards with more preference 
        if (isinstance(cards,list) and len(cards) != 0): 
            if ("J" in cards): 
                hand = ("J",suits,30)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("J")
                self.hand.remove(hand)
            elif ("9" in cards): 
                hand = ("9",suits,20)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("9")
                self.hand.remove(hand)
            elif ("A" in cards): 
                hand = ("A",suits,11)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("A")
                self.hand.remove(hand)
            elif ("10" in cards): 
                hand = ("10",suits,10)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("10")
                self.hand.remove(hand)
            elif ("Q" in cards): 
                hand = ("Q",suits,2)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("Q")
                self.hand.remove(hand)
            elif ("K" in cards): 
                hand = ("K",suits,3)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("K")
                self.hand.remove(hand)
            elif ("7" in cards): 
                hand = ("7",suits,0)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("7")
                self.hand.remove(hand)
            elif ("8" in cards): 
                hand = ("8",suits,0)
                gs.table.append(hand)
                self.handsDic.get(suits).remove("8")
                self.hand.remove(hand)
    

class MajSmallPlayer(smallPlayer):
    def __init__(self):
        super().__init__()

    # makeBidMaj
    # choose the hand with the largest number of rank of a certain number 
    # if no majority in hand -- bet 160 
    # if 3 out of four cards in hand are one trump suit -- bet 180 
    # if 4 out of four cards in hand are one trump suit -- bet 210 
    def makeBid(self):
        suitDic = self.getSuits()

        # returns the corresponding score and suit based on the number of cards in the ahnds 
        maxSuit = max(suitDic, key=suitDic.get)
        if (suitDic.get(maxSuit) <= 2):
            return 160, maxSuit
        elif (suitDic.get(maxSuit) == 3): 
            return 180, maxSuit
        else: 
            return 210, maxSuit

    

class MajBigPlayer(bigPlayer):
    def __init__(self):
        super().__init__()

    # makeBidMaj
    # choose the hand with the largest number of rank of a certain number 
    # if no majority in hand -- bet 160 
    # if 3 out of four cards in hand are one trump suit -- bet 180 
    # if 4 out of four cards in hand are one trump suit -- bet 210 
    def makeBid(self):
        suitDic = self.getSuits()

        maxSuit = max(suitDic, key=suitDic.get)
        if (suitDic.get(maxSuit) <= 2):
            return 160, maxSuit
        elif (suitDic.get(maxSuit) == 3): 
            return 180, maxSuit
        else: 
            return 210, maxSuit

    


class TopSmallPlayer(smallPlayer):
    def __init__(self):
        super().__init__()

    # makeBidTop
    # choose the hand with the larger amount of high-cards ("J", "9", "A")
    def makeBid(self):
        suitDic = self.getSuits()

        # creates dictionaries with each of the high-card ranks and the suits they are
        suitDicJack = {"H": False, "D": False, "S": False, "C": False}   #whether there is a jack of the trump suit in the hand 
        suitDicNine = {"H": False, "D": False, "S": False, "C": False}   #whether there is a nine of the trump suit in the hand 
        suitDicAce = {"H": False, "D": False, "S": False, "C": False}    #whether there is a ace of the trump suit in the hand

        # updates the dictionaries above 
        for suit in suits: 
            if("J" in self.handsDic.get(suit)): 
                suitDicJack.update({suit: True})
            elif ("9" in self.handsDic.get(suit)):
                suitDicNine.update({suit: True})
            elif ("A" in self.handsDic.get(suit)):
                suitDicAce.update({suit: True}) 

        # finds the suit that has the max amount of cards 
        maxSuit = max(suitDic, key=suitDic.get)

        ## returns the score and the suit 
        if (suitDicJack.get(maxSuit) == True and suitDicNine.get(maxSuit) == True and suitDicAce.get(maxSuit) == True): 
            return 230, maxSuit
        elif (suitDicJack.get(maxSuit) == True and suitDicNine.get(maxSuit) == True): 
            return 210, maxSuit 
        elif (suitDicJack.get(maxSuit) == True and suitDicAce.get(maxSuit) == True): 
            return 180, maxSuit
        else: 
            return 160, maxSuit 

        


class TopBigPlayer(bigPlayer):
    def __init__(self):
        super().__init__()

    # makeBidTop

    # choose the hand with the larger amount of high-cards ("J", "9", "A")
    def makeBid(self):
        suitDic = self.getSuits()

        suitDicJack = {"H": False, "D": False, "S": False, "C": False}   #whether there is a jack of the trump suit in the hand 
        suitDicNine = {"H": False, "D": False, "S": False, "C": False}   #whether there is a nine of the trump suit in the hand 
        suitDicAce = {"H": False, "D": False, "S": False, "C": False}    #whether there is a ace of the trump suit in the hand

        # updates the dictionaries above 
        for suit in suits: 
            if("J" in self.handsDic.get(suit)): 
                suitDicJack.update({suit: True})
            elif ("9" in self.handsDic.get(suit)):
                suitDicNine.update({suit: True})
            elif ("A" in self.handsDic.get(suit)):
                suitDicAce.update({suit: True}) 

        # finds the suit that has the max amount of cards
        maxSuit = max(suitDic, key=suitDic.get)

        ## returns the score and the suit 
        if (suitDicJack.get(maxSuit) == True and suitDicNine.get(maxSuit) == True and suitDicAce.get(maxSuit) == True): 
            return 230, maxSuit
        elif (suitDicJack.get(maxSuit) == True and suitDicNine.get(maxSuit) == True): 
            return 210, maxSuit 
        elif (suitDicJack.get(maxSuit) == True and suitDicAce.get(maxSuit) == True): 
            return 180, maxSuit
        else: 
            return 160, maxSuit 

        

class ValueSmallPlayer(smallPlayer):
    def __init__(self):
        super().__init__()

    # makeBidValue

    # makes big values based on the total sum of the values of the hand
    def makeBid(self):
        suitDic =  self.getSuits()
        maxSuit = max(suitDic, key=suitDic.get)
        
        if (suitDic.get(maxSuit) == 1): 
            return 160, maxSuit


        v = value(self.hand)

        if (v <= 30): 
            return 160, maxSuit
        elif (30 <= v <= 40): 
            return 180, maxSuit
        else: 
            return 210, maxSuit
   


class ValueBigPlayer(bigPlayer):
    def __init__(self):
        super().__init__()

    # makeBidValue
    # makes big values based on the total sum of the values of the hand
    def makeBid(self):
        suitDic =  self.getSuits()
        maxSuit = max(suitDic, key=suitDic.get)
        
        if (suitDic.get(maxSuit) == 1): 
            return 160, maxSuit

        v = value(self.hand)

        if (v <= 30): 
            return 160, maxSuit
        elif (30 <= v <= 40): 
            return 180, maxSuit
        else: 
            return 210, maxSuit


class TestPlayer(Player):
    def __init__(self):
        super().__init__()

    # makeBidValue
    def makeBid(self):
        suitDic = self.getSuits()
        maxSuit = max(suitDic, key=suitDic.get)

        if (suitDic.get(maxSuit) == 1):
            return 160, maxSuit

        v = value(self.hand)

        if (v <= 30):
            return 160, maxSuit
        elif (1 <= v <= 3):
            return 180, maxSuit
        else:
            return 210, maxSuit

class GameState:
    """
    All the things which every player can see:
     * cards on table
     * bids
     * trump
    """
    def __init__(self):
        self.table = []
        self.bids = []
        self.trumpIsOpen = False
        self.trumpSuit = None

    def getIndexOfWinningCard(self):
        # Computation Strategy: assign each card value an
        # arbitrary number of points based on the game circumstance,
        # then take the maximum.
        arbitraryPoints = []
        for i, card in enumerate(self.table):
            points = value(card)
            if self.trumpIsOpen and suit(card) == self.trumpSuit:
                points *= 1000  # matching an open trump with a non-zero card is valuable.
            elif suit(card) != suit(self.table[0]):
                points *= 0  # failing to match the suit is useless.
            elif i == 0:
                points += 0.01  # break ties by giving to the starting player
            arbitraryPoints.append(points)
        return(arbitraryPoints.index(max(arbitraryPoints)))

    def clear_table(self):
        self.table = []

    def __str__(self):
        return(f"table: {self.table}\ntrump: {self.trumpSuit}\ntrump is revealed: {self.trumpIsOpen}")



class GameManager:
    def __init__(self, players=None):
        if players is None:
            players = [TestPlayer(), TestPlayer(), TestPlayer(), TestPlayer()]
        self.players = players
        for i in range(4):
            self.players[i].name = PLAYER_NAMES[i]
        self.reset() # create the deck
        self.scoreboard = [[],[]]  # a 2-D array with two rows and lots of columns
                                   # to store the outcome of each game for eventual
                                   # data analysis.

    def newGameState(self):
        gs = GameState()
        for i in range(4):
            self.players[i].gs = gs
        self.gs = gs


    # Helper method
    # Deal 16 cards from the deck to the 4 players.
    def dealHalf(self):
        for i, player in enumerate(self.players):
            player.giveCards(self.deck[i*4:i*4+4])
        del self.deck[0:16]

    # Helper method
    # Clear the table, take each player's cards,
    # and shuffle the deck.
    def reset(self):
        self.newGameState()
        for player in self.players:
            player.clearHand()
        self.deck = [card for card in ALL_CARDS]
        random.shuffle(self.deck)

    # The sauce!
    def runGame(self):
        self.reset()
        self.dealHalf()

        # BIDDING
        # Simplification: Everyone makes their bid simultaneously
        # (no mind-games with the opponent's bids.)
        # a bid is a (val, suit) where that suit is what the player wants to play.
        self.gs.bids = [player.makeBid() for player in self.players]
        self.gs.bidVals = [bid[0] for bid in self.gs.bids]
        topBid = max(self.gs.bidVals)

        # if multiple players have the same top bid, break ties randomly
        topBidderIndices = [i for i in range(4) if self.gs.bidVals[i] == topBid]
        topBidderIndex = random.choice(topBidderIndices)

        self.dealHalf()

        # Simplification: No point in declaring a trump on the first bidding round.
        # The topBidder may pick their trump from 8 cards.

        self.trumpSuit = self.gs.bids[topBidderIndex][1]



        # Simplification: Each player comes up with a bid separately,
        # and each team uses the higher bid.
        teamOneBid = max(self.gs.bidVals[0], self.gs.bidVals[2])
        teamTwoBid = max(self.gs.bidVals[1], self.gs.bidVals[3])
        

        # PLAYING
        teamOnePool = []
        teamTwoPool = []


        startingPlayerIndex = topBidderIndex
        for rounds in range(8):
            winningPlayerIndex = self.round(startingPlayerIndex)
            if winningPlayerIndex in [0,2]:
                teamOnePool += self.gs.table
            else:
                teamTwoPool += self.gs.table
            self.gs.table = []
            startingPlayerIndex = winningPlayerIndex

        # SCORING
        self.scoreboard[0].append(self.score(teamOnePool, teamOneBid))
        self.scoreboard[1].append(self.score(teamTwoPool, teamTwoBid))

    def runGames(self, n):
        if (n <= 0):
            raise ValueError("Number of games cannot be negative")
        for i in range(n):
            self.runGame()

    # Helper method
    def round(self, startingPlayerIndex):
        # e.g. topBidder = 2 -> playerOrder = [2,3,0,1]
        playerOrder = [position % 4 for position in range(startingPlayerIndex, startingPlayerIndex + 4)]

        # Everyone goes
        for i in range(4):
            currentPlayer = self.players[playerOrder[i]]
            currentPlayer.makeMove(self.gs)

        winningPlayerIndex = playerOrder[self.gs.getIndexOfWinningCard()]
        # winningPlayer = self.players[winningPlayerIndex]

        return(winningPlayerIndex)


    # Helper method
    def getPlayerIndex(self, targetPlayer):
        for i, player in enumerate(self.players):
            if player == targetPlayer:
                return(i)
        raise RuntimeError("This player isn't even part of the game?!")

    # Helper method
    def score(self, cardPool, bid):
        val = value(cardPool)
        if (val >= bid):
            if (val > 200):
                tokens = 4
            else:
                tokens = 2
        else: # val < bid
            tokens = -2
        return(tokens)

    """Given a scoreboard, compute an array of the # of tokens earned by team 1 at each step"""
    def computeTransactions(self):
        n = len(self.scoreboard[0])
        return [self.scoreboard[0][i] - self.scoreboard[1][i] for i in range(n)]

    def expectedOutcome(self):
        transactions = self.computeTransactions()
        return(sum(transactions) / len(transactions))


def running_averages(ts):  # given a time series, compute the running average measured at each time increment
    sum = 0
    averageSeries = []
    for i, x in enumerate(ts):
        sum += x
        n_samples = i + 1
        averageSeries.append(sum/n_samples)
    return(averageSeries)


## EXPERIMENT PHASE 1: which strategy performs the best?

## comparing different strategies together 

# comparing small and big moves 
## Majority Bidding and Small Moves with Majority Bidding and Big Moves
playersMSMB = [MajSmallPlayer(), MajBigPlayer(), MajSmallPlayer(), MajBigPlayer()]
## Top Bidding and Small Moves with Top Bidding and Big Moves 
playersTSTB = [TopSmallPlayer(), TopBigPlayer(), TopSmallPlayer(), TopBigPlayer()]
## Value Bidding and Small Moves with Value Bidding and Big Moves 
playersVSVB = [ValueSmallPlayer(), ValueBigPlayer(), ValueSmallPlayer(), ValueBigPlayer()]

# comparing each of the bidding strategies  
## Majority Bidding and Small Moves with Top Bidding and Small Moves
playersMSTS = [MajSmallPlayer(), TopSmallPlayer(), MajSmallPlayer(), TopSmallPlayer()] 
## Majority Bidding and Small Moves with Value Bidding and Small Moves 
playersMSVS = [MajSmallPlayer(), ValueSmallPlayer(), MajSmallPlayer(), ValueSmallPlayer()]
## Top Bidding and Small Moves with Value Bidding and Small Moves
playersTSVS = [TopSmallPlayer(), ValueSmallPlayer(), TopSmallPlayer(), ValueSmallPlayer()] 

## Majority Bidding and Big Moves with Top Bidding and Big Moves
playersMBTB = [MajBigPlayer(), TopBigPlayer(), MajBigPlayer(), TopBigPlayer()] 
## Majority Bidding and Big Moves with Value Bidding and Big Moves
playersMBVB = [MajBigPlayer(), ValueBigPlayer(), MajBigPlayer(), ValueBigPlayer()] 
## Top Bidding and Big Moves with Value Bidding and Big Moves
playersTBVB = [TopBigPlayer(), ValueBigPlayer(), TopBigPlayer(), MajBigPlayer()] 

# Majority Bidding and Small Moves with Top Bidding and Big Moves
playersMSTS = [MajSmallPlayer(), TopBigPlayer(), MajSmallPlayer(), TopBigPlayer()] 
## Majority Bidding and Small Moves with Value Bidding and Big Moves 
playersMSVS = [MajSmallPlayer(), ValueBigPlayer(), MajSmallPlayer(), ValueBigPlayer()]
## Top Bidding and Small Moves with Value Bidding and Big Moves
playersTSVS = [TopSmallPlayer(), ValueBigPlayer(), TopSmallPlayer(), ValueBigPlayer()] 

# Majority Bidding and Big Moves with Top Bidding and Small Moves
playersMSTS = [MajBigPlayer(), TopSmallPlayer(), MajBigPlayer(), TopSmallPlayer()] 
## Majority Bidding and Big Moves with Value Bidding and Small Moves 
playersMSVS = [MajBigPlayer(), ValueSmallPlayer(), MajBigPlayer(), ValueSmallPlayer()]
## Top Bidding and Big Moves with Value Bidding and Small Moves
playersTSVS = [TopBigPlayer(), ValueSmallPlayer(), TopBigPlayer(), ValueSmallPlayer()] 

allPlayerStrategies = [playersMSMB,playersTSTB,playersVSVB,playersMSTS,playersMSVS,playersTSVS,
playersMBTB,playersMBVB,playersTBVB,playersMSTS,playersMSVS,playersTSVS,playersMSTS,playersMSVS,playersTSVS]



def createPlayerFromIndex(i):
    if i==0:
        return MajSmallPlayer()
    elif i==1:
        return MajBigPlayer()
    elif i==2:
        return TopSmallPlayer()
    elif i==3:
        return TopBigPlayer()
    elif i==4:
        return ValueSmallPlayer()
    elif i==5:
        return ValueBigPlayer()
    else:
        return None

count = 0
experimentResults = []
N_GAMES = 5000
for i in range(6):
    experimentResults.append([])
    for j in range(6):
        playerSet = [createPlayerFromIndex(i),
                     createPlayerFromIndex(j),
                     createPlayerFromIndex(i),
                     createPlayerFromIndex(j)]

        gm = GameManager(playerSet)
        gm.runGames(N_GAMES)
        expected_outcome = gm.expectedOutcome()

        experimentResults[i].append(expected_outcome)

for row in experimentResults:
    line = " ".join([str(round(val,3)) for val in row])
    print(line)







## EXPERIMENT PHASE 2: let's dig deeper into one particular strategy.
N_GAMES = 5000
N_EXPERIMENTS = 10

gm = GameManager([MajBigPlayer(), MajSmallPlayer(), MajBigPlayer(), MajSmallPlayer()])
gm.runGames(N_GAMES)
expected_outcome = gm.expectedOutcome()
print(f"Expected outcome: {expected_outcome}")
print()

"""

## Plot the convergence
for i in range(N_EXPERIMENTS):
    gm = GameManager()
    for g in range(N_GAMES):
        gm.runGame()
    transactions = computeTransactions(gm.scoreboard)
    plt.plot(range(N_GAMES), running_averages(transactions), linewidth=1)
#plt.hlines(y=[0, expected_outcome], xmin=[-N_GAMES, 0], xmax=[2*N_GAMES, N_GAMES], colors=["#BBBBBB","red"], linestyles=["solid", "dashed"])
plt.hlines(y=0, xmin=-N_GAMES, xmax=[2*N_GAMES], colors="#BBBBBB", linestyles="solid")
#plt.vlines(x=0, ymin=-20, ymax=20, colors="#BBBBBB")
plt.title(f"Convergence of the measured average token gain\n{N_GAMES} simulations each in {N_EXPERIMENTS} experiments", fontsize=16)
plt.xlabel("# of simulated games", fontsize=14)
plt.ylabel("Measured average token gain", fontsize=14)
plt.xlim(-3/1000*N_GAMES, N_GAMES)
plt.ylim(-6,6)
plt.show()

## Plot a discrete histogram of outcomes
sns.histplot(transactions, discrete=True, binrange=(-8,8), stat="density")
plt.xticks(range(-8,8+2,2), range(-8,8+2,2))
plt.title("Empirical distribution of outcomes for Team 1", fontsize=16)
plt.xlabel("Possible outcome", fontsize=14)
plt.ylabel("Empirical Probability", fontsize=14)
plt.show()


## Plot a continuous histogram of average outcomes
N_EXPERIMENTS = 500
N_GAMES = 500
means = []
for i in range(N_EXPERIMENTS):
    gm = GameManager()
    for g in range(N_GAMES):
        gm.runGame()
    transactions = computeTransactions(gm.scoreboard)
    means.append(sum(transactions)/N_GAMES)
sns.histplot(means, stat="density")
plt.xlabel("Expected value", fontsize=14)
plt.ylabel("Probability density", fontsize=14)
plt.title("Empirical sampling distribution of mean outcomes for Team 1\n500 measurements of sample means with n=500", fontsize=16)
plt.show()

"""