class person:
    def __init__(self, one_name):
        self.cards = []
        self.scores = 0
        self.name = one_name

    def draw_cards(self, stock):
        string = stock[0]
        self.cards.append(string)
        stock.pop(0)

    def play_cards(self, previous_card):
        pre_items = previous_card.split()
        while True:
            choice = input(
                "The previous card is " + previous_card + ", please choose one card to play(just type in the index of "
                                                          "the card and 0 means that you can't play)")
            try:
                choice_card = int(choice)
                my_card = self.cards[choice_card-1]
                your_item = my_card.split()
                if '0' <= pre_items[1] <= '9':
                    if your_item[0] == pre_items[0] or your_item[1] == pre_items[1]:
                        break
            except Exception as e:
                print(e)
                print("please enter again!")


