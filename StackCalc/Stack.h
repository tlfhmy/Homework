#ifndef STACK_H
#define STACK_H
#include <stdexcept>
#include <cstdlib>

template <class Value>
class Stack
{
  private:
    int maxElemts;
    int numElemts;
    Value *elmts;

  public:
    Stack() : maxElemts(1024), numElemts(0), elmts(new Value[maxElemts]) {}

    Stack(int maxS) : maxElemts(maxS), numElemts(0), elmts(new Value[maxElemts]) {}

    Stack(const Stack &s) : maxElemts(s.maxElemts), numElemts(s.numElemts), elmts(new Value[maxElemts])
    {
        for (int i = 0; i < s.numElemts; i++)
        {
            elmts[i] = s.elmts[i];
        }
    }

    ~Stack()
    {
        delete[] elmts;
    }

    Stack &operator=(const Stack &s);

    void push(Value x)
    {
        if (numElemts >= maxElemts)
        {
            int extent = maxElemts / 4;
            if (extent < 16)
                extent = 16;
            Value *p = new Value[maxElemts + extent];
            for (int i = 0; i < maxElemts; ++i)
                p[i] = elmts[i];
            elmts = p;
            maxElemts += extent;
        }
        elmts[numElemts] = x;
        ++numElemts;
    }

    Value pop()
    {
        if (numElemts == 0)
            throw std::runtime_error("Stack is empty.");
        Value x = elmts[numElemts - 1];
        --numElemts;
        return x;
    }

    Value top() const
    {
        if (numElemts == 0)
            throw std::runtime_error("Stack is empty.");
        return elmts[numElemts - 1];
    }

    Value &top()
    {
        if (numElemts == 0)
            throw std::runtime_error("Stack is empty.");
        return elmts[numElemts - 1];
    }

    int size() const { return numElemts; }

    void clear() { numElemts = 0; }
    bool empty() const
    {
        return (numElemts == 0);
    }

    Value elmtat(int i) const
    {
        if (i >= numElemts)
            throw std::out_of_range("Out of range.");
        return elmts[numElemts - 1 - i];
    }

    Value &elmtat(int i)
    {
        if (i >= numElemts)
            throw std::out_of_range("Out of range.");
        return elmts[numElemts - 1 - i];
    }
};

#endif