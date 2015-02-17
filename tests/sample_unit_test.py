from build.lib.PyML.classifiers.svm import SVM
from build.lib.PyML.containers.vectorDatasets import SparseDataSet

__author__ = 'basir'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


def main():
    data = SparseDataSet('../data/heartSparse.data', labelsColumn=-1)
    svm = SVM()
    res = svm.cv(data, 5)
    print res


if __name__ == '__main__':
# unittest.main()
    main()
