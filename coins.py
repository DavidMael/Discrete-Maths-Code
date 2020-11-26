import math as mt

#Determine if a coin system is canonical by comparing the greedy and dynamic solutions to the coin change problem.

#Copy the list of denominations from a text file to the list den.
denf = open("denominations.txt")
den =[int(element.strip()) for element in denf]
denf.close()
print(den)

#Functions:

#Dynamic programming solution to the coin change problem, for denominations denoms and an add up value of X
def coindyn(denoms, X, memo):

    ndenoms = len(denoms)
    # Solution: minimal quantity of coins used to add up to X
    # Start value: the maximal quantity of coins it can take to add up to X is X, as no testcase has a denomination below 1.
    # Context side note: there is no reason for this not the be the case: if a currency unit is divided into n > 100, 
    # then 1/n rather than 1/100 would be the subunit used on coins. E.g. Tunisian millime coins for 1/1000 Tunisian dinar.
    quant = X
    #a value for the number of coins that add up to X
    interm = 0

    #memoisation
    #skip the base case by initalising memo[0] to 0 before calling the function
    if memo[X] != ( len(memo) ):
        #print("memoised: ", X)
        return memo[X]

    for i in range(0, ndenoms):   
        
        #recursively compute the number of coins needed,
        #but only for arguments X-denoms[i] that can be used to lookup memoised values (>0)
        if X >= denoms[i]:
            interm = 1 + coindyn( denoms, (X - denoms[i]), memo )

            if(interm < quant):
                quant = interm

    memo[X] = quant

    #print("computed recursively: ", X)
    return quant

#Greedy algorithm solution to the coin change problem
def coingreed(denoms, X):
    L = len(denoms)
    S = 0
    #iteratively subtract m of the largest coins possible until X=0
    #result is sum(m for all k) of these coins, equal together to X
    for k in range(0, L):
        m = mt.floor( X/denoms[L-1-k] )
        X -= m*denoms[L-1-k]
        S += m
        if X == 0:
            return S

#Compare the results from these two functions, return true only if equal
#Also uses memoisation as all values but 2*max_denomination will be used more than once (see below)   
def compalgs (denoms, X, memo):
    D = coindyn(denoms, X, memo)
    G = coingreed(denoms, X)
    print("value= %s, greedy result= %s, dynamic result= %s" %(X, G, D))
    return( G == D )

#Test the greedy result against the dynamic for all change values between 0 and 2*max_denomination:
#It can be shown that if a system is not canonical for some X>2*max_denomination, it cannot be canonical for all X<=2*max_denomination
size = len(den)
maxval = 2*den[size-1]+1
canon = 1
memo = [maxval] * (maxval)
memo[0] = 0
for i in range (1, maxval):
    canon = compalgs(den, i, memo)
    if canon == 0:
        break

if(canon):
    print("The coin system is canonical")
else:
    print("The coin system is not canonical")