#include <iostream>
#include "Complex.h"

using namespace std;

int main()
{
    double x(0.), y(0.);
    Complex ts(x,y);
    cin >> x >> y;
    ts = Complex(x,y);
    ts = ts * 2;
    ts.displayCom();
    return 0;
}