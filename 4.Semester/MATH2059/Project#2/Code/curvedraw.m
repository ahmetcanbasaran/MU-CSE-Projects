%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%       Marmara University, Computer Science Engineering                 %
%       MATH2059 - Numerical Methods                                     %
%       Homework #2 - Problem #3                                         %
%                                                                        %
%       Oguzhan BÖLÜKBAS - 150114022                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%To get input from user with using graphical user interface
[x,y] = ginput;

%Calculate the S_x and S_y
[k, m] = cubicspline(x, y);

%Draw the obtained matrices
plot (k, m, 'b-')
    
grid on    

title( 'Cubic spline' )