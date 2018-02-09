%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%       Marmara University, Computer Science Engineering                 %
%       MATH2059 - Numerical Methods                                     %
%       Homework #2 - Problem #3                                         %
%                                                                        %
%       Oguzhan BÖLÜKBAS - 150114022                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function [k, m] =  cubicspline(x,y)
    
    x = x;
    y = y;
    
    %Length of the x coordinates that is also equal to y-coor.'s length
    n = length(x)

    %To keep the distance between each pair of x-coor.
    h = zeros(n-1)

    %To keep the distance between each pair of y-coor. relative to h[]
    b = zeros(n-1)

    %To calculate the distances beetween each pair coordinates for x and y
    for i=1 : (n-1)

        h(i) = x(i+1) - x(i)
        b(i) = (y(i+1) - y(i)) / h(i)

    end

    %It is two less because of starting point and end point
    A = zeros(n-2, n-2)

    %Make the calculations with cubic spline formulas
    for i=1 : n-3

        A(i, i) = 2*(h(i) + h(i+1))    %Derivative
        A(i, i+1) = h(i+1)   %Write one up the diagonal
        A(i+1, i) = h(i+1)    %Write one down the diagonal

    end

    A(n-2, n-2) = 2*(h(n-2)+ h(n-1))

    %Its for second derivative
    C = zeros(n-2, 1)

    for i=1 : n-2

        %Calculate the second derivative
        C(i) = 6 * (b(i+1) - b(i))

    end

    z = A\C

    %To assign the starting point and end point to zero
    z = [0; z; 0]
    
    i = n-1;
    
    k = x;
    
    m = zeros (size ( k ) ) ;
    
    m = z(i+1)/(6*h(i)).*(k-x(i)).^3+z(i)/(6*h(i)).*(x(i+1)-k).^3+(y(i+1)/h(i)-h(i)*z(i+1)/6).*(k-x(i))+(y(i)/h(i)-h(i)*z(i)/6.*(x(i+1)-k))
       
end