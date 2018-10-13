#include <iostream>

using namespace std;

int pwr(int, int, int &);
int pwrc(int, int, int &);

int main()
{
    int a(0), b(0);
    int t1(0), t2(0);
    cout << "Please Enter two numbers." << endl;

    cin >> a >> b;

    cout << "pow(" << a << ", " << b << ") = " << pwr(a, b, t1) << endl;
    cout << "powc(" << a << ", " << b << ") = " << pwrc(a, b, t2) << endl;

    cout << "pow uses " << t1 << " times prod" << endl;
    cout << "powc uses " << t2 << " times prod" << endl;
    return 0;
}

int pwr(int a, int n, int &tm)
{
    tm = 0;
    int k = n;
    int p = 1;
    int b = a;
    while (k != 0)
    {
        if (k % 2 == 0)
        {
            k /= 2;
            tm++;
            b *= b;
            tm++;
        }
        else
        {
            k -= 1;
            p *= b;
            tm++;
        }
    }
    return p;
}

int pwrc(int a, int n, int &tm)
{
    int p = 1;
    int k = n;
    while (k != 0)
    {
        p *= a;
        tm++;
        k--;
    }
    return p;
}