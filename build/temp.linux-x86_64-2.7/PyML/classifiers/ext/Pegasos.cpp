#include "Pegasos.h"


Pegasos::Pegasos(DataSet *_data, double _lambda, int _T):
    data(_data),
    the_lambda(_lambda),
    T(_T)
{
    Y.resize(size());
    alpha.resize(size());
    for (int i = 0; i < size(); i++)
    {
        Y[i] = data->Y[i] * 2.0 - 1.0;
        alpha[i] = 0;
    }
}

Pegasos::~Pegasos()
{
  //delete data;
}

void Pegasos::optimize()
{
    for (int t=1; t<=T ; t++)
    {
        double lambda_t = the_lambda * t;
        int i = rand() % size();
        double temp = 0;
        for (int j=0 ; j<size() ; j++)
        {
            if (i==j) continue;
            double K_ij = data->kernel->eval(data, i, j, data);
            temp += alpha[j] * K_ij * Y[i];
        }
        if ((Y[i]/lambda_t)*temp < 1)
            alpha[i] += 1;
    }
}

void Pegasos::show() {
    std::cout << "b: " << b << std::endl;
    std::cout << "alpha:" << std::endl;
    for (int i = 0; i < data->size(); i++) {
    std::cout << alpha[i] << " " << std::endl;
    }
    std::cout << std::endl;

}

std::vector<double> Pegasos::get_alpha()
{
    return alpha;
}

std::vector<double> runPegasos(DataSet * data, double lambda, int T)
{
    Pegasos p(data, lambda, T);
    p.optimize();
    return p.get_alpha();
}
