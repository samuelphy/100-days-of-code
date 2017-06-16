// Testing the shift of weather_station main.c line 173
#include <stdint.h>
#include <stdio.h>

uint32_t raw_h = 0;
uint8_t code;
uint8_t comment;
uint8_t oneshift;

int main()
{
    printf("Code, Comment, OneShift\n");
    for (size_t i = 0xFF; i < 105000; i=i+0x1FF) {
        code = (uint8_t)(i >> 11);
        code <<= 2; //sensor_values.humidity = (uint8_t)((raw_h/1024) * 2);

        comment = (uint8_t)((i/1024) *2);

        oneshift = (uint8_t)(i >> 9);

        code = code / 2;
        comment = comment / 2;
        oneshift = oneshift / 2;

        printf("%d, %d, %d\n", code, comment, oneshift);
    }

    // code = (uint8_t)(raw_h >> 11);
    // code <<= 2; //sensor_values.humidity = (uint8_t)((raw_h/1024) * 2);
    //
    // comment = (uint8_t)((raw_h/1024) *2);
    //
    // oneshift = (uint8_t)(raw_h >> 9);
    //
    // printf("%d vs %d vs %d\n", code, comment, oneshift);
    //
    // char test1 = 0x2F;
    // char test2 = 0x23;
    //
    // printf("%c vs %c\n", test1, test2);
}
