
def enqueue(aqueue,item,cRear,qsize):   # function to add items 
    cRear = cRear + 1 % qsize
    aqueue[cRear] = item
    qsize += 1
    
    return aqueue ,cRear ,qsize

def dequeue(cFront,qsize):
    cFront = cFront + 1 % qsize
    qsize -= 1
    
    return cFront, qsize



def Isfull(qsize,msize):   # can be called by the enqueue function 
    if qsize == msize:
        print("Queue is full!!")
        return True


def Isempty(qsize):    # can be called by the dequeue function
    if qsize == 0:
        print("Queue is empty")
        return True


mylist = [" "," "," "," "," "]   #initialise an empty queue
maxsize=5
size=0
front = 0
rear = -1
run = True
########## MAin program ###########

while run:
    if Isfull(size, len(mylist)):
        run = False
    else:
        choice = int(input("1.Add to queue\n2.Remove from queue\n"))
        if choice == 1:
            value = input("Enter value to queue\n")
            mylist, rear, size = enqueue(mylist,value, rear, size)
            print(mylist)
        else:
            print("Removing from queue")
            front, size = enqueue(front, size)
            