#include <stdio.h>

char* RGBToHex(int r, int g, int b) {
    char* hex = (char*)malloc(7);
    sprintf(hex, "#%02X%02X%02X", r, g, b);
    return hex;
}

int main() {
    // input string values from user console
    int r, g, b;
    printf("Enter the value of r, g, b: ");
    scanf("%d, %d, %d", &r, &g, &b);
    char *hex = RGBToHex(r, g, b);
    printf("Hex value: %s\n", hex);
    return 0;
}
