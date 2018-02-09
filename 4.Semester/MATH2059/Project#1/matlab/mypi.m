function zpi = mypi(numpoints)

success = 0; % sucessful event number 

for i = 1 : numpoints

    a = rand(); %Generate random variables between 0 and 1
  
    b = rand(); %Generate random variables between 0 and 1
  
    if ((a^2 + b^2) <= 1)
    
        success = success + 1;  %Increment the success for this estimation
  
    end
    
end

zpi = 4 * success / numpoints  %Multiply with 4 because we have 4 region in coordinate system

end