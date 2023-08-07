# MLCourseProject
Sample of code from a machine learning course I took in university. Do not plagiarize for homework.

## Usage
python3 main.py

## Description:
Demonstrates applications of classification and regression algorithms. A command line interface will prompt the user to select either classifier-regressor or connect four modes.

### classifier-regressor
Generates confusion matrices using 10-fold cross-validation for the data sets tictac_final, tictac_multi, and tictac_single.

tictac_final:
A set of completed tic-tac-toe games, with the first 9 entries in a row being the player occupant of a given spot, and the tenth index being the winner of the game.
Classifier algorithms are used for k-fold cross-validation to predict winners, with linear SVM, KNN, and multilayer perceptron classifiers being used from scikit-learn.

tictac_multi:
A set of tic-tac-toe games, with the first 9 entries in a row being the player occupant of a given spot, and the subsequent 9 entries being a boolean indicating whether a spot is both valid and optimal for the player to place their next marker in.
Regressor algorithms are used for k-fold cross-validation to predict the index of an optimal spot, with KNN, linear regression, and multilayer perceptron regressors being used. The KNN and multilayer perceptron algorithms are sourced from scikit-learn; the linear regression algorithm is written by hand and is found in linear_regressor.py.

tictac_single:
A set of tic-tac-toe games, with the first 9 entries in a row being the player occupant of a given spot, and the tenth index being the optimal space for the player to place their next marker in.
Classifier algorithms are used for k-fold cross-validation to predict the index of an optimal spot, with linear SVM, KNN, and multilayer perceptron classifiers being used from scikit-learn.

### connect four
Generates a regressor multilayer perceptron model for playing connect four from the connectfour dataset. This dataset contains connect four board states, along with the predicted winner of the game based on the board state. This model is used to support an AI opponent which can be played against. The AI will check the potential board that would result for placing its token in each column, and place its token in the column for which the regressor model returns the highest score. If two columns' scores are equal, it will place its token in the leftmost high-scoring column. The game is played until someone wins or the game ties.
The multilayer perceptron classifier is sourced from scikit-learn.