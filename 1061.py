dia, start_date=input().split()
start_date=int(start_date)
s_h, s_m, s_s = map(int, input().split(":"))


dia, end_date=input().split()
end_date=int(start_date)
e_h, e_m, e_s = map(int, input().split(":"))


s= e_s - s_s 
m= e_m - s_m 
h= e_h - s_h
d= end_date - start_date 


if (s < 0):
    s +=60
    m-= 1

if (m < 0):
    m += 60
    h -= 1

if (h < 0):
    h+=12
    d-=1

print(d, h, m, s)

# d1 =(start_date *24*60*60) + (s_h * 60*60)+ (s_m * 60)+ s_s
# d2 =(end_date *24*60*60) + (e_h * 60*60)+ (e_m * 60)+ e_s


# d=h=m=s=0

# for i in range(d1,d2):
#     s+=1
#     if s == 60:
#         m+=1
#         s=0
#         if m== 60:
#             h+=1
#             m=0
#             if h == 24:
#                 d+=1
#                 h=0

# print(s)
