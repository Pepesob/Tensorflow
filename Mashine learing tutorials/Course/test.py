import pandas
import numpy
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


data = pandas.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]



