#include <stdio.h>
#include <math.h>

int depositProfit(int deposit, int rate, int threshold) {
    int balance = deposit;
    int years = 0;
    while ((balance < threshold) && (years < 7)) {
        balance += ceil((balance * rate) / 100);   
        years++;
    }
    return years;
}

int main() {
    printf("Hello");

    int result = depositProfit(100,20,170);
    if (result == 3) {
        printf("Passed");
    } else {
        printf("Failed");
    }
    return 0;
}
