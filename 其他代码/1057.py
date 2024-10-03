#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
    for(int i=1 ; ; i++)
    {
        if( i%6==1 && i%2==1 && i%3==1 && i%4==1 && i%5==1 && i%7==0 )
        {
            cout << i << endl;
            return 0;
        }
    }
}
