import random
from PyML.classifiers import multi
from PyML.classifiers.svm import SVM
import numpy as np
from PyML.containers.vectorDatasets import SparseDataSet, VectorDataSet

__author__ = 'basir'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


def main():
    data = SparseDataSet('../../data/heartSparse.data', labelsColumn=-1)
    # data = SparseDataSet('../../data/heart.data', lab)
    # data = SparseDataSet('../../data/iris.data', labelsColumn=-1)
    data.attachKernel('gaussian', gamma=0.5)
    # data.addKernel
    # data.attachKernel('gaussian', gamma=0.5, normalization='cosine')
    n = len(data)
    n_training = 50
    # svm = SVM()
    svm = SVM(optimizer='pegasos')
    # svm = SVM(optimizer='mysmo')
    # random.seed(1000)
    # training_indices = list(random.sample(range(0, n), n_training))
    # training_indices.sort()
    # testing_indices = list(set(range(0, n)) - set(training_indices))
    # testing_indices.sort()
    # res = svm.trainTest(data, trainingPatterns=training_indices, testingPatterns=testing_indices)
    # mc = multi.OneAgainstRest(svm)
    # res = mc.cv(data, 5)
    res = svm.cv(data, 5)
    print res


if __name__ == '__main__':
    # unittest.main()
    main()
