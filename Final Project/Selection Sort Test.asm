    .data
array:  .word 64, 25, 12, 22, 11  # Example array to be sorted (in descending order)
size:   .word 5                    # Number of elements in the array

    .text
    .globl main

main:
    # Load the size of the array
    la   $t0, size          # Load address of size
    lw   $a0, 0($t0)        # Load the size of the array into $a0 (number of elements)

    # Load base address of the array
    la   $t1, array         # Load address of array into $t1 (pointer to array)

    # Outer loop: Iterate over each element in the array
outer_loop:
    beq  $a0, $zero, done    # If $a0 == 0, sorting is complete (array size is exhausted)

    # Set the index of the current element to sort
    move $t2, $zero          # $t2 = 0 (initial index)
    move $t3, $a0            # $t3 = size of the array (used for bounds checking)
    subu $t3, $t3, 1         # $t3 = size - 1 (the last index to consider)

    # Inner loop: Find the largest element in the unsorted portion
    move $t4, $t2            # $t4 = the index of the current maximum element (start with $t2)
    add  $t4, $t4, $t1       # $t4 points to the current maximum element in the array

inner_loop:
    add  $t5, $t2, $t1       # $t5 = current element in the array
    lw   $t6, 0($t5)         # Load array[t2] into $t6 (current element)

    add  $t7, $t2, $t1       # $t7 = next element in the array
    addi $t7, $t7, 4         # Move to the next element
    lw   $t8, 0($t7)         # Load array[t2+1] into $t8

    blt  $t6, $t8, continue_inner  # If current element < next element, update the max index

    move  $t4, $t7          # New maximum element found, so update the index of the maximum

continue_inner:
    addi $t2, $t2, 4         # Move to the next element
    blt  $t2, $t3, inner_loop # Continue inner loop until the end of the array

    # Swap the largest element with the first unsorted element
    # t4 holds the address of the maximum element
    # t2 holds the address of the current element to swap with
    lw   $t5, 0($t4)         # Load the current maximum element
    lw   $t6, 0($t1)         # Load the first unsorted element

    sw   $t6, 0($t4)         # Store the unsorted element at the position of the maximum element
    sw   $t5, 0($t1)         # Store the maximum element at the position of the unsorted element

    # Increment the boundary of the sorted portion (move to the next element)
    addi $t1, $t1, 4         # Increment the base pointer to the next element
    subu $a0, $a0, 1         # Decrease the number of elements left to sort
    j outer_loop             # Go back to outer loop

done:
    # Exit the program
    li   $v0, 10             # Syscall to exit
    syscall
