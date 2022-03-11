# There is a queue for the self-checkout tills at the supermarket. Your task is
# write a function to calculate the total time required for all the customers 
# to check out!

def queue_time(customers, n):
    
    if n == 1:
        return sum(customers)
    else:
        till = []
        
        for i in range(n):
            try:
                till.append(customers.pop(0))
            except IndexError:
                pass
                
        while customers:
            ind = till.index(min(till))
            try:
                till[ind] += customers.pop(0)
            except IndexError:
                pass
                
    return max(till)