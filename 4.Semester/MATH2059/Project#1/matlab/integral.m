a = 1.8;
b = 3.2;

%To find the integral, we will use Trapezoidal Rule
h = 0.01;
N = (b - a) / h;

x = linspace(1.8, 3.2, N)

trep1 = 0;

for i = 1 : N - 1

    trep1 = trep1 + f(x(1, i+1)) + f(x(1, i));

end    

trep1 = trep1 * h / 2;

% new h value
h = 0.1;
N = (b - a) / h;

x = linspace(1.8, 3.2, N)

trep2 = 0;

for i = 1 : N - 1

    trep2 = trep2 + f(x(1, i+1)) + f(x(1, i));

end    

trep2 = trep2 * h / 2;

%new h value
h = 1;
N = (b - a) / h;

x = linspace(1.8, 3.2, N)

trep3 = 0;

for i = 1 : N - 1

    trep3 = trep3 + f(x(1, i+1)) + f(x(1, i));

end    

trep3 = trep3 * h / 2;


%To integrate the function with Simpson's 3/8 Rule for different h values
h = 0.01;
simpson381 = 3 * h / 8 * (f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b));

h = 0.1;
simpson382 = 3 * h / 8 * (f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b));

h = 1;
simpson383 = 3 * h / 8 * (f(a) + 3*f((2*a+b)/3) + 3*f((a+2*b)/3) + f(b));


%To integrate the function with Simpson's Rule for different h values
h = 0.01;
simpsons1 = (b - a)/6 * (f(a) + 4*f((a+b)/2) + f(b));

h = 0.1;
simpsons2 = (b - a)/6 * (f(a) + 4*f((a+b)/2) + f(b));

h = 1;
simpsons3 = (b - a)/6 * (f(a) + 4*f((a+b)/2) + f(b));