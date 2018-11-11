#include "Stack.h"
#include <iostream>
#include <math.h>
#include <string>
#include <sstream>
#include <stdexcept>

using namespace std;

static void onAdd();
static void onSub();
static void onMul();
static void onDiv();
static void onMod();
static void onPush(string);
static void onPop();
static void onDup();
static void onExch();
static void onClear();
static void display();
static void printHelp();
static void onShow();
static void onSin();
static void onCos();
static void onTan();
static void onArcsin();
static void onArccos();
static void onArctan();
static void onLn();
static void onLog();
static void onLogxy();
static void onExp();
static void onXpy();

static Stack<double> stack;

int main()
{
    printHelp();

    string line;

    while (cin >> line)
    {
        int linstr = line.length();
        try
        {
            if (line == "+")
                onAdd();
            else if (line == "-")
                onSub();
            else if (line == "*")
                onMul();
            else if (line == "/")
                onDiv();
            else if (line == "%")
                onMod();
            else if (line == "sin")
                onSin();
            else if (line == "cos")
                onCos();
            else if (line == "tan")
                onTan();
            else if (line == "arcsin")
                onArcsin();
            else if (line == "arccos")
                onArccos();
            else if (line == "arctan")
                onArctan();
            else if (line == "ln")
                onLn();
            else if (line == "log")
                onLog();
            else if (line == "logxy")
                onLogxy();
            else if (line == "exp")
                onExp();
            else if (line == "xpy")
                onXpy();
            else if (line == "=")
                display();
            else if ((line.length() > 0 && isdigit(line[0])) ||
                     (((line.length() > 1 && (line[0] == '-') || line[0] == '+')) &&
                         isdigit(line[1])))
                onPush(line);
            else if (line == "pop")
                onPop();
            else if (line == "dup")
                onDup();
            else if (line == "exch")
                onExch();
            else if (line == "clear")
                onClear();
            else if (line == "show")
                onShow();
            else if (
                line == "" ||
                ((line.length() > 0 && (line[0] == 'q' || line[0] == 'Q'))))
                break;
            else
                printHelp();
        }
        catch (runtime_error &e)
        {
            cout << e.what() << endl;
        }
        catch (out_of_range &e)
        {
            cout << e.what() << endl;
        }
    }

    return 0;
}

static void onAdd()
{
    double y = stack.pop();
    double x = stack.pop();
    stack.push(x + y);
    display();
}

static void onSub()
{
    double y = stack.pop();
    double x = stack.pop();
    stack.push(x - y);
    display();
}

static void onMul()
{
    double y = stack.pop();
    double x = stack.pop();
    stack.push(x * y);
    display();
}

static void onDiv()
{
    double y = stack.pop();
    double x = stack.pop();
    stack.push(x / y);
    display();
}

static void onMod()
{
    double y = stack.pop();
    double x = stack.pop();
    stack.push(fmod(x, y));
    display();
}

static void onPush(string line)
{
    stringstream ss;
    ss << line;
    double x;
    ss >> x;
    stack.push(x);
}

static void onPop()
{
    stack.pop();
}

static void onDup()
{
    stack.push(stack.top());
}

static void onExch()
{
    double x = stack.pop();
    double y = stack.pop();
    stack.push(y);
    stack.push(x);
}

static void onClear()
{
    stack.clear();
}

static void display()
{
    if (!stack.empty())
    {
        cout << "= " << stack.top() << endl;
    }
    else
    {
        cout << "Stack is empty." << endl;
    }
}

static void onShow()
{
    int d = stack.size();
    cout << "Depth of the stack: " << d;
    if (d > 0)
        cout << "Stack elments:" << endl;
    else
        cout << endl;

    for (int i = 0; i < d; i++)
    {
        cout << "\t" << stack.elmtat(i);
    }
}

static void printHelp()
{
    cout << "*******" << endl;
}

static void onSin()
{
    double x = stack.pop();
    stack.push(sin(x));
    display();
}

static void onCos()
{
    stack.push(cos(stack.pop()));
    display();
}

static void onTan()
{
    stack.push(tan(stack.pop()));
    display();
}
static void onArcsin()
{
    stack.push(asin(stack.pop()));
    display();
}

static void onArccos()
{
    stack.push(acos(stack.pop()));
    display();
}

static void onArctan()
{
    stack.push(atan(stack.pop()));
    display();
}

static void onLn()
{
    stack.push(log(stack.pop()));
    display();
}

static void onLog()
{
    stack.push(log10(stack.pop()));
    display();
}

static void onLogxy()
{
    double y = stack.pop();
    double x = stack.pop();
    stack.push(log(y) / log(x));
    display();
}

static void onExp()
{
    stack.push(exp(stack.pop()));
    display();
}

static void onXpy()
{
    double y = stack.pop();
    double x = stack.pop();
    stack.push(pow(x, y));
    display();
}