def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if len(graph[start]) != 0:
        next = graph[start] - visited
        for elem in next:
            dfs(graph, elem, visited)
    return visited


N = int(input())
graph = {}
countDoublesLifts = {}
max_count_doubles = 0

for i in range(N):
    key, value = input().split(" ")
    if key == value:
        if countDoublesLifts.get(key):
            countDoublesLifts[key] += 1
            if countDoublesLifts[key] > max_count_doubles:
                max_count_doubles = countDoublesLifts[key]
        else:
            countDoublesLifts[key] = 1
    if key in graph.keys():
        graph[key].append(value)
    else:
        graph[key] = [value]

sumValues = []
for value in graph.values():
    sumValues.append(value)

for item in sumValues:
    for i in item:
        if i not in graph.keys():
            graph[i] = []

for key in graph.keys():
    graph[key] = set(graph[key])

max_count = 0

for key in graph.keys():
    countOnIter = dfs(graph, key)
    if len(countOnIter) > max_count:
        max_lenght = countOnIter
        max_count = len(countOnIter)
        max_key = key

dublicates = 0

for _, elem in enumerate(max_lenght):

    if countDoublesLifts.get(elem):
        dublicates += countDoublesLifts[elem]

if max_count:
    print(max_count - 1 + dublicates)
elif len(countDoublesLifts) == len(graph):
    print(1)
elif max_count_doubles:
    print(max_count_doubles)
else:
    print(1)
