# There is a queue for the self-checkout tills at the supermarket. Your task is
# write a function to calculate the total time required for all the customers 
# to check out!

def queue_time(customers, n):
    
    ans = []
    
    if n == 1:
        return sum(customers)
    else:
        till = []
        
        for i in range(n):
            try:
                till.append((customers.pop(0), 0))
            except IndexError:
                break  
                
        while till:
            tmp = []
            for (c, t) in till:
                if c > 0:
                    c -= 1
                    t += 1
                    tmp.append((c, t))
                else:
                    try:
                        tmp.append((customers.pop(0), t))
                    except IndexError:
                        ans.append((c,t))
                till = tmp
                
        _, time = max(ans)
    return time