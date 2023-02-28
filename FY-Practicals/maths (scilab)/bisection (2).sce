clc
a=input("Enter lower limit: ")
b=input("Enter upper limit: ")
k=input("Enter number of iterations: ")
deff("[y]=f(x)","y=x^3-20")

if(f(a)*f(b)>0) then disp ("Wrong limits")
   else
    j=1
    while (j<=k)
        xm=(a+b)/2
        printf("%f %f %f %f %f %f\n", a, b, xm, f(a), f(b), f(xm))
        if (f(a)*f(xm)<0) then b=xm
            else a=xm
        end
        j=j+1
    end
    disp("approximate root in bisection method is: ", xm)
end
