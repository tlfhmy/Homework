#include <iostream>

using namespace std;

int gcdext(int x, int y, int &u, int &v);

int main()
{
    cout << "Please enter two numbers." << endl;

    int x(0), y(0), u(0), v(0);

    cin >> x >> y;

    cout << gcdext(x, y, u, v) << " = " << x << "*"
         << "(" << u << ")"
         << " + " << y << "*"
         << "(" << v << ")" << endl;

    return 0;
}

int gcdext(int x, int y, int &u, int &v)
{
    int a = x;
    int b = y;

    int u1 = 1, u2 = 0;
    int v1 = 0, v2 = 1;

    int q = a/b;
    int r = a%b;

    
}