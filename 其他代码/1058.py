#include<stdio.h>
int main()
{
    int a;
	int num,n;
while(~scanf("%d",&n)){
	num=0;
	for(int i=1;i<=n;i++){
		a=1;
		for(int j=1;j<=i;j++){
		    a*=j;
		}
		num+=a;
	}
	printf("%d",num);
}
return 0;
}


