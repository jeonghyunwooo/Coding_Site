# W : 가로 , H : 세로
# R : 행   , C : 열
W,H = map(int,input().split())
P,Q = map(int,input().split())
Time = int(input())
# Time = Time % (W * H)

if ((P + Time) // W) % 2 == 0: # 짝수면 그대로
    P = (P + Time) % W
else: P = W - ((P + Time) % W)

if ((Q + Time) // H) % 2 == 0: # 짝수면 그대로
    Q = (Q + Time) % H
else: Q = H - ((Q + Time) % H)

print(P,Q)