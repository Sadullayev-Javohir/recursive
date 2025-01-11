"""1 dan N gacha bo'lgan natural sonlarning yig'indisini
rekursiv funksiya yordamida hisoblang."""

def hisoblash(n):
    if n > 1:
        return n + hisoblash(n - 1)
    else:
        return 1
    
print(hisoblash(5))