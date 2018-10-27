#include "Matrix.h"
#include "Matrix.cpp"
#include <stdexcept>
#include <iostream>
using namespace std;

void menu3()
{
    cout << "       **********    Matrix Calc    **********" << endl;
    cout << "       *                                     *" << endl;
    cout << "       *               a. A + B              *" << endl;
    cout << "       *               b. A - B              *" << endl;
    cout << "       *               c. A * B              *" << endl;
    cout << "       *                                     *" << endl;
    cout << "       ***************************************" << endl;
}

void menu1()
{
    cout << "       **********    Matrix Calc    **********" << endl;
    cout << "       *                                     *" << endl;
    cout << "       *        a. Monadic Operation         *" << endl;
    cout << "       *        b. Binary  Operation         *" << endl;
    cout << "       *                                     *" << endl;
    cout << "       ***************************************" << endl;
}

void menu2()
{
    cout << "       **********    Matrix Calc    **********" << endl;
    cout << "       *                                     *" << endl;
    cout << "       *      a. Transpose of Matrix         *" << endl;
    cout << "       *      b. Inverse Matrix              *" << endl;
    cout << "       *      c. Determinat of Matrix        *" << endl;
    cout << "       *      d. Triangular Matrix           *" << endl;
    cout << "       *      e. Solve LinearSys             *" << endl;
    cout << "       *                                     *" << endl;
    cout << "       ***************************************" << endl;
}

int main()
{
    menu1();

    Matrix A(1, 1);
    Matrix B(1, 1);
    int m(0), n(0);
    double *p = nullptr;

    char selec1(0);
    char selec2(0);
    cin >> selec1;

    switch (selec1)
    {
    case 'a':
        cout << "Please Enter rows and columns of Matrix." << endl;
        cin >> m >> n;
        cout << "Please Enter elements of Matrix." << endl;
        p = new double[m * n];
        for (int i = 0; i < m * n; i++)
        {
            cin >> p[i];
        }
        cin.clear();
        A = Matrix(m, n);
        A.input(p);
        delete[] p;
        break;
    case 'b':
        cout << "Please Enter rows and columns of Matrix A." << endl;
        cin >> m >> n;
        cout << "Please Enter elements of A." << endl;
        p = new double[m * n];
        for (int i = 0; i < m * n; i++)
        {
            cin >> p[i];
        }
        cin.clear();
        A = Matrix(m, n);
        A.input(p);
        delete[] p;

        cout << "Please Enter rows and columns of Matrix B." << endl;
        cin >> m >> n;
        cout << "Please Enter elements of B." << endl;
        p = new double[m * n];
        for (int i = 0; i < m * n; i++)
        {
            cin >> p[i];
        }
        cin.clear();
        B = Matrix(m, n);
        B.input(p);
        delete[] p;
        break;
    default:
        cout << "Invalid Param!" << endl;
        return 0;
    }

    if(selec1 == 'a')
        menu2();
    else
        menu3();

    try
    {
        while (true)
        {
            switch (selec1)
            {
            case 'a':
                cin >> selec2;
                switch (selec2)
                {
                case 'a':
                    menu2();
                    A.Transp().display();
                    break;
                case 'b':
                    menu2();
                    A.Inverse().display();
                    break;
                case 'c':
                    menu2();
                    cout << "This function has not accomplished." << endl;
                    break;
                case 'd':
                    menu2();
                    A.TriangMat().display();
                    break;
                case 'e':
                    menu2();
                    cout << "This function has not accomplished." << endl;
                    break;
                default:
                    cout << "Invalid Param!" << endl;
                    return 0;
                }
                break;
            case 'b':
                cin >> selec2;
                switch (selec2)
                {
                case 'a':
                    menu3();
                    (A + B).display();
                    break;
                case 'b':
                    menu3();
                    (A - B).display();
                    break;
                case 'c':
                    menu3();
                    (A * B).display();
                    break;
                default:
                    cout << "Invalid Param!" << endl;
                    return 0;
                }
                break;
            default:
                cout << "Invalid Param!" << endl;
                return 0;
            }
        }
    }
    catch (domain_error &e)
    {
        cout << "Error! Reason: \n"
             << e.what() << endl;
    }

    return 0;
}