%To find derivative of the function with two points method
h = 0.01;
twoPointsDerivative1 = (f(pi + h) - f(pi)) / h;

h = 0.1;
twoPointsDerivative2 = (f(pi + h) - f(pi)) / h;

h = 1;
twoPointsDerivative3 = (f(pi + h) - f(pi)) / h;

%To find derivative of the function with three points method
h = 0.01;
threePointsDerivative1 = (f(pi + h) - f(pi - h)) / 2*h;

h = 0.1;
threePointsDerivative2 = (f(pi + h) - f(pi - h)) / 2*h;

h = 1;
threePointsDerivative3 = (f(pi + h) - f(pi - h)) / 2*h;

%To find derivative of the function with five points method
h = 0.01;
fivePointsDerivative1 = (f(pi - 2*h) - 8*f(pi - h) + 8*f(pi + h) - f(pi + 2*h) ) / 12*h;

h = 0.1;
fivePointsDerivative2 = (f(pi - 2*h) - 8*f(pi - h) + 8*f(pi + h) - f(pi + 2*h) ) / 12*h;

h = 1;
fivePointsDerivative3 = (f(pi - 2*h) - 8*f(pi - h) + 8*f(pi + h) - f(pi + 2*h) ) / 12*h;