% Generate xPoints as a column vector
xPoints = linspace(pi, 6*pi, 2000);

% Generate results of the xPoints vector with using defined function
yPoints = 3*sin(xPoints.^(3*xPoints)./xPoints).*tan(log(3*exp(0.2*sin(xPoints)).*xPoints))

plot(xPoints, yPoints, 'r--')