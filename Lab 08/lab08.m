% MATLAB code template for lab08, EE 021


% 3a. Create an empty array that has three rows and three columns. 
% Print the array.
num_rows = 3
num_cols = 3

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Fix the code below to create an empty array with num_rows rows and num_cols columns.
% You must use the nan function to create the array.
% As an example, the code below creates a 2x2 array.
my_array = nan(num_rows, num_cols) % This is incorrect. Fix it.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

disp('Empty array with NaN (not a number) is')
disp(my_array)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3b. Fill up the array with all zeros. Must use for loops for this task.
% Two nested for loops in MATLAB are given below to get you started.
for i = 1:num_rows
    for j = 1:num_cols
        my_array(i,j) = 0
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3c. Update the values at all indices of the array with 
% values equal to the following 3 x 3 matrix: 
% [-1, 0, 1],
% [-2, 0, 2],
% [-1, 0, 1]
% You must update the already existing my_array variable, not create a new one.
% You may get started with the following code: my_array(1, 1) = -1
my_array(1,1) = -1
my_array(1,3) = 1
my_array(2,1) = -2
my_array(2,3) = 2
my_array(3,1) = -1
my_array(3,3) = 1

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Print the updated array with a \t (tab) separator between elements.
% Hint: fprintf('%d\t', my_array(i, j)) prints the value at index i, j 
% of the array and then adds a tab space.
% Hint: fprintf('\n') prints a newline character.
disp("Updated array is")
for i = 1:num_rows
    for j = 1:num_cols
        fprintf('%d\t', my_array(i, j))
    end
    fprintf('\n')
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3d. Find the value in the array that is exactly equal to 2, and change it to 4.
% Stop the loop once you find the value with the break statement.
done = false

for i = 1:num_rows
    for j = 1:num_cols
        if my_array(i,j) == 2
            my_array(i,j) = 4
            done = true
            break
        end
    end
    if done
        break
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3e. Retrieve data at 1,2 index of the array and print it.
% Fix this line to print only the index needed.
fprintf('Data at 1,2 index is %d\n', my_array(1,2)) 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3f. Update the value at the 2,2 index of the array and print the updated array.

my_array(2,2) = 32
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Print the updated array with a \t (tab) separator between elements.
disp("Updated array is")

for i = 1:num_rows
    for j = 1:num_cols
        fprintf('%d\t', my_array(i, j))
    end
    fprintf('\n')
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3g. Add two more rows and two more columns to create a new array.
% Fill up the array with the values in my_array, and new rows and columns as 0s.
num_rows = num_rows + 2
num_cols = num_cols + 2
new_array = nan(num_rows, num_cols) % This is incorrect. Fix it.
% Update values in this new array with the values in my_array and 0s for all other indices.


for i = 1:num_rows
    for j = 1:num_cols
        if i < 4 && j < 4
            new_array(i,j) = my_array(i,j)
        else 
            new_array(i,j) = 0
        end
        
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Print the updated array with a \t (tab) separator between elements.
disp("Expanded array is")


for i = 1:num_rows
    for j = 1:num_cols
        fprintf('%d\t', new_array(i, j))
    end
    fprintf('\n')
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%