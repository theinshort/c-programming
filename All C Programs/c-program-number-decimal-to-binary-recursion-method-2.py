/* Decimal to binary numbers also taking into account negative numbers. */ #include <stdio.h> int bitsize = 8; int sizeOfNumber(long n){    // Repeated division by 10 to find the size of the number.    int size = 0;    while (n > 0)    {        n /= 10;        size++;    }    // Bitsize will be helpful while finding the two's complement    if (size > 7)        bitsize = 16;    return size;} long twos_complement(long n){    long i = 1;    long twos_comp = 0;    long r;    int flag = 0;    printf("The number has %d digits so setting bitsize at %d.\n", sizeOfNumber(n), bitsize);    for (int j = 0; j < bitsize; j++)    {        // Finding the remainder and appending it according to the flag.        r = n % 10;        if (flag == 1)            twos_comp += ((r == 1) ? 0 : 1) * i;        else            twos_comp += r * i;        n /= 10;        i *= 10;        if (r == 1)            flag = 1;    }    printf("The twos complement ");    return twos_comp;} /* Simple decimal to binary convertor */long dec_to_bin(long n){    long bin = 0;    long dec = n;    long i = 1;     while (dec > 0)    {        bin += (dec % 2) * i;        dec /= 2;        i *= 10;    }     return bin;} long toBinary(long n){    // Function to check whether it's a negative or a positive number and     // accordingly passes through the functions.    if (n >= 0)        return dec_to_bin(n);    else        return twos_complement(dec_to_bin(~n + 1));} int main(void){    long n;    printf("Enter a decimal number: ");    scanf("%ld", &n);    printf("Binary equivalent of %ld = %ld\n", n, toBinary(n));    return 0;}