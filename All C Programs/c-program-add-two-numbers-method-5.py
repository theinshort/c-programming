/* * C program to add two numbers without using third variable */ #include <stdio.h> int main(){    int a,b;    printf("Enter Two Numbers: ");     //Input Two Numbers    scanf("%d %d",&a,&b);     //Storing sum in a instead of declaring third variable    a = a+b;     //print sum    printf("Sum is: %d ",a);     return 0;}