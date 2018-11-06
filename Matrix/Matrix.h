#ifndef MATRIX_H
#define MATRIX_H

#include <iostream>
#include <cmath>
const double Esp = 1e-8;
class Matrix
{
  private:
    int m;
    int n;
    double *a;

  public:
    Matrix() : m(1), n(1), a(new double[1]) {}

    Matrix(int r, int c) : m(r), n(c), a(new double[m * n])
    {
        for (int i = 0; i < m * n; i++)
        {
            a[i] = 0.;
        }
    }

    Matrix(const Matrix &b) : m(b.m), n(b.n), a(new double[m * n])
    {
        for (int i = 0; i < m * n; i++)
        {
            a[i] = b.a[i];
        }
    }

    ~Matrix()
    {
        delete[] a;
    }

    Matrix &operator=(const Matrix &b)
    {
        if (m * n < b.m * b.n)
        {
            delete[] a;
            a = new double[b.m * b.n];
        }

        m = b.m;
        n = b.n;

        for (int i = 0; i < m * n; i++)
        {
            a[i] = b.a[i];
        }
        return *this;
    }

    int rows() const
    {
        return m;
    }

    int columns() const
    {
        return n;
    }

    bool empty() const
    {
        return (m == 0 || n == 0);
    }

    double at(int i, int j) const
    {
        if (i < 0 || j < 0 || i > m || j > n)
        {
            throw std::range_error("Element which you want to access does NOT EXIST!!");
        }
        return a[i * n + j];
    };

    void input(const double *el)
    {
        for (int i = 0; i < m * n; i++)
        {
            a[i] = el[i];
        }
    }

    void display() const
    {
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                double tmp = at(i, j);
                if (fabs(tmp) < Esp)
                {
                    std::cout << "\t" << 0.0 << " ";
                }
                else
                {
                    std::cout <<"\t" << tmp << " ";
                }
            }
            std::cout << std::endl;
        }
    }

    Matrix operator*(const double &z) const;
    Matrix operator*(const Matrix &rm) const;

    Matrix operator+(const Matrix &z) const;
    Matrix operator-(const Matrix &z) const;

    Matrix Transp() const;
    Matrix Inverse() const;

    Matrix TriangMat() const;
    double Det() const;
};
#endif