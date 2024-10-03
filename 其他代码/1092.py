#include<bits/stdc++.h>
using namespace std;
int judge(int x)
{
	int i;
	int sum=0;
	for(i=1;i<x;i++)
	{
		if(x%i==0)
		{
			sum+=i;
		}
	}
	return sum;
}

int main()
{
	int i=0;
	while(1)
	{
		i++;
		if(i==judge(judge(i))&&i!=judge(i))
		{
			cout<<i<<" "<<judge(i)<<endl;
			break;
		}
	}
}
