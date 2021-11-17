import random

## Create constants.
PLAYER_NAMES = ["South", "East", "North", "West"]
ALL_CARDS = {}
ranks = ["J", "9", "A", "10", "K", "Q", "8", "7"]
suits = ["H", "D", "S", "C"]
values = [30, 20, 11, 10, 3, 2, 0, 0]
ALL_CARDS = {(r,s,values[i]) for i, r in enumerate(ranks) for s in suits}
del ranks; del suits; del values

## Avoid index hell.
def rank(card):
    return(card[0])
def suit(card):
    return(card[1])
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

    self.hand = []
    self.name = None
    self.gs = None
    self.bidInFirstRound = None  # for use in makeSecondBid()
    self.suitDic = {}

    def __init__(self):
        pass

    def giveCards(self, cards):
        if isinstance(cards, list):
            self.hand += cards
        if isinstance(cards, tuple):
            self.hand += [cards]

    def playCard(self, card):
        self.cards.remove(card)
        gs.table += [card]


    ## Decisions for child classes to make
    ## This parent class makes naive decisions.
    ## 
    ## DO NOT WASTE YOUR TIME trying to improve these.
    ## These are just placeholders so that the code can 
    ## run without actually implementing each decision.
    def makeFirstBid(self):
        """
        Evaluate the 4 cards in self.hand,
        then make a bid between 160 and 200.
        """
        bid = 160
        self.bidInFirstRound = bid
        return(bid)

    def makeSecondBid(self, gs):
        """
        Evaluate the 8 cards in self.hand
                 and maybe also self.gs,
        then decide whether to raise the your bid to 250.
        """
        return(self.bidInFirstRound)

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
        playCard(self.hand[0])
    
    def __str__(self):
        return(f"Name: {name}\nHand:{hand}", self.name, self.hand)



class SimplePlayer(Player):
    def __init__(self)
        super().__init__()

    # IMPORTANT:
    # To implement these decision functions,
    # create an external function and pass the necessary
    # parameters into it.
    # 
    # This way, two players can share particular strategies
    # without reusing code.
    #
    # For now, I have each decision function commented out
    # so that before you implement them, SimplePlayer inherits
    # the naive decision functions from Player.

    def getSuits(): 
        suitDic = {"H": 0, "D": 0, "S": 0, "C": 0}
        for hand in self.hand: 
            s = suit(hand)
            suitDic.update({s: suitDic.get(s) + 1})

        return suitDic 


    # choose the hand with the largest number of rank of a certain number 
    # if no majority in hand -- bet 160 
    # if 3 out of four cards in hand are one trump suit -- bet 180 
    # if 4 out of four cards in hand are one trump suit -- bet 210 
    def makeFirstBidMaj(self): 
        suitDic = getSuits()
        maxSuit = max(suitDic, key=suitDic.get)
        if (suitDic.get(maxSuit) <= 2):
            return 160, maxSuit
        elif (suitDic.get(maxSuit) == 3): 
            return 180, maxSuit
        else: 
            return 210, maxSuit

    
    def makeFirstBidTop(self): 
        suitDic = {"H": 0, "D": 0, "S": 0, "C": 0}
        suitDicJack = {"H": False, "D": False, "S": False, "C": False}   #whether there is a jack of the trump suit in the hand 
        suitDicNine = {"H": False, "D": False, "S": False, "C": False}   #whether there is a nine of the trump suit in the hand 
        suitDicAce = {"H": False, "D": False, "S": False, "C": False}    #whether there is a ace of the trump suit in the hand

        for hand in self.hand: 
            r = rank(hand)
            suitDic.update({r: suitDic.get(r) + 1})
            s = suit(hand)
            if (s == "J"):
                suitDicJack.update({r: True})
            elif (s == "9")
                suitDicNine.update({r: True})
            elif (s = "A"):
                suitDicAce.update({r: True})

        maxSuit = max(suitDic, key=suitDic.get)

        if (suitDicJack.get(maxSuit) == True and suitDicNine.get(maxSuit) == True and suitDicAce.get(maxSuit) == True): 
            return 230, maxSuit
        elif (suitDicJack.get(maxSuit) == True and suitDicNine.get(maxSuit) == True): 
            return 210, maxSuit 
        elif (suitDicJack.get(maxSuit) == True and suitDicAce.get(maxSuit) == True): 
            return 180, maxSuit
        else: 
            return 160, maxSuit 


    def makeFirstBidValue(self):
        suitDic getSuits()
        maxSuit = max(suitDic, key=suitDic.get)
        
        if (suitDic.get(maxSuit) == 1): 
            return 160, maxSuit

        v = value(self.hand)

        if (v <= ): 
            return 160, maxSuit
        elif (1 <= v <= 3): 
            return 180, maxSuit
        else: 
            return 210, maxSuit
    

    def makeFirstBid(self):

    
    """TODO -- don't need because we handle it in bid function 
    def pickTrump(self):
        # TODO write an external function for this.
        pass
    """


    def makeMoveSmall(self, gs):
        current = gs.table[-1]    ## gets the top card on the pile 
        suit = suit(current)    ## suit of the top card 
        suitDic = getSuits()    

        if (suitDic.get(suit) > 0): #if the player has that suit in their hand 
            

        else (suitDic.get(suit) > 0): 


    def makeMoveBig(self, gs): 
        current = gs.table[-1]    ## gets the top card on the pile 
        suit = suit(current)    ## suit of the top card 
        suitDic = getSuits()    

        suitDicJack = {"H": False, "D": False, "S": False, "C": False}   #whether there is a jack of the trump suit in the hand 
        suitDicNine = {"H": False, "D": False, "S": False, "C": False}   #whether there is a nine of the trump suit in the hand 
        suitDicAce = {"H": False, "D": False, "S": False, "C": False}    #whether there is a ace of the trump suit in the hand
        suitDicTen = {"H": False, "D": False, "S": False, "C": False}   #whether there is a jack of the trump suit in the hand 
        suitDicQueen = {"H": False, "D": False, "S": False, "C": False}   #whether there is a nine of the trump suit in the hand 
        suitDicKing = {"H": False, "D": False, "S": False, "C": False}    #whether there is a ace of the trump suit in the hand
        suitDicSeven = {"H": False, "D": False, "S": False, "C": False}   #whether there is a nine of the trump suit in the hand 
        suitDicEight = {"H": False, "D": False, "S": False, "C": False}    #whether there is a ace of the trump suit in the hand

        for hand in self.hand: 
            s = suit(hand)
            if (s == "J"):
                suitDicJack.update({r: True})
            elif (s == "9")
                suitDicNine.update({r: True})
            elif (s = "A"):
                suitDicAce.update({r: True})
            elif (s = "10"): 
                suitDicTen.update({r: True})
            elif (s = "K"):
                suitDicKing.update({r: True})
            elif (s = "Q"):
                suitDicQueen.update({r: True})
            elif (s = "8"):
                suitDicEight.update({r: True})
            elif (s = "7"):
                suitDicSeven.update({r: True})

        if (suitDic.get(suit) > 0): #if the player has that suit in their hand 
            if (suitDicJack.get(suit) == True): 
                gs.table.append(hand)
                suitDicJack.update({suit: False})
                self.hand.remove(hand)
            
        else: 
            if (not gs.trumpIsOpen):     
                gs.trumpIsOpen = True   ## trump card is now open 
            
            if (suitDic.get(current) > 0): 
                getSuits() 
                
                
                

                

        

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
                points *= 1000  # matching an open trump is valuable.
            elif suit(card) != suit(self.table[0]):
                points *= 0  # failing to match the suit is useless.
            arbitraryPoints.append(points)
        return(arbitraryPoints.index(max(arbitraryPoints)))

    def clear_table(self):
        self.table = []

    def __str__(self):
        return(f"table: {table}\ntrump: {trumpSuit}\ntrump is revealed: {trumpIsOpen}")

    


