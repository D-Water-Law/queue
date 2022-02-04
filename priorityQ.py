class Queue():
    def __init__(self):
        self.queue = [(4,""),(4,""),(4,""),(4,""),(4,"")]
        self.maxS = len(self.queue)
        self.size = 0
        self.front = 0
        self.rear = -1
    
    def enqueue(self, item):
        self.rear = (self.rear + 1) % self.maxS
        self.queue[self.rear] = item
        self.size += 1
        self.queue = sorted(self.queue, key=lambda queue: self.queue[0])
        
        print(self.queue)


    def dequeue(self):
        self.front = (self.front + 1) % self.maxS
        self.size -= 1
        print(self.queue[self.front],"is in front of the queue")

    def isFull(self):
        if self.size == self.maxS:
            print("Queue is full")
            return True   

    def Isempty(self):
        if self.size == 0:
            print("Queue is empty")
            return True   

    def showQ(self):
        for i in self.queue:
            print(i[1], end=" ")
        print() 
    
########## MAin program ###########
print("Names starting with 1 have most priority\nNames with 2 second\nNames with 3 third")
run = True
myQueue = Queue()

while run:
    if myQueue.isFull():
        run = False
    else:
        choice = int(input("1.Add to queue\n2.Remove from queue\n"))
        if choice == 1:
            name = input("Add name to queue\n")
            priority = int(input("Enter Priority level of name"))

            myQueue.enqueue((priority," "+name))
        else:
            if myQueue.Isempty():
                pass
            else:
                myQueue.dequeue()
            