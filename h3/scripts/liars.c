#include <stdio.h>
#include <assert.h>
#include <gmp.h>

int main(int argc, char *argv[])
{

    int i,exp;
    mpz_t n;
    mpz_t modded;
    mpz_t NminusModded;
    mpz_t a;
    int inputOne = atoi(argv[1]);

    int liars = 0;
    int Oneliars = 0;
    int Negliars = 0;
    exp = (inputOne-1)/2;
    mpz_init_set_ui(n,inputOne);
    mpz_init(modded);
    mpz_init(NminusModded);
    mpz_init(a);
    
    
    for(i = 1; i < inputOne; i++)
    {
        mpz_set_ui(a,i);
        mpz_powm_ui(modded,a,exp,n);
        mpz_sub(NminusModded,n,modded);
        if(mpz_cmp_si(modded,1) == 0)
        {
            liars++;
            Oneliars++;
            mpz_out_str(stdout,10,a);
            printf("\n");
        }
        if(mpz_cmp_si(NminusModded,1) == 0)
        {
            mpz_out_str(stdout,10,a);
            liars++;
            Negliars++;
            printf("\n");
        }


    }
    mpz_clear(n);
    mpz_clear(modded);
    mpz_clear(NminusModded);
    mpz_clear(a);
    printf("Total Liars: %d\n",liars);
    printf("One Liars: %d\n",Oneliars);
    printf("Neg Liars: %d\n",Negliars);
    return 0;
}
