#include <stdio.h>
int main()
{
	int i,n,s1=0,s2=0;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		if(i%2==0)
			s1+=i;
		else
			s2+=i;
	}
	printf("%d %d\n",s1,s2);
	return 0;
}
