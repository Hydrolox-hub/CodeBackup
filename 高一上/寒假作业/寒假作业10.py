for cock in range(1,20):
    for hen in range(1,32):
        if cock * 5 + hen * 3 + (100 - cock - hen) // 3 != 100:
            continue
        if (100 - cock -hen) % 3 !=0:
            continue
        print("cock=" + str(cock), "hen=" + str(hen), "chick=" + str(100-cock - hen))
