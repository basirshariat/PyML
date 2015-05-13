%module pegasos
%{
#include "Pegasos.h"
%}
/* %include "Pegasos.h" */
%import std_vector.i

extern std::vector<double> runPegasos(DataSet * data, double lambda, int T);

