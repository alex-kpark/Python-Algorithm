from itertools import product
from collections import defaultdict, namedtuple
import string, random
import time

'''
Bottom-up Approach
'''
def lcs_grid(xs, ys):

    Cell = namedtuple('Cell', 'length move')
    grid = defaultdict(lambda: Cell(0, 'e'))
    sqs = product(enumerate(ys), enumerate(xs))
    for (j, y), (i, x) in sqs:
        if x == y:
            cell = Cell(grid[(j-1, i-1)].length + 1, '\\')
        else:
            left = grid[(j, i-1)].length
            over = grid[(j-1, i)].length
            if left < over:
                cell = Cell(over, '^')
            else:
                cell = Cell(left, '<')
        grid[(j, i)] = cell
    return grid

#실제로 실행하는 함수
def lcs(xs, ys):
    grid = lcs_grid(xs, ys)
    i, j = len(xs) - 1, len(ys) - 1
    lcs = list()
    for move in iter(lambda: grid[(j, i)].move, 'e'):
        if move == '\\':
            lcs.append(xs[i])
            i -= 1
            j -= 1
        elif move == '^':
            j -= 1
        elif move == '<':
            i -= 1
    lcs.reverse()
    return lcs


'''
Top-down
'''
def topdown_lcs(u,v):
    c = [[-1]*(len(v) + 1) for _ in range(len(u) + 1)]
    lcs_helper(u, v, c, 0, 0)
    return c

def lcs_helper(u, v, c, i, j):
    if c[i][j] >= 0:
        return c[i][j]
 
    if i == len(u) or j == len(v):
        q = 0
    else:
        if u[i] == v[j]:
            q = 1 + lcs_helper(u, v, c, i + 1, j + 1)
        else:
            q = max(lcs_helper(u, v, c, i + 1, j),
                    lcs_helper(u, v, c, i, j + 1))
    c[i][j] = q
    return q

#실제로 출력해주는 함수
def print_lcs(u, v, c):
    i = j = 0
    while not (i == len(u) or j == len(v)):
        if u[i] == v[j]:
            print(u[i], end='')
            i += 1
            j += 1
        elif c[i][j + 1] > c[i + 1][j]:
            j += 1
        else:
            i += 1

def random_char(size):
    temp = ''.join(random.choice(string.ascii_letters) for x in range(size))
    return temp.upper()


'''
Non-Dynamic Programming (Recursive)
'''

def recursive_lcs(xlist,ylist):
    if not xlist or not ylist:
        return []
    x, xs, y, ys = xlist[0], xlist[1:], ylist[0], ylist[1:]
    if x == y:
        return [x] + recursive_lcs(xs, ys)
    else:
        return max(recursive_lcs(xlist, ys), recursive_lcs(xs, ylist), key=len)


'''
Testing
'''

u = random_char(100)
v = random_char(100)
recursive_u = list(u) #재귀용 u
recursive_v = list(v) #재귀용 v

#print('Common Input u is:' + u)
#print('Common Input v is:' + v)

#Bottom-up
btn_start = time.time()
lcs(u, v)
btn_end = time.time()

#Top-Down
top_start = time.time()
c = topdown_lcs(u, v)
print_lcs(u, v, c)
top_end = time.time()

#Non-Dynamic
non_start = time.time()
recursive_lcs(recursive_u, recursive_v)
non_end = time.time()


print("Bottom up Approach takes" + btn_end - btn_start)
print("Top Down Approach takes" + top_end - top_start)

#print(non_end - non_start)
