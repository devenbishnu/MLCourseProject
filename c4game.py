import connectfourboard
import translators
from sklearn.neural_network import MLPRegressor


#
# performs command-line-based turn cycling and win checking for connect 4 game
#
def run():
    print("Launching Connect 4 game...")
    model = getmodel()
    game = connectfourboard.ConnectFour()
    while game.is_won() == 0:
        game.print_board()
        column = aiturn(game, model)
        game.place(column, 1)
        game.print_board()
        valid = False
        if game.is_won() == 1:
            print("AI wins!")
            return
        if game.is_won() == 2:
            print("Tie!")
            return
        print("Player turn:")
        while not valid:
            column = int(input("Column to place in (0-6):\n"))
            valid = game.place(column, -1)
            if not valid:
                print("Invalid column. Please try again.")
        game.print_board()
        if game.is_won() == -1:
            print("Player wins!")
            return
        if game.is_won() == 2:
            print("Tie!")
            return
    return


#
# creates a multilayer perceptron classifying board states as likely to win, lose, or tie
#
def getmodel():
    print("Loading training data...")
    data = translators.get_connect_four()
    features = []
    labels = []
    print("Training...")
    for i in range(len(data)):
        features.append(data[i][0:42])
        labels.append(data[i][42])
    reg = MLPRegressor(random_state=1, max_iter=1500)
    reg.fit(features, labels)
    print("Training done. Starting game...")
    return reg


#
# returns the first valid column likely to result in a win for the AI
#
def aiturn(game, model):
    print("AI turn:")
    score = 0
    result = 0
    for i in range(7):
        if game.winning_move(i, 1):
            return i
        potential = game.board_if(i, 1)
        if len(potential) == 0:
            continue
        prediction = model.predict([potential])
        if prediction[0] > score:
            score = prediction[0]
            result = i
    return result