%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%       Marmara University, Computer Science Engineering                 %
%       MATH2059 - Numerical Methods                                     %
%       Homework #2 - Problem #1                                         %
%                                                                        %
%       Oguzhan BÖLÜKBAS - 150114022                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  

%Part a:

%Generate the sparese matrix of the given matrix A
A = sparse([1/2 0 1/2; 0 0 1/2; 1/2 1 0]);

%To compute eigenvector of the A matrix 
%with using default matlab "eigs" function
matlabEigenVecA = eigs(A);

%initial values
myEigenVecA = [1; 1; 1];;

i = 0;  %to count

%100 times iteraiton is quite enough
while i < 100;
   
    myEigenVecA = A*myEigenVecA;
    
    if myEigenVecA(1,1) == myEigenVecA(3,1)
        
        break;
    
    end    
        
    i = i+1;
    
end

%To calculate normalized value (magnitude of vector) 
norValA = sqrt(power(myEigenVecA(1,1), 2) + power(myEigenVecA(2,1), 2) + power(myEigenVecA(3,1), 2));

%To normalize the eigenvector
myEigenVecA = myEigenVecA./norValA;



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%Part b:

%What will happen if Marmara removes the link from Marmara to Bo?aziçi?

%Generate the sparese matrix of the given matrix A
B = sparse([1/2 0 1/2; 0 0 1/2; 1/2 0 0]);

%To compute eigenvector of the A matrix 
%with using default matlab "eigs" function
matlabEigenVecB = eigs(B);

%initial values
myEigenVecB = [1; 1; 1];;

i = 0;  %to count

%10000 times iteraiton is enough
while i < 10000;
   
    myEigenVecB = B*myEigenVecB;
    
    if myEigenVecB(1,1) == myEigenVecB(3,1)
        
        break;
    
    end    
        
    i = i+1;
    
end

%To calculate normalized value (magnitude of vector) 
norValB = sqrt(power(myEigenVecB(1,1), 2) + power(myEigenVecB(2,1), 2) + power(myEigenVecB(3,1), 2));

%To normalize the eigenvector
myEigenVecB = myEigenVecB./norValB;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%Part c:

%We try to make the Marmara the most important web site

%In this matrix, Marmara shows itself instead of Bo?aziçi
C = sparse([1/2 0 1/2; 0 1 1/2; 1/2 0 0]);

%To compute eigenvector of the A matrix 
%with using default matlab "eigs" function
matlabEigenVecC = eigs(C);

%initial values
myEigenVecC = [1; 1; 1];;

i = 0;  %To count

%To see the result, 10 times iteraiton will be enough
while i < 10;
   
    myEigenVecC = C*myEigenVecC;
    
    if myEigenVecC(1,1) == myEigenVecC(3,1)
        
        break;
    
    end    
        
    i = i+1;
    
end

%To calculate normalized value (magnitude of vector) 
norValC = sqrt(power(myEigenVecC(1,1), 2) + power(myEigenVecC(2,1), 2) + power(myEigenVecC(3,1), 2));

%To normalize the eigenvector
myEigenVecC = myEigenVecC./norValC;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%Part d:

%Generate the sparese matrix of the given matrix A
D = sparse([0 1 0; 0 0 1; 1 0 0]); 

%To compute eigenvector of the A matrix 
%with using default matlab "eigs" function
matlabEigenVecD = eigs(D);

%initial values
myEigenVecD = [1; 1; 1];;

i = 0;  %to count

%100 times iteraiton is quite enough
while i < 100;
   
    myEigenVecD = D*myEigenVecD;
    
    if myEigenVecD(1,1) == myEigenVecD(3,1)
        
        break;
    
    end    
        
    i = i+1;
    
end

%To calculate normalized value (magnitude of vector) 
norValD = sqrt(power(myEigenVecD(1,1), 2) + power(myEigenVecD(2,1), 2) + power(myEigenVecD(3,1), 2));

%To normalize the eigenvector
myEigenVecD = myEigenVecD./norValD;