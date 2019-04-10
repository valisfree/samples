#! /usr/bin/env python3
links = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('d', 'a')]
pages = dict()
rank = dict()
for i in links: # a:rank
        for j in i:
            if j not in rank:
                rank.setdefault(j, 1)

for i in rank:
    pages[i] = 0

for i in links:
    pages[i[0]] += 1
k = 1
while k < 11:
    for i in links:
        rank[i[1]] += (rank[i[0]] / pages[i[0]]) * 0.85
    k += 1

print(rank)
