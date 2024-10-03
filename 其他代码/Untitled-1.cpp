using namespace std;
int main()
{
	int x,a,b,c;
	cin >> x;
	if (x % 4 == 0)
	{
		a = 0;
		b = 0;
		c = x / 4;
	}
	else if (x % 4 == 1)
	{
		a = 0;
		b = 1;
		c = x / 4 - 1;
	}
	else if (x % 4 == 2)
	{
		a = 1;
		b = 0;
		c = x / 4 - 1;
 
	}
	else if (x % 4 == 3)
	{
		a = 1;
		b = 1;
		c = x / 4 - 2;
	}
	cout << a << " " << b << " " << c;
}