"""Berilgan N natural sonning raqamlari yig'indisini
rekursiv funksiya yordamida hisoblang."""

def yigindi(n):
    if n > 0:
        return (n % 10) + yigindi(n // 10)
    else:
        return 0

print(yigindi(231))