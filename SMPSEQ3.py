# http://www.spoj.com/problems/SMPSEQ3/
# ref https://github.com/chao98/Python/blob/master/SPOJ/SPOJ17102.py

x = int(input())
list_x = [int(a) for a in input().split(' ')[:x]]

y = int(input())
list_y = [int(a) for a in input().split(' ')[:y]]

print(*[x for x in list_x if x not in list_y])
