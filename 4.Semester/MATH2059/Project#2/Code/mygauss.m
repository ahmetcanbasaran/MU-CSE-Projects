%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%       Marmara University, Computer Science Engineering                 %
%       MATH2059 - Numerical Methods                                     %
%       Homework #2 - Problem #2                                         %
%                                                                        %
%       Oguzhan BÖLÜKBAS - 150114022                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

%singular is a scalar indicating whether the matrix A is non-singular (0) or
%singular (1) (i.e. whether the Gaussian elimination process is successfully
%finished (0) or not (1)), and x is the solution of the system Ax = b.
function [singular, x] = mygauss (A,b)

    %We will work with matrix M which has matrix A and vector b
    M = A;
    
    %To find dimension of the obtained matrix M
    [n,n] = size(M);
   
    %Scale factors, one for each row
    %S vector contains absolute max. number of each row
    S = max(abs(M),[],2);
    M(:, n+1) = b;
    %Now, me must find the ratio vector of the matrix M in order to 
    %divide first column of the M with max. value of ratio vec.
    ratioVector = abs(M(:,1))./S;
    
    %To prevent -0(negative zero)
    tol = 1.e-6; 
    
    for i = 1 : n-1
    
        %Now, we must find the max. value of the ratio vector in order to find
        %pivot number that will be interchanged with first row
        ratioVector(i:n, 1);
        [maxVal, pivot] = max(ratioVector(i:n, 1));
        pivot = pivot + i - 1;
        
        %Now, we must interchange the pivot row with first row of the M
        temp = M(i, :);
        M(i, :) = M(pivot, :);
        M(pivot, :) = temp;
        
        %To do Gaussian reduction
        for c = i+1 : n
            
            ratio = M(c, i) / M(i, i);
            ratio .* M(i, :);    
            M(c, :) = M(c, :) - ratio .* M(i, :);
          
        end
        
        %To prevent negative zero
        M((M < 0) & (M > -tol)) = 0;
        
    end        
    
    %Now, back substitutions
    
    %To do it for each row
    for i = n : -1 : 1
       
        %To substractract value from other rows above    
        for c = i-1 : -1 : 1
            
            ratio = M(c, i) / M(i, i);
            ratio .* M(i, :);
            
            %Subtract the value
            M(c, :) = M(c, :) - ratio .* M(i, :);
          
        end
        
        %To prevent negative zero
        M((M < 0) & (M >- tol)) = 0;
        
    end
    
    %Now, we can find the solution vector
    x = M(:, n+1) ./ diag(M);
    
    %Check whether our solution is true
    if A*x == b
        
        %If true, return 0
        singular = 0;
        
    else
        
        %Return false        
        singular = 1;
        
    end
        
end