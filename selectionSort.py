#make an array for the selection
array = [11, 3, 4, 5, 12, 23]

#functional header for selectionsort
def selectioSort(array):

    n = len(array)

    #iterate through the actual array 
    for i in range(n):           #<-- whatever the length of the array is how many times you are going to run the for loop

        #initially assume the first element of the unsorted part as the minimum 

        minimum = i 

        for j in range(i+1, n):

            if (array[j] < array[minimum]): #<-- comparison operator

                minimum = j

        #swap the minimum element with the first element of the unsorted part 
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    return array 
print(selectioSort(array))