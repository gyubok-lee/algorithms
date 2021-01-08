# https://programmers.co.kr/learn/courses/30/lessons/42892

from collections import deque
import sys
sys.setrecursionlimit(10**6)

def mk_binary_tree(node,now):
    while True:
        if node[1][1] < now[1][1] :
            if node[1][0] > now[1][0] :
                if len(tree[repr(now)][1]) == 0 :
                    tree[repr(now)][1] = node
                    tree[repr(node)] = [[],[]]
                    return
                else :
                    now = tree[repr(now)][1]
            elif node[1][0] < now[1][0] :
                if len(tree[repr(now)][0]) == 0 :
                    tree[repr(now)][0] = node
                    tree[repr(node)] = [[], []]
                    return
                else :
                    now = tree[repr(now)][0]
    return

def preorder(now):
    pre.append(now[0])
    if len(tree[repr(now)][0]) != 0 :
        preorder(tree[repr(now)][0])
    if len(tree[repr(now)][1]) != 0 :
        preorder(tree[repr(now)][1])

def postorder(now):
    if len(tree[repr(now)][0]) != 0 :
        postorder(tree[repr(now)][0])
    if len(tree[repr(now)][1]) != 0 :
        postorder(tree[repr(now)][1])
    post.append(now[0])

def solution(nodeinfo):
    global tree
    tree = dict()
    global pre
    pre = []
    global post
    post = []

    nodeinfo = list(enumerate(nodeinfo,1))
    nodeinfo = sorted(nodeinfo, key = lambda x : x[1][0])
    nodeinfo = sorted(nodeinfo, key=lambda x: x[1][1],reverse=True)

    root = nodeinfo[0]
    tree[repr(root)] = [[],[]]
    parent_nodes = [root]
    nodeinfo = nodeinfo[1:]

    nodeinfo = deque(nodeinfo)
    while nodeinfo:
        n = nodeinfo.popleft()
        mk_binary_tree(n,root)

    preorder(root)
    postorder(root)
    return [pre, post]

nodes = [[5,3]]
print(solution((nodes)))