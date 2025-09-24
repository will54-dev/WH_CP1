# Wh 2nd scum card game

cards = [52,"h1","d1","s1","c1","h2","d2","s2","c2","h3","d3","s3","c3","h4","d4","s4","c4","h5","d5","s5","c5","h6","d6","s6","c6","h7","d7","s7","c7","h8","d8","s8","c8","h9","d9","s9","c9","h10","d10","s10","c10","hj","dj","sj","cj","hq","dq","sq","cq","hk","dk","sk","ck"]

def suffle(cardt):
    cardt_1 = cardt[1:26]
    cardt_2 = cardt[26:cardt[0]]
    print(cardt_1)
    print(cardt_2)

suffle(cards)