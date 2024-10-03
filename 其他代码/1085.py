#include <bits/stdc++.h>
using namespace std;
int main(){
	int n,num=1,sum=1;
	cin>>n;
	
	for(int i=2;i<=n;i++){
		num*=i;
		sum+=num;
	}
	
	cout<<sum;
	return 0;
}
