import sys

'''
    create new array c3 of size m+m
    copy c1 into c3
    copy c2 into c3
    call list.sort
    copy c3 into c1
    return c1
    Runtime O(m+n)log(m+n)
    Space O(m+n)
    
    pointer base soln
    Runtime O(m+n)
    Space O(1) 
    
    merge sort cursive soln
'''


def sorted(customerData1, customerData2, m, n) -> list[int]:
    if (customerData1 or customerData2) is None:
        raise LookupError
    if (customerData1.count(0) != n):
        raise LookupError
    if (len(customerData1) != m+n):
        raise LookupError
    p1 = m-1
    p2 = n-1
    p3 = m+n -1
    while p1 >=0 and p2 >=0:
        if customerData1[p1]> customerData2[p2]:
            customerData1[p3] = customerData1[p1]
            p3-=1
            p1-=1
        else:
            customerData1[p3] = customerData2[p2]
            p3-=1
            p2-=1
    return customerData1

def test1():
    customerData1 = [101,104,107,0,0,0]
    m = 3
    customerData2 = [102,105,108]
    n = 3
    sorted(customerData1, customerData2, m, n)
    assert customerData1 == [101,102,104,105,107,108], f"Test1 failed"

def test2():
    customerData1 = [103]
    m = 1
    customerData2 = []
    n = 0
    sorted(customerData1, customerData2, m, n)
    assert customerData1 == [103], f"Test2 failed"

def test3():
    customerData1 = None
    m = 0
    customerData2 = None
    n = 0
    sorted(customerData1, customerData2, m, n)
    assert customerData1 == None , f"Test3 failed"

def test4():
    customerData1 = customerData1 = [101,104,107,0,0,0]
    m = 8
    customerData2 = [102,105,108]
    n = 6
    sorted(customerData1, customerData2, m, n)
    assert customerData1 == None , f"Test4 failed"

def main():
    #test1()
    #test2()
    #test3()
    test4()

if __name__ == "__main__":
    sys.exit(main())