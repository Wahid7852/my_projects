#include<stdio.h>
#include<conio.h>

//program to read matrix of size m*n
void main()
{
    int array1[3][3],i,j,m,n,sum=0;

    printf("Enter no. of rows: \n");
        scanf("%d", &m);
    printf("Enter no. of columns: \n");
        scanf("%d",&n);
    printf("Enter values to the matrix: \n\n");
        
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("\nEnter a[%d][%d] value: ",i,j);
            scanf("%d", &array1[i][j]);
        }
    }
    
    printf("\nThe given matrix is \n\n");    
    for (i = 0; i < m; ++i)
    {
        for (j = 0; j < n; ++j)
        {
            printf("\t%d", array1[i][j]);
        }
        printf("\n\n");
    }

getch();
}