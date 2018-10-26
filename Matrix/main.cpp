#include "Matrix.h"
#include "Matrix.cpp"
using namespace std;

int main()
{

    int m(0),n(0);
    cout << "Please enter number of rows and columns: ";
    cin >> m >> n;
    cout << endl;

    double* p = new double[m*n];
    for(int r = 0; r < m*n; r++)
    {
        cin >> p[r];
    }

      /*double p[] =  {1.,2.,3.,
        4.,7.,2.,
        6.,3.,8.};*/

    Matrix tst(m,n);
    tst.input(p);
    Matrix sm = tst;

    cout << "Now, we display the original matrix." << endl;
    tst.display();

    cout << "Transpose Matrix of this Matrix." << endl;
    Matrix tst1 = tst.TriangMat();
    //tst1.display();
    tst.Transp().display();

    cout << "TrangleMat of this Matrix." << endl;
    tst.TriangMat().display();

    cout << "Reverse of this Matrix." << endl;
    tst.Reverse().display();

    /*cout << "Half" << endl;
    tst.HalfReverse(sm).display();*/

    cout << "Test reverse of this Matrix." << endl;
    Matrix pro(m,n);
    pro = tst * (tst.Reverse());
    pro.display();
    
    return 0;
}