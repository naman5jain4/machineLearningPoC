import csv
import pandas
import numpy
import sklearn


def main():
    # Training Data
    txt_file21 = r"TrainData1.txt"
    csv_file21 = r"TrainData1_noNaN.csv"
    in_txt21 = csv.reader(open(txt_file21, "rt"), delimiter='\t')
    out_csv21 = csv.writer(open(csv_file21, 'wt'))
    out_csv21.writerows(in_txt21)
    with open("TrainData1_noNaN.csv", "rt") as fin:
        with open("TrainData1.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TrainData1.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TrainData1.csv')

    txt_file22 = r"TrainData2.txt"
    csv_file22 = r"TrainData2_noNaN.csv"
    in_txt22 = csv.reader(open(txt_file22, "rt"), delimiter='\t')
    out_csv22 = csv.writer(open(csv_file22, 'wt'))
    out_csv22.writerows(in_txt22)
    with open("TrainData2_noNaN.csv", "rt") as fin:
        with open("TrainData2.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TrainData2.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TrainData2.csv')

    txt_file23 = r"TrainData3.txt"
    csv_file23 = r"TrainData3_noNaN.csv"
    in_txt23 = csv.reader(open(txt_file23, "rt"), delimiter='\t')
    out_csv23 = csv.writer(open(csv_file23, 'wt'))
    out_csv23.writerows(in_txt23)
    with open("TrainData3_noNaN.csv", "rt") as fin:
        with open("TrainData3.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TrainData3.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TrainData3.csv')

    txt_file24 = r"TrainData4.txt"
    csv_file24 = r"TrainData4_noNaN.csv"
    in_txt24 = csv.reader(open(txt_file24, "rt"), delimiter='\t')
    out_csv24 = csv.writer(open(csv_file24, 'wt'))
    out_csv24.writerows(in_txt24)
    with open("TrainData4_noNaN.csv", "rt") as fin:
        with open("TrainData4.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TrainData4.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TrainData4.csv')

    txt_file25 = r"TrainData5.txt"
    csv_file25 = r"TrainData5_noNaN.csv"
    in_txt25 = csv.reader(open(txt_file25, "rt"), delimiter='\t')
    out_csv25 = csv.writer(open(csv_file25, 'wt'))
    out_csv25.writerows(in_txt25)
    with open("TrainData5_noNaN.csv", "rt") as fin:
        with open("TrainData5.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TrainData5.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TrainData5.csv')

    txt_file26 = r"TrainData6.txt"
    csv_file26 = r"TrainData6_noNaN.csv"
    in_txt26 = csv.reader(open(txt_file26, "rt"), delimiter='\t')
    out_csv26 = csv.writer(open(csv_file26, 'wt'))
    out_csv26.writerows(in_txt26)
    with open("TrainData6_noNaN.csv", "rt") as fin:
        with open("TrainData6.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TrainData6.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TrainData6.csv')

    # Testing Data
    txt_file31 = r"TestData1.txt"
    csv_file31 = r"TestData1_noNaN.csv"
    in_txt31 = csv.reader(open(txt_file31, "rt"), delimiter='\t')
    out_csv31 = csv.writer(open(csv_file31, 'wt'))
    out_csv31.writerows(in_txt31)
    with open("TestData1_noNaN.csv", "rt") as fin:
        with open("TestData1.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TestData1.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TestData1.csv')

    txt_file32 = r"TestData2.txt"
    csv_file32 = r"TestData2_noNaN.csv"
    in_txt32 = csv.reader(open(txt_file32, "rt"), delimiter='\t')
    out_csv32 = csv.writer(open(csv_file32, 'wt'))
    out_csv32.writerows(in_txt32)
    with open("TestData2_noNaN.csv", "rt") as fin:
        with open("TestData2.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TestData2.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TestData2.csv')

    txt_file33 = r"TestData3.txt"
    csv_file33 = r"TestData3_noNaN.csv"
    in_txt33 = csv.reader(open(txt_file33, "rt"), delimiter='\t')
    out_csv33 = csv.writer(open(csv_file33, 'wt'))
    out_csv33.writerows(in_txt33)
    with open("TestData3_noNaN.csv", "rt") as fin:
        with open("TestData3.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TestData3.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TestData3.csv')

    txt_file34 = r"TestData4.txt"
    csv_file34 = r"TestData4_noNaN.csv"
    in_txt34 = csv.reader(open(txt_file34, "rt"), delimiter='\t')
    out_csv34 = csv.writer(open(csv_file34, 'wt'))
    out_csv34.writerows(in_txt34)
    with open("TestData4_noNaN.csv", "rt") as fin:
        with open("TestData4.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TestData4.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TestData4.csv')

    txt_file35 = r"TestData5.txt"
    csv_file35 = r"TestData5_noNaN.csv"
    in_txt35 = csv.reader(open(txt_file35, "rt"), delimiter='\t')
    out_csv35 = csv.writer(open(csv_file35, 'wt'))
    out_csv35.writerows(in_txt35)
    with open("TestData5_noNaN.csv", "rt") as fin:
        with open("TestData5.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TestData5.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TestData5.csv')

    txt_file36 = r"TestData6.txt"
    csv_file36 = r"TestData6_noNaN.csv"
    in_txt36 = csv.reader(open(txt_file36, "rt"), delimiter='\t')
    out_csv36 = csv.writer(open(csv_file36, 'wt'))
    out_csv36.writerows(in_txt36)
    with open("TestData6_noNaN.csv", "rt") as fin:
        with open("TestData6.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace('1.00000000000000e+99', 'NaN'))
    dataset = pandas.read_csv('TestData6.csv')
    dataset.fillna(dataset.mean(), inplace=True)
    dataset.to_csv('TestData6.csv')


main()
