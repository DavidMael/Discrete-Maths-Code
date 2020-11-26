#base fee paid by each client 0...n-1
base = [10, 2, 50, 60, 45, 23]
T = 6

#Greedy algorithm for max profit over T days, find the most profitable contract for each day
def total_greed(T, base): 
    n = len(base)
    value_temp = 0
    value_day = 0
    value_total = 0
    previous_clients = [0] * n
    client_day = 0

    #for each day
    for i in range(T):

        #for each client
        for c in range(n):

            value_temp = base[c]/(2**previous_clients[c])
            print("Client %s would bring %s" %(c, value_temp) )

            if value_temp > value_day:
                value_day = value_temp
                client_day = c

        print("Day %s, client %s pays %s" %(i, client_day, value_day) )
        value_total += value_day
        value_day = 0
        previous_clients[client_day] += 1

    print("Greedy: Total income in %s days: %s" %(T, value_total) )

#Greedy
total_greed(T, base)






