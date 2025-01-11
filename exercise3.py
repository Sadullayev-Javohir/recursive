"""n-Fibonachi sonini rekursiv funksiya yordamida
aniqlovchi dastur tuzing.
Bunda:
f(0) = 1, f(1) = 1, f(n) = f(n-1)+f(n-2), n>=2."""

def fibonachchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachchi(n - 1) + fibonachchi(n - 2)
    
print(fibonachchi(10))
        