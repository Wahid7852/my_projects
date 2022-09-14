//Include Libraries

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//Function to stop the program
static void stop()
{
    printf("Press any key to exit...");
    getchar();
    getchar();
    exit(0);
}

//start of main function
int main(int argc, char *argv[])
{
  float v1;
  float v2;
  char operator;
  float answer;

  printf("to add: +, to subtract: -, to multiply: *, to divide: /, to find square root: ^ \n\n");
  printf("What do you need to calculate? :\n\n");
  scanf("%f %c %f", &v1, &operator, &v2);

//operators
  switch(operator)
    {
    case '/': answer = v1/v2;
      break;
    case '*': answer = v1*v2;
      break;
    case '+': answer = v1+v2;
      break;
    case '-': answer = v1-v2;
      break;
    case '^': answer = sqrt(v1);
      break;
    default: goto fail;
    }
  printf("%.9g%c%.9g =  %.6g\n\n",v1,operator, v2, answer);
  goto exit;
 fail:
  printf("Failed, Please enter proper mathematical equation \n");
 exit:
  stop();
  return 0;
}