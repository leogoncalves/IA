insertInOrder(X, [], [X]).
insertInOrder(X, [H|T], [X, H|T]):-
    X =< H.
insertInOrder(X, [H|T1], [H|T2]) :-
    X > H,
    insertInOrder(X, T1, T2).

multiples(0, []).
multiples(X, []) :-
    X < 4.
multiples(X, [4]) :- 
    X = 4.
multiples(X, [X|T]) :- 
    X > 4,
	0 is X mod 4,
    X1 is X - 1,
    multiples(X1, T).
multiples(X, T) :-
    X > 4,
    not(0 is X mod 4),
    X1 is X - 1,
    multiples(X1, T).
    	  
