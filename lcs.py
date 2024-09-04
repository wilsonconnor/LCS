# Generate the table arrays for b and c
def LCSLength(X, Y):
    m = len(X)
    n = len(Y)
    b = dict() # b and c are made to be dictionaries
    c = dict() 

    for i in range(1, m+1): # Initialize the first row to 0
        c[i, 0] = 0
    for j in range(1, n+1): # Initialize the first column to 0
        c[0, j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: # If both are same, point to NWE index, add 1
                c[i, j] = c[i-1, j-1]+1
                b[i, j] = "↖"
            elif c[i-1, j] >= c[i, j-1]: # If max is index above, OR tied
                c[i, j] = c[i-1, j]      # assign an up arrow, set index val to above's
                b[i, j] = "↑"
            else:
                c[i, j] = c[i, j-1] # Else assign left arrow, same as left being max
                b[i, j] = "←"       # Also set equal to left index
    return b, c

# Print the longest common subsequence
def printLCS(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i, j] == "↖":
        printLCS(b, X, i-1, j-1)
        print(X[i-1], end = "") # Print i-1 because the X arr is 0-28, not 1-29
    elif b[i, j] == "↑":
        printLCS(b, X, i-1, j)
    else:
        printLCS(b, X, i, j-1)

# Import the data from dna.txt
def getDNA(X, Y):
    file = open('dna.txt', 'r')
    activeArr = X # Start by inserting data into the X array
    i = 0
    while 1:
        char = file.read(1)         
        if not char:
            break
        if char == "\n": # If the next DNA seq. is detected, switch to Y array
            i = 0
            activeArr = Y
        else:
            activeArr.append(char)
    file.close()

def main():
    X = []
    Y = []
    getDNA(X, Y)

    b = []
    c = []
    b, c = LCSLength(X, Y)

    print("The length of the LCS is:", c[len(X),len(Y)])
    print("The LCS is:", end = " ")
    printLCS(b, X, len(X), len(Y))

main()
