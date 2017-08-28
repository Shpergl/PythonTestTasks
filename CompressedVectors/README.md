# Test task text

There are two vectors in a form of long lists. Vectors are compressed in next way - every pair of elements is consist of first element that shows the value of number and the second shows how previous element is compressed.

## Example:
Compressed list `[1,4,3,4,5,3,1,5]`
Extended list `[1,1,1,1,3,3,3,3,5,5,5,1,1,1,1,1]`

The task is to calculate scalar multiplying of compressed vectors.

## Special conditions:
Vectors can't be extended while multiplying because of not enought space to extand, only some space for processing.

## Input values:
first vector: `[1,4,3,4,5,3,1,5]`
second vector `[3,5,4,6,5,5]`

## Quick start:

1. Create directory for script:
`$ mkdir ./scalar_multiply`
2. Step into directory:
`$ cd scalar_multiply`
3. Create new repository:
`$ git init`
4. Checkout repository from github:
`$ git clone https://github.com/Shpergl/PythonTestTasks.git`

# How to use

Go to tasks derectory:
`$ cd CompressedVectors`

## Start tests:

`python3 test.py`

## Start script:
`python3 compressed_lists.py`

Enter valid vectors in compressed form of just input empty string for default values.
Get number of scalar multiplying. Have fun_)



