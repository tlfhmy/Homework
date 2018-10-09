#include "Complex.h"

Complex Complex::rootUnit(int n, int k) {
    if(k == 0)
        return Complex(1.);
    double phi = 2. * M_PI / (double) n;
    return Complex(cos(phi * k), sin(phi * k));
}

Complex Complex::root(int n, int k) const {
    double  phi = arg();
    double alpha = phi / (double) n;
    double r = pow(mod(), 1. / (double) n);

    Complex z = Complex::expForm(r, alpha);

    return z * Complex::rootUnit(n, k);
}