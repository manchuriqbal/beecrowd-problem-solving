second= int(input())

minute= second // 60

second= second% 60

hour= minute //60

minute= minute % 60

print(f"{hour}:{minute}:{second}")