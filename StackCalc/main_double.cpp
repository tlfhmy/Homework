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
            else if (line == "=")
                display();
            else if ((line.length() > 0 && isdigit(line[0])) ||
                     (line.length() > 1 && (line[0] == '-') || line[0] == '+') &&
                         isdigit(line[1]))
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
                (line.length() > 0 && (line[0] == 'q' || line[0] == 'Q')))
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

static void  onMod()
{
    double y = stack.pop();
    double x = stack.pop();
    stack.push(fmod(x,y));
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
    if(!stack.empty())
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
    if(d > 0)
        cout << "Stack elments:" << endl;
    else
        cout << endl;
    
    for(int i = 0; i < d; i++)
    {
        cout << "\t" << stack.elmtat(i);
    }
}

static void printHelp()
{
    cout << "*******" << endl;
}