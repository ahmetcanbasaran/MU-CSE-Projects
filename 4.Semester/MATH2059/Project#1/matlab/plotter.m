x = linspace(10,10000,200)

for i = 1 : 200
    
    zpi(1, i) = mypi(x(1, i));
    
end

absolute = abs(pi - zpi)


plot(x, absolute, 'rx')
title('plotter');
xlabel('numpoints');
ylabel('absolute error');
