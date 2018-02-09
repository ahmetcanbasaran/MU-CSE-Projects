function [x, polyVal, division, integratedCoef, integratedVal, derCoef, derVal] = polypint( coef, x1, x2, numpoints )

x = linspace(x1, x2, numpoints); % Generate xPoints as a column vector
polyVal = polyval(coef, x); % Polynom values at the required xPoints

division = linspace(length(coef),1,length(coef));
integratedCoef = coef ./ division;
integratedCoef(1, length(coef)+1) = 1;
integratedVal = polyval(integratedCoef, x);

derCoef = coef(1:end-1).*(length(coef)-1:-1:length(coef)-1); % Derivative coefficients
derVal = polyval(derCoef, x); % Derivative values at the required xPoints

plot(x, polyVal, 'g', x, integratedVal, 'b-.', x, derVal, 'r--');
grid on;
legend('Polynom', 'Integration', 'Derivative');

end