import copy
import math
import linear_regressor
import translators
import random
from sklearn import neighbors
from sklearn.neural_network import MLPRegressor


#
# generate confusion matrices for tictac_multi using k-fold cross-validation
#
def run():
    solve_multi()
    return 0


#
# generate confusion matrices for tictac_multi
#
def solve_multi():
    print("--tictac_multi.txt--")
    print("Performing 10-fold cross validation...")
    knearresult = [[] for _ in range(9)]
    linregresult = [[] for _ in range(9)]
    mlpresult = [[] for _ in range(9)]
    data = translators.get_tictac_multi()
    inputdata = k_fold(data)
    for i in range(len(inputdata)):
        trainingfeatures = inputdata[i][0]
        traininglabels = inputdata[i][1]
        testfeatures = inputdata[i][2]
        testlabels = inputdata[i][3]
        outcome = k_nearest(trainingfeatures, traininglabels, testfeatures, testlabels)
        for j in range(len(outcome)):
            knearresult[j].extend(outcome[j])
        #outcome = linreg(trainingfeatures, traininglabels, testfeatures, testlabels)
        #for j in range(len(outcome)):
            #linregresult[j].extend(outcome[j])
        outcome = mlp(trainingfeatures, traininglabels, testfeatures, testlabels)
        for j in range(len(outcome)):
            mlpresult[j].extend(outcome[j])
        print("Fold " + str(i + 1) + "/10 complete")
    print("")
    confusion(knearresult, "k-nearest neighbors")
    print("")
    #confusion(linregresult, "linear regression")
    print("")
    confusion(mlpresult, "multilayer perceptron")
    print("")


#
# generates datasets for k-fold cross validation, k=10, returning an array of training and test labels/features
#
def k_fold(data):
    k = 10
    result = []
    segments = []
    random.shuffle(data)
    indexer = math.trunc(len(data) / 10)
    for i in range(k - 1):
        segments.append(copy.deepcopy(data[(i * indexer):((i + 1) * indexer)]))
    segments.append(copy.deepcopy(data[((k - 1) * indexer):(len(data) - 1)]))
    for i in range(k):
        trainingfeatures = []
        traininglabels = []
        testfeatures = []
        testlabels = []
        testdata = segments[i]
        trainingdata = []
        for j in range(10):
            if i == j:
                continue
            trainingdata.extend(segments[j])
        for j in testdata:
            testfeatures.append(j[0:9])
            testlabels.append(j[9:18])
        for j in trainingdata:
            trainingfeatures.append(j[0:9])
            traininglabels.append(j[9:18])
        result.append([copy.deepcopy(trainingfeatures), copy.deepcopy(traininglabels), copy.deepcopy(testfeatures),
                       copy.deepcopy(testlabels)])
    return result


#
# creates a knn model from the dataset and returns predictions for the test features
#
def k_nearest(trainingfeatures, traininglabels, testfeatures, testlabels):
    result = []
    for i in range(9):
        labels = []
        outputs = []
        labelresult = []
        for j in range(len(traininglabels)):
            labels.append(traininglabels[j][i])
        for j in range(len(testlabels)):
            outputs.append(testlabels[j][i])
        reg = neighbors.KNeighborsRegressor(15, weights="uniform")
        reg.fit(trainingfeatures, labels)
        for j in range(len(testfeatures)):
            prediction = reg.predict([testfeatures[j]])
            labelresult.append([round(prediction[0]), testlabels[j][i]])
        result.append(labelresult)
    return result


#
# creates a linear regression model from the dataset and returns predictions for test features
#
def linreg(trainingfeatures, traininglabels, testfeatures, testlabels):
    result = []
    for i in range(9):
        labels = []
        outputs = []
        labelresult = []
        for j in range(len(traininglabels)):
            labels.append(traininglabels[j][i])
        for j in range(len(testlabels)):
            outputs.append(testlabels[j][i])
        reg = linear_regressor.LinearRegressor()
        reg.fit(trainingfeatures, labels)
        for j in range(len(testfeatures)):
            prediction = reg.predict([testfeatures[j]])
            labelresult.append([round(prediction[0]), testlabels[j][i]])
        result.append(labelresult)
    return result


#
# creates a multilayer perceptron from the dataset and generates predictions for the test features
#
def mlp(trainingfeatures, traininglabels, testfeatures, testlabels):
    result = []
    for i in range(9):
        labels = []
        outputs = []
        labelresult = []
        for j in range(len(traininglabels)):
            labels.append(traininglabels[j][i])
        for j in range(len(testlabels)):
            outputs.append(testlabels[j][i])
        reg = MLPRegressor(random_state=1, max_iter=1500)
        reg.fit(trainingfeatures, labels)
        for j in range(len(testfeatures)):
            prediction = reg.predict([testfeatures[j]])
            labelresult.append([round(prediction[0]), testlabels[j][i]])
        result.append(labelresult)
    return result


#
# creates a confusion matrix for a model trained on tictac_multi data and prints it
#
def confusion(data, model):
    for i in range(len(data)):
        truegood = 0
        truebad = 0
        falsegood = 0
        falsebad = 0
        total = 0
        for j in data[i]:
            total = total + 1
            if j[0] == j[1]:
                if j[0] == 1:
                    truegood = truegood + 1
                if j[0] == 0:
                    truebad = truebad + 1
            else:
                if j[0] == 1:
                    falsegood = falsegood + 1
                if j[0] == 0:
                    falsebad = falsebad + 1
        row1 = [round(falsegood / (falsegood + truebad), 2), round(truebad / (falsegood + truebad), 2)]
        row2 = [round(truegood / (truegood + falsebad), 2), round(falsebad / (truegood + falsebad), 2)]
        print(model + " Regression (output = " + str(i) + "):")
        accuracy = (truegood + truebad) / total
        print("Statistical Accuracy: " + str(accuracy))
        print("Confusion Matrix:")
        toplabels = ["Predicted Optimal ", "Predicted Not Optimal "]
        sidelabels = ["Actual Not Optimal ", "Actual Optimal     "]
        table = [row1, row2]
        format_row = "{:>12}" * 3
        for side, row in zip(sidelabels, table):
            print(format_row.format(side, *row))
        print(format_row.format("              ", *toplabels))
        print("")
