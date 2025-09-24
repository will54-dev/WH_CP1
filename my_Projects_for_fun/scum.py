# Wh 2nd scum card game

cards = [52,"h1","d1","s1","c1","h2","d2","s2","c2","h3","d3","s3","c3","h4","d4","s4","c4","h5","d5","s5","c5","h6","d6","s6","c6","h7","d7","s7","c7","h8","d8","s8","c8","h9","d9","s9","c9","h10","d10","s10","c10","hj","dj","sj","cj","hq","dq","sq","cq","hk","dk","sk","ck"]

import random

def suffle(cardt):
    cardt_1 = [cardt[0]//2,cardt[1:cardt[0]//2]]
    cardt_2 = [cardt[0]-cardt[0]//2 , cardt[cardt[0]-cardt[0]//2:cardt[0]]]
    random_card_1 = 1
    random_card_2 = 1
    random_count_1 = 0
    random_count_1 = 0
    cardt_3 = [cardt[0]]

    while
    random_val_1 = random.randint(1,2)
    random_val_2 = random.randint(1,2)
    cardt_3 += cardt_1[1][random_card_1:random_card_1+random_val_1]
    cardt_3 += cardt_1[1][random_card_2:random_card_2+random_val_2]
    random_card_2 += random_val_2
    random_card_1 += random_val_1
    
    print(cardt_1)
    print(cardt_2)
    print(cardt_3)
    

suffle(cards)