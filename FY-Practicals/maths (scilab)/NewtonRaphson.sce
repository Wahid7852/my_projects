clc
deff('y=f(x)','y=x^4-x-10');
deff('z=f1(x)','z=4*x^3-1');
a=input("Enter 1st root: ")
b=input("Enter 2nd root: ")
x=(a+b)/2;
i=1;
while(i<=15)
    x=(x-(f(x)/f1(x)));
    i=i+1;
    [x]
end;
disp("root of the equation is: ", x)
