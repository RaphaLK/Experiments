#include <cstdio>
#include <string>

int N, M, A, B;

int main(){
    scanf("%d %d", &N, &M);
    int A = N / M;
    int B = N % M;

    printf("masing-masing %d\n", A);
    printf("bersisa %d\n", B);
}