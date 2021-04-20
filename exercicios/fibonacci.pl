fib(0, 0).
fib(1, 0).
fib(2, 1).
fib(I, N) :-
    A is I - 1,
    B is I - 2,
    I > 2,
    fib(A, F2),
    fib(B, F1),
    N is F2 + F1.
    
    
