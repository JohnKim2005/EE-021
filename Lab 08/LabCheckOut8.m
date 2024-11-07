num_cols = 3;
num_rows = 3;

a(3,3) = 0;

for i = 1:num_cols
    for j = 1:num_rows
        a(i,j) = 0;
    end
end

disp(a)

a(1,1) = -1;
a(1,3) = 1;
a(2,1) = -2;
a(2,3) = 2;
a(3,1) = -1;
a(3,3) = 1;


disp(a)