

#sorts the array with the number of indexes
def sortArrays(Array1,Array2,index):
    #Combines Array 1 and Array 2
    combined_array = Array1 + Array2

    #Sorts the array in numerical order using a built in function
    combined_array.sort()
    
    #separates the array based on the index of the array and returns a string
    return "sortArrays(arr1, arr2, k) returns: \n" + str(combined_array[0:index])

