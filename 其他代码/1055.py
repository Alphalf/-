
#include <bits/stdc++.h>
using namespace std;

int main()
{
    float a,b;
    cin>>a;
    float s=0;
    for(b=1;;b++)
    {
        s=s+(1/b);
        if(s>=a)
        {
            cout<<b;
            break;
        }
        if(a<0)
        {
            cout<<0;
            break;
        }
    }
    return 0;
}
