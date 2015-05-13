#include "Pegasos.h"
#include <algorithm>


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
    int indices[size()];
    for (int i=0; i<size(); i++)
        indices[i] = i;

    random_shuffle(&indices[0], &indices[size()-1]);
    int counter = 0;
    for (int t=1; t<=T ; t++)
    {
        if (counter==size())
        {
            counter=0;
            random_shuffle(&indices[0], &indices[size()-1]);
        }

        double lambda_t = the_lambda * t;
//        int i = rand() % size();
        int i = indices[counter];
        counter++;
        double sigma = 0;
        double K_ij = 0;
        for (int j=0; j<size(); j++)
        {
            K_ij = data->kernel->eval(data, i, j, data);
            sigma += alpha[j] * K_ij * (double)(Y[j] * Y[i])* 2;
        }
        if (sigma/lambda_t < 1)
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
