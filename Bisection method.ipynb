# %%
import math as m
import pandas as pd

# %%
a = float(input("a:"))
b = float(input("b:"))
error_bound = float(input("Error bound:"))

# %%
def f1(x):
    return x**6 - x - 1

# %%
def bm_approx(a, b, e):
    iter_bound = m.log((b-a)/e) / m.log(2)
    iter= 0
    data= []
    while iter < iter_bound:
        iter += 1
        c = (a+b)/2
        data.append([iter, a, b, c, b-c, f1(c)])

        if b-c < e:
            break
        elif b-c > e:
            if m.copysign(1,f(b)) * m.copysign(1,f(c)) == -1:
                a = c
            elif m.copysign(1,f(a)) * m.copysign(1,f(c)) == -1:
                b = c
    return pd.DataFrame(data)


# %%
df = bm_approx(a, b, error_bound)
df.rename(columns={0: "Iteration", 1: "a", 2: "b", 3: "c", 4: "b-c", 5: "f(c)"}, inplace=True)
df.set_index("Iteration", inplace= True)
df.head(15)


