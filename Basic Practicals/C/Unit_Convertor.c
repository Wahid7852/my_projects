#include <stdio.h>

int main() {
  char category;
  int tempChoice;
  int currencyChoice;
  int massChoice;

  //user inputs
  int userinputF;
  int userinputC; 
  int userinputUSDtoEuro; 
  int userinputUSDtoINR; 
  int userinputEurotoINR; 
  int userinputPounds; 
  int userinputKg; 

  //conversion
  int fahrenheitToCelcius;
  int celciusToFahrenheit;
  float USDtoEURO; 
  float USDtoINR; 
  float EUROtoINR; 
  float KgToPounds;
  float PoundsToKg;
  
    //menu
  printf("Welcome to Unit Converter! \n");
  printf("Please choose a letter of which you want to convert: \n");
  printf("Temperature (T), Currency (C) or Mass (M) \n");
  scanf("%c",&category);
  
  if(category == 'T'){
      printf("Enter 1 to convert from Fahrenheit to Celsius. \n");
      printf("Enter 2 to convert from Celsius to Fahrenheit. \n");
      scanf("%d",&tempChoice);
      if(tempChoice == 1){
          printf("Please enter the Fahrenheit degree: \n");
          scanf("%d",&userinputF);
          fahrenheitToCelcius =  ((userinputF-32) * (5.0/9.0));
          printf("Celcius: %d",fahrenheitToCelcius);
      }
      else if(tempChoice == 2){
        printf("Please enter the Celcius degree: \n");
        scanf("%d",&userinputC);
        celciusToFahrenheit = ((9.0/5.0)*userinputC + 32);
        printf("Fahrenheit: %d",celciusToFahrenheit);
      }
      else
        printf("Please choose the correct option. \n");
  }
  
  else if(category == 'C') {
      printf("Enter 1 for USD to Euro. \n");
      printf("Enter 2 for USD to INR. \n");
      printf("Enter 3 for Euro to INR. \n");
      scanf("%d",&currencyChoice);
      if(currencyChoice == 1){
          printf("Please enter the USD amount: \n");
          scanf("%d",&userinputUSDtoEuro);
          USDtoEURO = userinputUSDtoEuro * 0.95; // Variable Rate.
          printf("Euro: %.2f",USDtoEURO); // Using %.2f to round the float to only 2 decimal places;
      }
      else if(currencyChoice == 2){
          printf("Please enter the USD amount: \n");
          scanf("%d",&userinputUSDtoINR);
          USDtoINR = userinputUSDtoINR * 82.80; // Variable Rate.
          printf("INR: %.2f",USDtoINR);
      }
      else if(currencyChoice == 3) {
        printf("Please enter the USD amount: \n");
        scanf("%d",&userinputEurotoINR);
        EUROtoINR = userinputEurotoINR * 88.35; // Variable Rate.
        printf("INR: %.2f",EUROtoINR);
      }
      else
        printf("Please choose the correct option. \n");
   }
  else if(category == 'M'){
      printf("Enter 1 for kilograms to pounds. \n");
      printf("Enter 2 for pounds to kilograms. \n");
      scanf("%d",&massChoice);
      if(massChoice == 1){
          printf("Please enter the kilograms amount: \n");
          scanf("%d",&userinputKg);
          KgToPounds = userinputKg * 2.204623;
          printf("Pounds: %.2f",KgToPounds);
      }
      else if(massChoice == 2) {
          printf("Please enter the pounds amount: \n");
          scanf("%d",&userinputPounds);
          PoundsToKg = userinputPounds * 0.4535924;
          printf("Kg: %.5f",PoundsToKg);
      }
      else 
        printf("Please enter the correct choice. \n");
   }
  return 0;
}
