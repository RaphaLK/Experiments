#include <cstdio>

int A, T;
float Area;

int main(){
    scanf("%d %d", &A, &T);
    Area = (0.5)*(A*T);
    printf("%.2f", Area);
}