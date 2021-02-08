#include <cstdio>
#include <cmath>
using namespace std;

int a, b, c, d, e;

float result1, result2;

int main(){
    scanf("%d %d %d", &a, &b, &c);
    d = (b*b)-(4*a*c);
    e = 2*a;
    result1 = ((-b+sqrt(d))/(e));
    result2 = ((-b-sqrt(d))/(e));

    printf("%.2f\n%.2f\n%d\n%d", result1, result2, d, e);
}