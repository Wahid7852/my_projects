#include <stdio.h>

int main() {
  char category;
  
  printf("Welcome to Unit Converter! \n");
  printf("Please choose a letter of which you want to convert: \n");
  printf("Temperature (T), Currency (C) or Mass (M) \n");
  scanf("%c",&category);
  
  switch(category) {
    case 'T': {
      int tempChoice;
      float temp;
      printf("Enter 1 to convert from Fahrenheit to Celsius.\n");
      printf("Enter 2 to convert from Celsius to Fahrenheit.\n");
      scanf("%d", &tempChoice);
      printf("Enter temperature value: ");
      scanf("%f", &temp);
      if(tempChoice == 1) {
        printf("Celsius: %.2f", (temp-32)*(5.0/9.0));
      }
      else if(tempChoice == 2) {
        printf("Fahrenheit: %.2f", (temp*(9.0/5.0)) + 32);
      }
      else {
        printf("Please choose a valid option.\n");
      }
      break;
    }
    case 'C': {
      int currencyChoice;
      float amount;
      printf("Enter 1 for USD to Euro.\n");
      printf("Enter 2 for USD to INR.\n");
      printf("Enter 3 for Euro to INR.\n");
      scanf("%d", &currencyChoice);
      printf("Enter amount: ");
      scanf("%f", &amount);
      switch(currencyChoice) {
        case 1:
          printf("Euro: %.2f", amount*0.85);
          break;
        case 2:
          printf("INR: %.2f", amount*74.68);
          break;
        case 3:
          printf("INR: %.2f", amount*88.08);
          break;
        default:
          printf("Please choose a valid option.\n");
          break;
      }
      break;
    }
    case 'M': {
      int massChoice;
      float mass;
      printf("Enter 1 for kilograms to pounds.\n");
      printf("Enter 2 for pounds to kilograms.\n");
      scanf("%d", &massChoice);
      printf("Enter mass value: ");
      scanf("%f", &mass);
      if(massChoice == 1) {
        printf("Pounds: %.2f", mass*2.204623);
      }
      else if(massChoice == 2) {
        printf("Kg: %.2f", mass*0.4535924);
      }
      else {
        printf("Please choose a valid option.\n");
      }
      break;
    }
    default:
      printf("Please choose a valid category.\n");
      break;
  }
  
  return 0;
}