class GameManager:
    def __init__(self, verbose=False):
        self.players = [SimplePlayer(), SimplePlayer(), SimplePlayer(), SimplePlayer()]
        for i in range(4):
            players[i].name = PLAYER_NAMES[i]
        self.verbose = verbose
        self.reset()
        self.scoreboard = []  # this can be a 2-D array with 
                              # two rows and lots of columns
                              # to store the outcome of each game
                              # for eventual data analysis.

    def newGameState(self):
        gs = GameState()
        for i in range(4):
            players[i].gs = gs
        self.gs = gs


    # Deal 16 cards from the deck to the 4 players.
    def dealHalf(self):
        for i, player in enumerate(players):
            player.giveCards(deck[i*4:i*4+4])
        del deck[0:16]

    # Clear the table, take each player's cards,
    # and shuffle the deck.
    def reset(self):
        self.newGameState()
        for player in self.players:
            player.setHand([])
        self.deck = [card for card in ALL_CARDS]
        random.shuffle(self.deck)

    # The sauce!
    def runGame(self):
        self.reset()
        self.dealHalf()

        # FIRST ROUND OF BIDDING
        # Simplification: Everyone makes the first bid simultaneously
        # (no mind-games with the opponent bids.)
        gs.bids = [player.makeFirstBet() for player in self.players]
        
        # Simplification: No point in declaring a trump on the first bidding round.
        
        # SECOND ROUND OF BIDDING
        self.dealHalf()
        ## gs.bids = [player.makeSecondBet(gs) for player in self.players]
        topBidder = players[gs.bids.index(max(gs.bids))]
        self.trumpSuit = topBidder.pickTrump()
        # Simplification: Each player comes up with a bid separately,
        # and each team uses the higher bid.
        teamOneBid = max(self.bids[0], self.bids[2])
        teamTwoBid = max(self.bids[1], self.bids[3])
        

        # PLAYING
        # (this section has not been tested yet)
        teamOnePool = []
        teamTwoPool = []

        startingPlayer = topBidder
        for rounds in range(8):
            winningPlayer, winningPlayerIndex = round(startingPlayer)
            if winningPlayerIndex in [0,2]:
                teamOnePool += gs.table
            else:
                teamTwoPool += gs.table
            gs.table = []
            startingPlayer = winningPlayer


        
        

        # TODO compare value(teamOnePool) against teamOneBid
        #      compare value(teamTwoPool) against teamTwoBid
        #      mark the correct number of points on the scoreboard.
        

    def round(startingPlayer):
        # e.g. topBidder = 2 -> playerOrder = [2,3,0,1]
        playerOrder = [position % 4 for position in range(startingPlayer, startingPlayer + 4)]

        # Everyone goes
        for i in range(4):
            currentPlayer = self.players[playerOrder[i]]
            currentPlayer.makeMove(self.gs)

        winningPlayerIndex = playerOrder[gs.getIndexOfWinningCard()]
        winningPlayer = self.players[winningPlayerIndex]

        return(winningPlayer, winningPlayerIndex)

