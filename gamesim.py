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
        return(card[2])
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

    """TODO
    def makeFirstBid(self):
        # TODO write an external function for this.
        pass
    """

    """TODO
    def makeSecondBid(self, gs):
        # TODO write an external function for this.
        pass
    """
    
    """TODO
    def pickTrump(self):
        # TODO write an external function for this.
        pass
    """

    """TODO
    def makeMove(self, gs):
        # TODO write an external function for this.
        pass
    """

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
        gs.bids = [player.makeSecondBet(gs) for player in self.players]
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

