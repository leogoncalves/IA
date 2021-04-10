soma(0, S) :- S is 0.
soma(A, B):-
    C is A - 1,       
    soma(C, D),
    B is A + D.


