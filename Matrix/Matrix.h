#ifndef MATRIX_H
#define MATRIX_H

class Matrix{
private:
    int m;
    int n;
    double *a;
public:
    Matrix(): m(1), n(1), a(new double[1]) {}

    Matrix(int r, int c): m(r), n(c), a(new double[m*n]) {
        for(int i = 0; i < m*n; i++){
            a[i] = 0.;
        }
    }

    Matrix(const Matrix &b): m(b.m), n(b.n), a(new double[m*n]) {
        for(int i = 0; i < m*n; i++) {
            a[i] = b.a[i];
        }
    }

    ~Matrix(){
        delete[] a;
    }

    Matrix & operator= (const Matrix &b) {
        if(m*n < b.m * b.n) {
            delete[] a;
            a = new double [b.m * b.n];
        }

        m = b.m;
        n = b.n;

        for(int i = 0; i < m*n; i++){
            a[i] = b.a[i];
        }
        return *this;
    }

    int rows() const {
        return m;
    }

    int columns() const {
        return n;
    }

<<<<<<< HEAD
    double at(int i, int j) {
        return a[i*n + j];
    }

    Matrix & operator* (const double &z) {
        Matrix tm;
        tm.m = m;
        tm.n = n;
        tm.a = new double[m*n];

        for(int i = 0; i < m*n; i++){
            tm.a[i] = a[i] * z;
        }

        return tm;
    }

    Matrix & operator+ (const Matrix & z) {
        if(m != z.m || n != z.n){
            std::cout << "They are of diffrent form! Can not plus." << std::endl;
            return NULL;
        }
        esle{
            Matrix tm;
            tm.m = m;
            tm.n = n;
            tm.a = new double [m * n];

            for(int i = 0; i < m*n; i++) {
                tm.a[i] = a[i] + z.a[i];
            }
        }

        return tm;
    }
=======
    
>>>>>>> parent of 0319cc8... Make some operators function
};



#endif