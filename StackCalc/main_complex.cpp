#include "Stack.h"
#include <iostream>
#include <math.h>
#include <string>
#include <sstream>
#include "Complex.h"
#include "Complex.cpp"
#include <stdexcept>

using namespace std;

static void onAdd();
static void onSub();
static void onMul();
static void onDiv();
//static void onMod();
static void onPush(string);
static void onPop();
static void onDup();
static void onExch();
static void onClear();
static void display();
static void printHelp();
static void onShow();

static Stack<Complex> stack;

int main()
{
    printHelp();

    string line;

    while (getline(cin,line))
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
            //else if (line == "%")
                //onMod();
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
    Complex y = stack.pop();
    Complex x = stack.pop();
    stack.push(x + y);
    display();
}

static void onSub()
{
    Complex y = stack.pop();
    Complex x = stack.pop();
    stack.push(x - y);
    display();
}

static void onMul()
{
    Complex y = stack.pop();
    Complex x = stack.pop();
    stack.push(x * y);
    display();
}

static void onDiv()
{
    Complex y = stack.pop();
    Complex x = stack.pop();
    stack.push(x / y);
    display();
}

/*static void  onMod()
{
    Complex y = stack.pop();
    Complex x = stack.pop();
    stack.push(fmod(x,y));
    display();
}*/

static void onPush(string line)
{
    stringstream ss;
    ss << line;
    double x(0.);
    ss >> x;
    //ss << line;
    double y(0.);
    ss >> y;
    Complex tmp = Complex(x,y);
    stack.push(tmp);
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
    Complex x = stack.pop();
    Complex y = stack.pop();
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
        stack.top().displayCom();
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
        stack.elmtat(i).displayCom();
    }
}

static void printHelp()
{
    cout << "*******" << endl;
}