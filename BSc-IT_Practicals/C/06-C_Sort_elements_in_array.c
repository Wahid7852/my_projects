#include<stdio.h>
#include<conio.h>

void swap(int *x, int *y) 
{ 
   int temp = *x; 
   *x = *y; 
   *y = temp; 
}

void sort(int array[], int s) 
{ 
    int i, j, k;
    for (i = 0; i < s-1; i++) 
    { 
        k=i;
        for (j=i+1; j < s; j++)
        {
            if (array[j] < array[k]) 
            k=j; 
        }
        swap(&array[k], &array[i]); 
     } 
}

void show(int array[], int s) 
{ 
    int i; 
    for (i=0; i<s; i++)
    { 
       printf("%d ",array[i]);
    }
     printf("\n"); 
}

void main() 
{
    int array[100], s, i;
    printf("Enter size of array: ");
    scanf("%d", &s);
    printf("Enter elements of array: ");

    for (i=0; i<s; i++)
    {
        scanf("%d ", &array[i]);
    }

    sort(array, s);
    show(array, s);
    getch(); 
}