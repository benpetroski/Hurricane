'''
@author: bpetroski
'''
  
if __name__ == '__main__':
    print 'Enter number of digits to be computed:'
    digits=int(raw_input())
    val=reduce(lambda x,p:p/2*x/p+2*10**digits,range(6637,1,-2))
    print '%s.%s' % (str(val)[0], str(val)[1:])