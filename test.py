import heapq
result=[]
heapq.heappush(result, 14)
print(result)
# [14]

heapq.heappush(result, 10)
print(result)
# [10, 14]

heapq.heappush(result, 6)
print(result)
# [6, 14, 10]

heapq.heappush(result, 8)
print(result)
# [6, 8, 10, 14]

heapq.heappush(result, 12)
print(result)
# [6, 8, 10, 14, 12]

heapq.heappush(result, 4)
print(result)

print(heapq.heappop(result))
print(result)
print(heapq.heappop(result))
print(result)
print(heapq.heappop(result))
print(result)

print(heapq.heappop(result))
print(result)

print(heapq.heappop(result))
print(result)

print(heapq.heappop(result))
print(result)

print(heapq.heappop(result))
print(result)
