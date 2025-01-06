def share_or_steal(list1: list[str], list2: list[str]) -> list[int]:
    user1 = 3
    user2 = 3
    i = 0
    while i < len(list1):
        if list1[i].strip() =='share':
            user1 -= 1
            user2 += 3
        if list2[i].strip() == 'share':
            user2 -= 1
            user1 += 3
        i+=1
    
    return [user1, user2]

ls1 = input("User1 ni kiriting: (steal or share) ").split(",")
ls2 = input("User2 ni kiriting: (steal or share) ").split(",")

print(share_or_steal(ls1, ls2))
