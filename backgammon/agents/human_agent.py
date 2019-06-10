from ..game import Game

class HumanAgent(object):
    def __init__(self, player):
        self.player = player
        self.name = 'Human'

    def get_action(self, moves, game=None,doubles=False):
        if not moves:
            input("No moves for you...(hit enter)")
            return None
        
        mv1 = mv2 = mv3 = mv4 = None
        while True:
            while True:
                mv1 = input('Please enter a move "<location start>,<location end>" ("%s" for on the board, "%s" for off the board): ' % (Game.ON, Game.OFF))
                mv1 = self.get_formatted_move(mv1)
                if not mv1:
                    print('Bad format enter e.g. "3,4" for the first move')
                else:
                    break

            while True:
                mv2 = input('Please enter a second move (enter to skip): ')
                if mv2 == '':
                    mv2 = None
                    break
                mv2 = self.get_formatted_move(mv2)
                if not mv2:
                    print('Bad format enter e.g. "3,4" for the second move')
                else:
                    break

            if doubles:
                while True:
                    mv3 = input('Please enter a third move (enter to skip): ')
                    if mv3 == '':
                        mv3 = None
                        break
                    mv3 = self.get_formatted_move(mv3)
                    if not mv3:
                        print('Bad format enter e.g. "3,4" for the third move')
                    else:
                        break

                while True:
                    mv4 = input('Please enter a fourth move (enter to skip): ')
                    if mv4 == '':
                        mv4 = None
                        break
                    mv4 = self.get_formatted_move(mv4)
                    if not mv4:
                        print('Bad format enter e.g. "3,4" for the fourth move')
                    else:
                        break

            if mv4 and doubles:
                move = (mv1, mv2, mv3, mv4)
            elif mv3 and doubles:
                move = (mv1, mv2, mv3,)
            elif mv2 and doubles:
                move = (mv1, mv2,"",)
            elif mv1 and doubles:
                move = (mv1,"","",)
            elif mv2:
                move = (mv1, mv2)
            else:
                move = (mv1,)

            if move in moves:
                return move
            elif move[::-1] in moves:
                move = move[::-1]
                return move
            else:
                print("You can't play that move")
                """check the moves that you entered"""
                if FLAGS.test:
                    for mov in move:
                        print(mov)
                
        return None

    def get_formatted_move(self, move):
        try:
            start, end = move.split(",")
            if start == Game.ON:
                return (start, int(end))
            if end == Game.OFF:
                return (int(start), end)
            return (int(start), int(end))
        except:
            return False
