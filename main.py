import classifiers
import regressors
import c4game
import linear_regressor


#
# loop prompt user for mode (tic-tac-toe classifier or connect 4 bot)
#
def main():
    prompt = ""
    while True:
        if prompt == "classifier-regressor":
            classifiers.run()
            regressors.run()
            prompt = ""
        elif prompt == "connect four":
            c4game.run()
            prompt = ""
        elif prompt == "exit":
            return
        else:
            prompt = input("Please choose a program (\"classifier-regressor\" OR \"connect four\" OR \"exit\")\n")


if __name__ == "__main__":
    main()
