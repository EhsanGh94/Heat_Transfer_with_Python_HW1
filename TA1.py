# measuring thermal conductivity

"""
int float bool str ...
"""

V = int(input("\nV(V) = "))
I = float(input("\0I(A) = "))
Q = V * I
print("Q(W) = ", Q, "\u0001")

D = float(input("\nD(m) = "))
A = (3.14 * D ** 2)/4

T1 = float(input("T1(K) = "))
T2 = float(input("T2(K) = "))

x1 = float(input("x1(m) = "))
x2 = float(input("x2(m) = "))

k = (0.5 * Q * (x2 - x1))/(A * (T1 - T2))
print("Conductivity of material is: ", "\tk(W/m.K) = ", k)