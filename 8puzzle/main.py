from draw import *
from time import sleep

''' PARAMETERS '''

# Represent initial and goal states
M_INIT = [
    [1, 0, 3],
    [4, 2, 5],
    [7, 8, 6]
]

M_GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


''' CLASSES '''

class Node():
    def __init__(self, m, moves, parent):
        self.m = m
        self.moves = moves
        self.parent = parent

''' INIT '''

node_init = Node(M_INIT, 0, None)

''' COST '''

def diff(m1, m2):
    loss = 0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            # Number of differing cells between m1 and m2
            if m1[i][j] != m2[i][j]:
                loss += 1

    return loss

def cost(node):
    # 'number of moves' + 'difference to the goal state'
    return node.moves + diff(node.m, M_GOAL)

''' ACTIONS '''

def right(m):
    for i in range(len(m)):
        for j in range(len(m[0])-1):
            # Action: right
            if m[i][j]==0:
                m[i][j] = m[i][j+1]
                m[i][j+1] = 0
                return

def left(m):
    for i in range(len(m)):
        for j in range(1, len(m[0])):
            # Action: left
            if m[i][j]==0:
                m[i][j] = m[i][j-1]
                m[i][j-1] = 0
                return

def down(m):
    for i in range(len(m)-1):
        for j in range(len(m[0])):
            # Action: down
            if m[i][j]==0:
                m[i][j] = m[i+1][j]
                m[i+1][j] = 0
                return

def top(m):
    for i in range(1, len(m)):
        for j in range(len(m[0])):
            # Action: top
            if m[i][j]==0:
                m[i][j] = m[i-1][j]
                m[i-1][j] = 0
                return
            
''' MAKE NEW STATE BY ACTION '''

def makechild(node, kdir):
    m2 = [l[:] for l in node.m]

    if kdir == "l":
        left(m2)
    elif kdir == "r":
        right(m2)
    elif kdir == "t":
        top(m2)
    elif kdir == "d":
        down(m2)
        
    return Node(m2, node.moves+1, node)

''' MAIN '''

# Play manually!
# while True:
    # draw_all(M_INIT, M_INIT==M_GOAL)
    # kdir = detect_keyboard()
    # if kdir=="l":
        # left(M_INIT)
    # elif kdir=="r":
        # right(M_INIT)
    # elif kdir=="t":
        # top(M_INIT)
    # elif kdir=="d":
        # down(M_INIT)

# Initialize 'visit' and 'stack' lists
visit = []
stack = [node_init]

while stack:

    # Take a state from the stack
    node = stack.pop()

    # Show
    draw_all(node.m)
    #

    # State equal to goal?
    if node.m == M_GOAL:
        break

    # Add to visit
    visit.append(node.m)

    # Make child states using the 4 actions (left, right, top, down)
    childs = []
    childs.append(makechild(node, "l"))
    childs.append(makechild(node, "r"))
    childs.append(makechild(node, "t"))
    childs.append(makechild(node, "d"))

    # Iterate the generated child states
    for child in childs:
        # State not visited yet: add to the stack
        if child.m not in visit:
            stack.append(child)

    # Sort the stack to give priority for the minimal cost
    stack = sorted(stack, key=lambda x: cost(x), reverse=True)

# Get the path by taking the parent nodes
path = []
while node:
    path.append(node)
    node = node.parent

# Display the path (initial state -> goal state)
while path:
    node = path.pop()
    draw_all(node.m)
    sleep(1)


while True:
    detect_exit()
