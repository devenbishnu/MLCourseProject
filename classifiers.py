import copy
import math
import translators
import random
from sklearn import svm, neighbors
from sklearn.neural_network import MLPClassifier


#
# generate confusion matrices for tictac_final and tictac_single using k-fold cross validation
#
def run():
    solve_final()
    solve_single()
    return 0


#
# generate confusion matrices for tictac_final
#
def solve_final():
    print("--tictac_final.txt--")
    print("Performing 10-fold cross validation...")
    svmresult = []
    knearresult = []
    mlpresult = []
    data = translators.get_tictac_final()
    inputdata = k_fold(data)
    for i in range(len(inputdata)):
        trainingfeatures = inputdata[i][0]
        traininglabels = inputdata[i][1]
        testfeatures = inputdata[i][2]
        testlabels = inputdata[i][3]
        svmresult.extend(linear_svm(trainingfeatures, traininglabels, testfeatures, testlabels))
        knearresult.extend(k_nearest(trainingfeatures, traininglabels, testfeatures, testlabels))
        mlpresult.extend(mlp(trainingfeatures, traininglabels, testfeatures, testlabels))
        print("Fold " + str(i + 1) + "/10 complete")
    print("")
    final_confusion(svmresult, "linear SVM")
    final_confusion(knearresult, "k-nearest neighbors")
    final_confusion(mlpresult, "multilayer perceptron")
    print("")


#
# generate confusion matrices for tictac-single
#
def solve_single():
    print("--tictac_single.txt--")
    print("Performing 10-fold cross validation...")
    svmresult = []
    knearresult = []
    mlpresult = []
    data = translators.get_tictac_single()
    inputdata = k_fold(data)
    for i in range(len(inputdata)):
        trainingfeatures = inputdata[i][0]
        traininglabels = inputdata[i][1]
        testfeatures = inputdata[i][2]
        testlabels = inputdata[i][3]
        svmresult.extend(
            linear_svm(trainingfeatures, traininglabels, testfeatures,
                       testlabels))
        knearresult.extend(
            k_nearest(trainingfeatures, traininglabels, testfeatures,
                      testlabels))
        mlpresult.extend(mlp(trainingfeatures, traininglabels, testfeatures, testlabels))
        print("Fold " + str(i + 1) + "/10 complete")
    print("")
    single_confusion(svmresult, "linear SVM")
    single_confusion(knearresult, "k-nearest neighbors")
    single_confusion(mlpresult, "multilayer perceptron")
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
            testlabels.append(j[9])
        for j in trainingdata:
            trainingfeatures.append(j[0:9])
            traininglabels.append(j[9])
        result.append([copy.deepcopy(trainingfeatures), copy.deepcopy(traininglabels), copy.deepcopy(testfeatures),
                       copy.deepcopy(testlabels)])
    return result


#
# creates a linear svm from the dataset and returns predictions for the test features
#
def linear_svm(trainingfeatures, traininglabels, testfeatures, testlabels):
    clf = svm.SVC()
    clf.fit(trainingfeatures, traininglabels)
    result = []
    for i in range(len(testfeatures)):
        prediction = clf.predict([testfeatures[i]])
        result.append([prediction[0], testlabels[i]])
    return result


#
# creates a knn model from the dataset and returns predictions for the test features
#
def k_nearest(trainingfeatures, traininglabels, testfeatures, testlabels):
    clf = neighbors.KNeighborsClassifier(15, weights="uniform")
    clf.fit(trainingfeatures, traininglabels)
    result = []
    for i in range(len(testfeatures)):
        prediction = clf.predict([testfeatures[i]])
        result.append([prediction[0], testlabels[i]])
    return result


#
# creates a multilayer perceptron from the dataset and generates predictions for the test features
#
def mlp(trainingfeatures, traininglabels, testfeatures, testlabels):
    clf = MLPClassifier(random_state=1, max_iter=1500)
    clf.fit(trainingfeatures, traininglabels)
    result = []
    for i in range(len(testfeatures)):
        prediction = clf.predict([testfeatures[i]])
        result.append([prediction[0], testlabels[i]])
    return result


#
# creates a confusion matrix for a model trained on tictac_final data and prints it
#
def final_confusion(data, model):
    truewin = 0
    trueloss = 0
    falsewin = 0
    falseloss = 0
    for i in data:
        if i[0] == i[1]:
            if i[0] == -1:
                truewin = truewin + 1
            if i[0] == 1:
                trueloss = trueloss + 1
        else:
            if i[0] == -1:
                falsewin = falsewin + 1
            if i[0] == 1:
                falseloss = falseloss + 1
    row1 = [round(falsewin / (falsewin + trueloss), 2), round(trueloss / (falsewin + trueloss), 2)]
    row2 = [round(truewin / (truewin + falseloss), 2), round(falseloss / (truewin + falseloss), 2)]
    print(model + ":")
    accuracy = (truewin + trueloss) / len(data)
    print("Statistical Accuracy: " + str(accuracy))
    print("Confusion Matrix:")
    toplabels = ["Predicted Win ", "Predicted Loss "]
    sidelabels = ["Actual Loss ", "Actual Win "]
    table = [row1, row2]
    format_row = "{:>12}" * 3
    for side, row in zip(sidelabels, table):
        print(format_row.format(side, *row))
    print(format_row.format(" ", *toplabels))
    print("")


#
# creates a confusion matrix for a model trained on tictac_single data and prints it
#
def single_confusion(data, model):
    actuals = [[0 for _ in range(9)] for _ in range(9)]
    ratios = []
    table = []
    toplabels = []
    correct = 0
    for i in data:
        if i[0] == i[1]:
            val = i[0]
            actuals[val][val] = actuals[val][val] + 1
            correct = correct + 1
        else:
            val = i[0]
            trueval = i[1]
            actuals[trueval][val] = actuals[trueval][val] + 1
    for i in range(len(actuals)):
        ratios.append([])
        for j in range(len(actuals[i])):
            ratios[i].append(round(actuals[i][j] / sum(actuals[i]), 2))
    actuals = ratios
    for i in range(len(actuals)):
        prefix = "Actual " + str(i) + " "
        toplabels.append("Predicted " + str(i) + " ")
        prefix = [prefix]
        prefix.extend(actuals[i])
        table.append(prefix)
    table = reversed(table)
    format_row = "{:>12}" * 10
    print(model + ":")
    accuracy = correct / len(data)
    print("Statistical Accuracy: " + str(accuracy))
    print("Confusion Matrix:")
    for row in table:
        print(format_row.format(*row))
    print(format_row.format(" ", *toplabels))
    print("")
