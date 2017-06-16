// Testing shift of positiv and negative numbers
#include <stdint.h>
#include <stdio.h>

int8_t x = 8;
int8_t y = -8;
int8_t z = -8;


int main()
{
    printf(">>  >>  /2\n");
    for (size_t i = 0; i < 6; i=i+1) {
        x >>= 1;
        y >>= 1;
        z /= 2;
        printf("%d, %d, %d\n", x, y, z);
    }
    printf("Shifting instead of div 2 becomes a problem for negative numbers");
}
