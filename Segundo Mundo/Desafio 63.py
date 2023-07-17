#sequencia de Fibonacci

n = int(input('Digite um número: '))

fib = 0
aux = 0
i = 0
while i < n:
    print(fib, end=' ')
    fib = fib + aux
    aux = fib - aux

    if fib == 0:
        fib = fib + 1
    i += 1
