#include <iostream>
#include <cmath>

using namespace std;

double logud(double, double, double);

int main()
{
    cout << "Please enter two numbers." << endl;

    double a(0.), b(0.);

    cin >> a >> b;

    cout << "logud(" << a << ", " << b << ") = " << logud(a, b, 10e-8) << endl;
    return 0;
}

double logud(double a, double y, double esp = 10e-8)
{
    double x = 0.;
    double z = y;
    double t = 1.;

    while (z < 1. / a || z > a || fabs(t) > esp)
    {
        if (z < 1. / a)
        {
            z *= a;
            x -= t;
        }
        else if (z > a)
        {
            z /= a;
            x += t;
        }
        else
        {
            z *= z;
            t /= 2;
        }
    }

    return x;
}