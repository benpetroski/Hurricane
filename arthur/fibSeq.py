'''
@author: benpetroski
'''

if __name__ == '__main__':
    print 'Enter nth iteration/max val (>0):'
    stopper=int(raw_input())    
    fibPrevious=1
    fibPrev=fibPrevious
    fib=fibPrev
    flag=True
    for i in xrange(stopper): 
        fib=fibPrev+fibPrevious      
        fibPrev=fibPrevious
        fibPrevious=fib 
        if fibPrevious>stopper and flag:
            boundFib = fibPrev 
            flag=False
    print 'Fib('+str(stopper)+') = '+str(fibPrev)+'\nMax Fib<'+str(stopper)+' = '+str(boundFib)