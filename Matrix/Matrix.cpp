#include "Matrix.h"
#include <stdexcept>

Matrix Matrix::Transp() const
{
    Matrix z(n, m);
    for (int i = 0; i < z.m; i++)
    {
        for (int j = 0; j < z.n; j++)
        {
            z.a[i * z.n + j] = this->at(j, i);
        }
    }
    return z;
}

Matrix &Matrix::operator*(const Matrix &tm) const
{
    Matrix z(this->m, tm.n);
    Matrix trtm = tm.Transp();
    if (this->n != tm.m)
    {
        throw std::domain_error("These two matrixes are not matched!.");
    }
    else if (this->empty() || tm.empty())
    {
        throw std::domain_error("Some matrix(es) are empty!");
    }
    else
    {
        for (int i = 0; i < z.m; i++)
        {
            for (int j = 0; j < z.n; j++)
            {
                double vesu(0.);
                for (int k = 0; k < this->n; k++)
                {
                    vesu += this->at(i, k) * trtm.at(j, k);
                }
                z.a[i * n + j] = vesu;
            }
        }
    }
    return z;
}

Matrix &Matrix::operator*(const double &z) const
{
    Matrix p(m, n);
    for (int i = 0; i < m * n; i++)
    {
        p.a[i] = a[i] * z;
    }
    return p;
}

Matrix &Matrix::operator+(const Matrix &tm) const
{
    Matrix z(this->m, this->n);
    if (this->m != tm.m || this->n != tm.n)
    {
        throw std::domain_error("Those two matrixes are not suitbal for Adding!");
    }
    else if (this->empty() || tm.empty())
    {
        throw std::domain_error("Some matrix is EMPTY!");
    }
    else
    {
        for (int i = 0; i < m * n; i++)
        {
            z.a[i] = this->a[i] + tm.a[i];
        }
    }
    return z;
}

Matrix &Matrix::operator-(const Matrix &tm) const
{
    Matrix z(this->m, this->n);
    if (this->m != tm.m || this->n != tm.n)
    {
        throw std::domain_error("Those two matrixes are not suitbal for Substract!");
    }
    else if (this->empty() || tm.empty())
    {
        throw std::domain_error("Some matrix is EMPTY!");
    }
    else
    {
        for (int i = 0; i < m * n; i++)
        {
            z.a[i] = this->a[i] - tm.a[i];
        }
    }
    return z;
}

Matrix Matrix::TriangMat() const
{
    Matrix tm = *this;
    for (int i = 0; i < m; i++)
    {
        bool fst_0 = false;
        int ftnz = -1;
        if (tm.at(i, i) == 0.)
        {
            fst_0 = true;
        }
        if (fst_0)
        {
            for (int r = 0; r < n; r++)
            {
                if (tm.at(i, r) != 0)
                {
                    ftnz = r;
                    break;
                }
            }
        }
        if (ftnz != -1)
        {
            for (int r = 0; r < m; r++)
            {
                tm.a[r * n + i] += tm.at(r, ftnz);
            }
        }
        else if (fst_0)
        {
            continue;
        }
        double basor(0.0);
        basor = tm.at(i, i);
        for (int j = i + 1; j < n; j++)
        {
            double basdy(0.0);
            basdy = tm.at(j, i);
            basdy = basdy / basor;
            for (int k = i; k < m; k++)
            {
                tm.a[j * n + k] -= basdy * tm.at(i, k);
            }
        }
    }
    return tm;
}

Matrix Matrix::Reverse() const
{
    Matrix tm = *this;
    Matrix unit(m,n);
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j)
            {
                unit.a[i * n + j] = 1.;
            }
            else
            {
                unit.a[i * n + j] = 0.;
            }
        }
    }
    if (m != n)
    {
        throw std::domain_error("Just able to find Reverse Matrix from Square Matrix!");
    }
    else if (tm.empty())
    {
        throw std::domain_error("Empty matrix without Reverse!");
    }
    else
    {
        for (int i = 0; i < m; i++)
        {
            bool fst_0 = false;
            int ftnz = -1;
            if (tm.at(i, i) == 0.)
            {
                fst_0 = true;
            }
            if (fst_0)
            {
                for (int r = 0; r < n; r++)
                {
                    if (tm.at(i, r) != 0)
                    {
                        ftnz = r;
                        break;
                    }
                }
            }
            if (ftnz != -1)
            {
                for (int r = 0; r < m; r++)
                {
                    tm.a[r * n + i] += tm.at(r, ftnz);
                    unit.a[r * n + i] += unit.at(r, ftnz);
                }
            }
            else if (fst_0)
            {
                continue;
            }
            double basor(0.0);
            basor = tm.at(i, i);
            for (int j = i + 1; j < n; j++)
            {
                double basdy(0.0);
                basdy = tm.at(j, i);
                basdy = basdy / basor;
                for (int k = 0; k < m; k++)
                {
                    tm.a[j * n + k] -= basdy * tm.at(i, k);
                    unit.a[j * n + k] -= basdy * unit.at(i, k);
                }
            }
        }
        for(int j = n-1; j > 0; j--)
        {
            for(int i = 0; i < j; i++)
            {
                double el = tm.at(i,j)/tm.at(j,j);
                for(int k = 0; k<m; k++)
                {
                    tm.a[i*n+k] -= el*tm.at(j,k);
                    unit.a[i*n+k] -= el*unit.at(j,k);
                }
            }
        }
        for(int i = 0; i < m; i++)
        {
            double el = tm.at(i,i);
            for(int j = 0; j < n; j++)
            {
                tm.a[i*n+j] /= el;
                unit.a[i*n+j] /= el;
            }
        }
    }
    return unit;
}