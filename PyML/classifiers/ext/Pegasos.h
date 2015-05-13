#ifndef PEGASOS_H
#define PEGASOS_H

#include "../../containers/ext/DataSet.h"
#include "../../containers/ext/Kernel.h"

#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>

/*
    This class implements the SVM solver algorithm described in
    Shalev-Shwartz, Shai, et al. "Pegasos: Primal estimated sub-gradient solver for svm."
     Mathematical programming 127.1 (2011): 3-30.

*/
class Pegasos {
public:
    void optimize();
    Pegasos(DataSet *_data, double _lambda, int _T);
    ~Pegasos();
    std::vector<double> get_alpha();
    void show();
private:
    DataSet *data;
    std::vector<double> Y;
    std::vector<double> alpha;
    double the_lambda;
    double b;
    double T;
    int size() { return data->size(); }
};

std::vector<double> runPegasos(DataSet *data, double _the_lambda, int T);

#endif
