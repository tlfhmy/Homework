#ifndef COMPLEX_H
#define COMPLEX_H

#include <iostream>
#include <cmath>

class Complex{
public:
    double re;
    double im;
public:
    Complex():re(0.), im(0.) {}
    Complex(double r, double i = 0.): re(r), im(i) {}
    Complex(const Complex &z): re(z.re), im(z.im) {}

    ~Complex() {}

    Complex& operator= (const Complex &tm) {
        this->re = tm.re;
        this->im = tm.im;
        return *this;
    }

    Complex operator+ (const Complex &tm) const {
        return Complex(this->re + tm.re, this->im + tm.im);
    }

    Complex operator- (const Complex &tm) const {
        return Complex(this->re - tm.re, this->im - tm.im);
    }

    Complex operator* (const Complex &tm) const {
        return Complex(this->re * tm.re - this->im * tm.im,
                        this->re * tm.im + this->im * tm.re);
    }

     Complex operator/ (const Complex &tm) const {
        return Complex((re*tm.re + im*tm.im)/(tm.re*tm.re + tm.im*tm.im),(-re*tm.im + im*tm.re)/(tm.re*tm.re + tm.im*tm.im));
    }

    /*std::iostream operator<<(std::iostream out,Complex &mp)
    {
        out << tmp.re << " + " << tm.im << "i";
    }*/


    /*Complex operator* (const double tm) {
        return Complex(this->re * tm, this->im * tm);
    }*/

    Complex& operator+= (const Complex &tm) {
        this->re += tm.re;
        this->im += tm.im;
        return *this;
    }

    Complex& operator*= (const Complex &tm) {
        this->re = this->re * tm.re - this->im * tm.im;
        this->im = this->re * tm.im + this->im * tm.re;
        return *this;
    }

    double mod() const {
        return sqrt(re*re + im*im);
    }

    double arg() const {
        return atan2(im, re);
    }

    static Complex rootUnit(int n, int k);

    Complex root(int n, int k) const;

    static Complex expForm(double r, double phi) {
        return Complex(r*cos(phi), r*sin(phi));
    }

    void displayCom() {
        std::cout << this->re << " + " << this->im << "i" << std::endl;
    }
};

#endif