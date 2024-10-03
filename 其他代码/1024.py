#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int x, a, y, b;
    cin >> x >> a >> y >> b;
    double z = (y * b - x * a) * 1.0 / (b - a);
    cout << fixed << setprecision(2) << z << endl;
    return 0;
}
