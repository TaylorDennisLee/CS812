#include <stdio.h>
#include <math.h>


bindis(int num)
{
    int binsize,index,index2,num2;
    num2 = num;
    binsize = ceil(log2(num2));
    int output[binsize];
    output[binsize-1] = 1;
    for (index = 0; index < binsize-1; index++)
    {
        if ((num2 % 2) == 1)
        {
            output[index] = 1;
        }
        else
        {
            output[index] = 0;
        }
        num2 >>= 1;
    }
    for (index2 = (binsize-1); index2 >= 0; index2--)
    {
        printf("%d",output[index2]);
    }
    printf("\n");
}

int isqrt(int num) {
    int res = 0;
    int bit = 1 << 14; // The second-to-top bit is set: 1 << 30 for 32 bits
    
    // "bit" starts at the highest power of four <= the argument.
    while (bit > num)
    {
        bit >>= 2;
        printf("bit:");
        bindis(bit);
    }

    while (bit != 0) {
        if (num >= res + bit) {
            num -= res + bit;
            res = (res >> 1) + bit;
        }
        else
            res >>= 1;
        bit >>= 2;
    }
    return res;
}

main()
{
    printf("End:%d",isqrt(40));
}