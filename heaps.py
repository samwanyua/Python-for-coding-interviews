# heaps
import heapq

# under the hood are arrays
minHeap = []

# to push
heapq.heappush(minHeap, 34)
heapq.heappush(minHeap, 343)
heapq.heappush(minHeap, 32)
heapq.heappush(minHeap, 3423)
heapq.heappush(minHeap, 34232)

# min is always at index 0

print(minHeap) # [32, 343, 34, 3423, 34232]

# loop through heap
while len(minHeap):
    print(heapq.heappop(minHeap))

# no max heaps by default, we use min heap and multiply by -1 when we push and pop
    
maxHeap = []
heapq.heappush(maxHeap, -35)
heapq.heappush(maxHeap, -30)
heapq.heappush(maxHeap, -33)
# max is always at index 0
print(-1 * maxHeap[0])
print(maxHeap)

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# building heap from initial values
arr = [70,71,72,73,74,75]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr)) #prints smallest to alargest


