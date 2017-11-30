#include <iostream>
#include <string>
using namespace std;


template <class T>
class MyVector {
public:
    MyVector();
    MyVector(const int s);
    ~MyVector();
    
    int Size();
    int Capacity();
    bool IsEmpty();
    T Get(int index);
    void Push(T item);
    void Insert(int index, T item);
    void Prepend(T item);
    T Pop();
    void Delete(int index);
    void Remove(T item);
    int Find(T item);
    void Resize(const int newSize);
    
    void PrintValues();
    
private:
    int size;
    int capacity;
    T* ptr;
    
    void shiftRight(int startIndex);
    void shiftLeft(int statIndex);
};

template <class T>
void MyVector<T>::shiftRight(int startIndex)
{
    if (Size() >= Capacity())
    {
        Resize(Capacity() * 2);
    }
    
    for (int i = Size() - 1; i >= startIndex; --i)
    {
        ptr[i + 1] = ptr[i];
    }
    
    ++size;
}

template <class T>
void MyVector<T>::shiftLeft(int startIndex)
{
    for (int i = startIndex; i < Size() - 1; ++i)
    {
        ptr[i] = ptr[i + 1];
    }
    
    --size;
}


template <class T>
MyVector<T>::MyVector()
{
    size = 0;
    capacity = 2;
    ptr = new T[capacity];
}

template <class T>
MyVector<T>::MyVector(const int s) {
    size = 0;
    capacity = s;
    ptr = new T[capacity];
}

template <class T>
MyVector<T>::~MyVector()
{
    delete ptr;
}

template <class T>
int MyVector<T>::Size()
{
    return size;
}

template <class T>
int MyVector<T>::Capacity()
{
    return capacity;
}

template <class T>
bool MyVector<T>::IsEmpty()
{
    return size <= 0;
}

template <class T>
T MyVector<T>::Get(int index)
{
    if (index >= size)
    {
        throw std::out_of_range("Out of range");
    }
    
    return ptr[index];
}

template <class T>
void MyVector<T>::Push(T item)
{
    if (size >= capacity)
    {
        Resize(capacity * 2);
    }
    
    ptr[size++] = item;
}

template <class T>
void MyVector<T>::Insert(int index, T item)
{
    if (Capacity() < size + 1)
    {
        Resize(Capacity() * 2);
    }
    
    shiftRight(index);
    
    ptr[index] = item;
}

template <class T>
void MyVector<T>::Prepend(T item)
{
    Insert(0, item);
}

template <class T>
T MyVector<T>::Pop()
{
    if (size > 0) {
        T result =  ptr[size - 1];
         --size;
        return result;
    }
    
    throw std::out_of_range("Out of range");
}

template <class T>
void MyVector<T>::Delete(int index)
{
    shiftLeft(index);
}

template <class T>
void MyVector<T>::Remove(T item)
{
    for (int i = 0; i < Size(); ++i)
    {
        if (ptr[i] == item)
        {
            Delete(i);
            --i;
        }
    }
}

template <class T>
int MyVector<T>::Find(T item)
{
    for (int i = 0; i < Size(); ++i)
    {
        if (ptr[i] == item)
        {
            return i;
        }
    }
    
    return -1;
}

template <class T>
void MyVector<T>::Resize(const int newSize)
{
    if (newSize == size)
    {
        return;
    }
    
    if (size > newSize)
    {
        // shrink array
        size = newSize;
        capacity = newSize;
    }
    else if (size < newSize)
    {
        // expand array
        capacity = newSize;
    }
    
    int* newPtr = new int[newSize];
    for (int i = 0; i < size; ++i)
    {
        newPtr[i] = ptr[i];
    }
    
    delete [] ptr;
    
    ptr = newPtr;
}

template <class T>
void MyVector<T>::PrintValues()
{
    cout << "Size: " << Size() << "=>  {";
    
    for (int i = 0; i < Size(); ++i)
    {
        cout << ptr[i] << ", ";
    }
    
    cout << "}" << endl;
}