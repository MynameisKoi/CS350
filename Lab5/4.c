#include <stdio.h>

int main() {
    int payment, num_bills, remaining_payment;

    // Read in the payment amount
    printf("Enter total payment: ");
    scanf("%d", &payment);

    // Calculate the number of $100 bills required
    num_bills = payment / 100;
    remaining_payment = payment % 100;

    // Calculate the number of $50 bills required
    num_bills += remaining_payment / 50;
    remaining_payment %= 50;

    // Calculate the number of $20 bills required
    num_bills += remaining_payment / 20;
    remaining_payment %= 20;

    // Calculate the number of $10 bills required
    num_bills += remaining_payment / 10;
    remaining_payment %= 10;

    // Calculate the number of $5 bills required
    num_bills += remaining_payment / 5;
    remaining_payment %= 5;

    // Calculate the number of $1 bills required
    num_bills += remaining_payment;

    // Print the result
    printf("Result of minimum number of bills: %d\n", num_bills);
    printf("$100 bill: %d\n", payment / 100);
    printf("$50 bill: %d\n", (payment % 100) / 50);
    printf("$20 bill: %d\n", (payment % 50) / 20);
    printf("$10 bill: %d\n", (payment % 20) / 10);
    printf("$5 bill: %d\n", (payment % 10) / 5);
    printf("$1 bill: %d\n", payment % 5);

    return 0;
}
