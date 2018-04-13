import csv
import pandas
import numpy
import sklearn
import sklearn.model_selection
import sklearn.neighbors
import sklearn.svm
import sklearn.ensemble
import sklearn.tree


def main():
    # Training Data
    # Data 1 Learning
    with open('TrainData1.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('1.00000000000000e+99', 'NaN')
    with open('TrainData1_NaN.txt', 'w') as file:
        file.write(filedata)
    # Save imputed data to file and keep in dataframe for computation
    datasetlearn1 = pandas.read_csv('TrainData1_NaN.txt', header=None, index_col=None, delim_whitespace=True)
    datasetlearn1.fillna(datasetlearn1.mean(), inplace=True)
    datasetlearn1.to_csv('TrainData1.csv', index=False, header=None)
    datasetlabels1 = pandas.read_csv('TrainLabel1.txt', header=None, index_col=None)
    datasetlabels1 = numpy.ravel(datasetlabels1)
    x_train1, x_test1, y_train1, y_test1 = sklearn.model_selection.train_test_split(datasetlearn1, datasetlabels1,
                                                                                    test_size=0.20)
    # Use KNN classifier
    knn1 = sklearn.neighbors.KNeighborsClassifier()
    knn1.fit(x_train1, y_train1)
    print("Estimated accuracy for dataset 1 label prediction via KNN, 1:4 sample:")
    print(knn1.score(x_test1, y_test1))
    # Use SVM
    svm1 = sklearn.svm.SVC()
    svm1.fit(x_train1, y_train1)
    print("Estimated accuracy for dataset 1 label prediction via SVM, 1:4 sample:")
    print(svm1.score(x_test1, y_test1))
    # Use Random Forest
    rf1 = sklearn.ensemble.RandomForestClassifier()
    rf1.fit(X=x_train1, y=y_train1)
    print("Estimated accuracy for dataset 1 label prediction via Random Forest, 1:4 sample:")
    print(rf1.score(x_test1, y_test1))
    # Use Decision Tree
    dt1 = sklearn.tree.DecisionTreeClassifier()
    dt1.fit(x_train1, y_train1)
    print("Estimated accuracy for dataset 1 label prediction via DecisionTree, 1:4 sample:")
    print(dt1.score(x_test1, y_test1))

    print("After repeated testing, the chosen algorithm for this data set is KNN. Please see report for more details.")
    print("")

    # Data 2 Learning
    with open('TrainData2.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('1.00000000000000e+99', 'NaN')
    with open('TrainData2_NaN.txt', 'w') as file:
        file.write(filedata)
    # Save imputed data to file and keep in dataframe for computation
    datasetlearn2 = pandas.read_csv('TrainData2_NaN.txt', names=None, header=None, delim_whitespace=True)
    datasetlearn2.fillna(datasetlearn2.mean(), inplace=True)
    datasetlearn2.to_csv('TrainData2.csv', index=False, header=None)
    datasetlabels2 = pandas.read_csv('TrainLabel2.txt', names=None, header=None)
    datasetlabels2 = numpy.ravel(datasetlabels2)
    x_train2, x_test2, y_train2, y_test2 = sklearn.model_selection.train_test_split(datasetlearn2, datasetlabels2,
                                                                                    test_size=0.20)
    # Use KNN classifier
    knn2 = sklearn.neighbors.KNeighborsClassifier()
    knn2.fit(x_train2, y_train2)
    print("Estimated accuracy for dataset 2 label prediction via KNN, 1:4 sample:")
    print(knn2.score(x_test2, y_test2))
    # Use SVM
    svm2 = sklearn.svm.SVC()
    svm2.fit(x_train2, y_train2)
    print("Estimated accuracy for dataset 2 label prediction via SVM, 1:4 sample:")
    print(svm2.score(x_test2, y_test2))
    # Use Random Forest
    rf2 = sklearn.ensemble.RandomForestClassifier()
    rf2.fit(X=x_train2, y=y_train2)
    print("Estimated accuracy for dataset 2 label prediction via Random Forest, 1:4 sample:")
    print(rf2.score(x_test2, y_test2))
    # Use Decision Tree
    dt2 = sklearn.tree.DecisionTreeClassifier()
    dt2.fit(x_train2, y_train2)
    print("Estimated accuracy for dataset 2 label prediction via DecisionTree, 1:4 sample:")
    print(dt2.score(x_test2, y_test2))

    print("After repeated testing, the chosen algorithm for this data set is KNN. Please see report for more details.")
    print("")

    # Data 3 Learning
    with open('TrainData3.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('1.00000000000000e+99', 'NaN')
    with open('TrainData3_NaN.txt', 'w') as file:
        file.write(filedata)
    # Save imputed data to file and keep in dataframe for computation
    datasetlearn3 = pandas.read_csv('TrainData3_NaN.txt', names=None, header=None, delim_whitespace=True)
    datasetlearn3.fillna(datasetlearn3.mean(), inplace=True)
    datasetlearn3.to_csv('TrainData3.csv', index=False, header=None)
    datasetlabels3 = pandas.read_csv('TrainLabel3.txt', names=None, header=None)
    datasetlabels3 = numpy.ravel(datasetlabels3)
    x_train3, x_test3, y_train3, y_test3 = sklearn.model_selection.train_test_split(datasetlearn3, datasetlabels3,
                                                                                    test_size=0.20)
    # Use KNN classifier
    knn3 = sklearn.neighbors.KNeighborsClassifier()
    knn3.fit(x_train3, y_train3)
    print("Estimated accuracy for dataset 3 label prediction via KNN, 1:4 sample:")
    print(knn3.score(x_test3, y_test3))
    # Use SVM
    svm3 = sklearn.svm.SVC()
    svm3.fit(x_train3, y_train3)
    print("Estimated accuracy for dataset 3 label prediction via SVM, 1:4 sample:")
    print(svm3.score(x_test3, y_test3))
    # Use Random Forest
    rf3 = sklearn.ensemble.RandomForestClassifier()
    rf3.fit(X=x_train3, y=y_train3)
    print("Estimated accuracy for dataset 3 label prediction via Random Forest, 1:4 sample:")
    print(rf3.score(x_test3, y_test3))
    # Use Decision Tree
    dt3 = sklearn.tree.DecisionTreeClassifier()
    dt3.fit(x_train3, y_train3)
    print("Estimated accuracy for dataset 3 label prediction via DecisionTree, 1:4 sample:")
    print(dt3.score(x_test3, y_test3))

    print("After repeated testing, the chosen algorithm for this data set is SVM. Please see report for more details.")
    print("")

    # Data 4 Learning
    with open('TrainData4.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('1.00000000000000e+99', 'NaN')
    with open('TrainData4_NaN.txt', 'w') as file:
        file.write(filedata)
    # Save imputed data to file and keep in dataframe for computation
    datasetlearn4 = pandas.read_csv('TrainData4_NaN.txt', names=None, header=None, delim_whitespace=True)
    datasetlearn4.fillna(datasetlearn4.mean(), inplace=True)
    datasetlearn4.to_csv('TrainData4.csv', index=False, header=None)
    datasetlabels4 = pandas.read_csv('TrainLabel4.txt', names=None, header=None)
    datasetlabels4 = numpy.ravel(datasetlabels4)
    x_train4, x_test4, y_train4, y_test4 = sklearn.model_selection.train_test_split(datasetlearn4, datasetlabels4,
                                                                                    test_size=0.20)
    # Use KNN classifier
    knn4 = sklearn.neighbors.KNeighborsClassifier()
    knn4.fit(x_train4, y_train4)
    print("Estimated accuracy for dataset 4 label prediction via KNN, 1:4 sample:")
    print(knn4.score(x_test4, y_test4))
    # Use SVM
    svm4 = sklearn.svm.SVC()
    svm4.fit(x_train4, y_train4)
    print("Estimated accuracy for dataset 4 label prediction via SVM, 1:4 sample:")
    print(svm4.score(x_test4, y_test4))
    # Use Random Forest
    rf4 = sklearn.ensemble.RandomForestClassifier()
    rf4.fit(X=x_train4, y=y_train4)
    print("Estimated accuracy for dataset 4 label prediction via Random Forest, 1:4 sample:")
    print(rf4.score(x_test4, y_test4))
    # Use Decision Tree
    dt4 = sklearn.tree.DecisionTreeClassifier()
    dt4.fit(x_train4, y_train4)
    print("Estimated accuracy for dataset 4 label prediction via DecisionTree, 1:4 sample:")
    print(dt4.score(x_test4, y_test4))

    print("After repeated testing, the chosen algorithm for this data set is Random Forest. Please see report for "
          "more details.")
    print("")

    # Data 5 Learning
    with open('TrainData5.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('1.00000000000000e+99', 'NaN')
    with open('TrainData5_NaN.txt', 'w') as file:
        file.write(filedata)
    # Save imputed data to file and keep in dataframe for computation
    datasetlearn5 = pandas.read_csv('TrainData5_NaN.txt', names=None, header=None, delim_whitespace=True)
    datasetlearn5.fillna(datasetlearn5.mean(), inplace=True)
    datasetlearn5.to_csv('TrainData5.csv', index=False, header=None)
    datasetlabels5 = pandas.read_csv('TrainLabel5.txt', names=None, header=None)
    datasetlabels5 = numpy.ravel(datasetlabels5)
    x_train5, x_test5, y_train5, y_test5 = sklearn.model_selection.train_test_split(datasetlearn5, datasetlabels5,
                                                                                    test_size=0.20)
    # Use KNN classifier
    knn5 = sklearn.neighbors.KNeighborsClassifier()
    knn5.fit(x_train5, y_train5)
    print("Estimated accuracy for dataset 5 label prediction via KNN, 1:4 sample:")
    print(knn5.score(x_test5, y_test5))
    # Use SVM
    svm5 = sklearn.svm.SVC()
    svm5.fit(x_train5, y_train5)
    print("Estimated accuracy for dataset 5 label prediction via SVM, 1:4 sample:")
    print(svm5.score(x_test5, y_test5))
    # Use Random Forest
    rf5 = sklearn.ensemble.RandomForestClassifier()
    rf5.fit(X=x_train5, y=y_train5)
    print("Estimated accuracy for dataset 5 label prediction via Random Forest, 1:4 sample:")
    print(rf5.score(x_test5, y_test5))
    # Use Decision Tree
    dt5 = sklearn.tree.DecisionTreeClassifier()
    dt5.fit(x_train5, y_train5)
    print("Estimated accuracy for dataset 5 label prediction via DecisionTree, 1:4 sample:")
    print(dt5.score(x_test5, y_test5))

    print("After repeated testing, the chosen algorithm for this data set is Random Forest. Please see report for "
          "more details.")
    print("")

    # Testing Data
    # Test set 1
    with open('TestData1.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('1.00000000000000e+99', 'NaN')
    with open('TestData1_NaN.txt', 'w') as file:
        file.write(filedata)
    # Save imputed data to file and keep in dataframe for computation
    datasettest1 = pandas.read_csv('TestData1_NaN.txt', names=None, header=None, delim_whitespace=True)
    datasettest1.fillna(datasettest1.mean(), inplace=True)
    datasettest1.to_csv('TestData1.csv')
    # Re-fit with entire learning data set
    knn1.fit(datasetlearn1, datasetlabels1)
    predictions1 = knn1.predict(datasettest1)
    results1 = open('TestLabel1.txt', 'w')
    for eaLine in predictions1:
        results1.write("%s\n" % eaLine)

    # Test set 2
    with open('TestData2.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('1.00000000000000e+99', 'NaN')
    with open('TestData2_NaN.txt', 'w') as file:
        file.write(filedata)
    # Save imputed data to file and keep in dataframe for computation
    datasettest2 = pandas.read_csv('TestData2_NaN.txt', names=None, header=None, delim_whitespace=True)
    datasettest2.fillna(datasettest2.mean(), inplace=True)
    datasettest2.to_csv('TestData2.csv', index=None, header=None)
    # Re-fit with entire learning data set
    knn2.fit(datasetlearn2, datasetlabels2)
    predictions2 = knn2.predict(datasettest2)
    results2 = open('TestLabel2.txt', 'w')
    for eaLine in predictions2:
        results2.write("%s\n" % eaLine)

    # Test set 3
    with open('TestData3.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('1.00000000000000e+99', 'NaN')
    with open('TestData3_NaN.txt', 'w') as file:
        file.write(filedata)
    # Save imputed data to file and keep in dataframe for computation
    datasettest3 = pandas.read_csv('TestData3_NaN.txt', names=None, header=None)
    datasettest3.fillna(datasettest3.mean(), inplace=True)
    datasettest3.to_csv('TestData3.csv', index=None, header=None)
    # Re-fit with entire learning data set
    svm3.fit(datasetlearn3, datasetlabels3)
    predictions3 = svm3.predict(datasettest3)
    results3 = open('TestLabel3.txt', 'w')
    for eaLine in predictions3:
        results3.write("%s\n" % eaLine)

    # Test set 4
    txt_file34 = r"TestData4.txt"
    csv_file34 = r"TestData4_noNaN.csv"
    in_txt34 = csv.reader(open(txt_file34, "rt"), delimiter='\t')
    out_csv34 = csv.writer(open(csv_file34, 'wt'))
    out_csv34.writerows(in_txt34)
    with open("TestData4_noNaN.csv", "rt") as fin:
        with open("TestData4.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    # Save imputed data to file and keep in dataframe for computation
    datasettest4 = pandas.read_csv('TestData4.csv', names=None, header=None, delim_whitespace=True)
    datasettest4.fillna(datasettest4.mean(), inplace=True)
    datasettest4.to_csv('TestData4.csv', index=None, header=None)
    # Re-fit with entire learning data set
    rf4.fit(datasetlearn4, datasetlabels4)
    predictions4 = rf4.predict(datasettest4)
    results4 = open('TestLabel4.txt', 'w')
    for eaLine in predictions4:
        results4.write("%s\n" % eaLine)

    # Test set 5
    txt_file35 = r"TestData5.txt"
    csv_file35 = r"TestData5_noNaN.csv"
    in_txt35 = csv.reader(open(txt_file35, "rt"), delimiter='\t')
    out_csv35 = csv.writer(open(csv_file35, 'wt'))
    out_csv35.writerows(in_txt35)
    with open("TestData5_noNaN.csv", "rt") as fin:
        with open("TestData5.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    # Save imputed data to file and keep in dataframe for computation
    datasettest5 = pandas.read_csv('TestData5.csv', names=None, header=None, delim_whitespace=True)
    datasettest5.fillna(datasettest5.mean(), inplace=True)
    datasettest5.to_csv('TestData5.csv', index=None, header=None)
    # Re-fit with entire learning data set
    rf5.fit(datasetlearn5, datasetlabels5)
    predictions5 = rf5.predict(datasettest5)
    results5 = open('TestLabel5.txt', 'w')
    for eaLine in predictions5:
        results5.write("%s\n" % eaLine)


main()
