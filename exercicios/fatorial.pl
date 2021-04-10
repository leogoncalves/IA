fat(1, S) :- S is 1.
fat(A, B):-
    C is A - 1,       
    fat(C, D),
    B is A * D.