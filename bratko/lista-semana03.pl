f(X, 0) :- X < 3, !.
f(X, 2) :- 3 =< X, X < 6, !.
f(X, 4) :- 6 =< X.

not(P):-P, !, fail.
not(_).

vencer(a, b).
vencer(c, a).
vencer(d, b).

categ(X, lutador) :- 
    vencer(_, X),
    vencer(X, _).
categ(X, vencedor) :- 
    vencer(X, _), 
    not(vencer(_, X)).
categ(X, perdedor) :- 
    vencer(_, X), 
    not(vencer(X, _)).


p(1).
p(2) :- !.
p(3).

% class(Number, positive) :- Number > 0.
% class(0, zero).
% class(Number, negative):- Number < 0.

class(Number, negative) :- Number < 0, !.
class(Number, zero) :- Number == 0, !.
class(Number, positive) :- Number > 0.

split([], [], []).
split([H|T], [H|P], N) :-
    H >= 0, split(T, P, N).

split([H|T], P, [H|N]) :-
    H < 0, split(T, P, N).


splitcut([], [], []).
splitcut([HP|T], [HP|TP], N) :-
    HP >= 0, 
    !,
    splitcut(T, TP, N).
splitcut([HN|T1], P, [HN|T2]) :-
    HN < 0,
    !,
    splitcut(T1, P, T2).

diffSetsWithCut([], _, []).
diffSetsWithCut([X|L1], L2, L3) :-
    member(X, L2),
    !,
    diffSets(L1, L2, L3).

diffSetsWithCut([X|L1], L2, [X|L3]) :-     
    diffSets(L1, L2, L3).
    
    

diffSets([], _, []).
diffSets([X|L1], L2, L3) :-
    member(X, L2),
    !,
    diffSets(L1, L2, L3).

diffSets([X|L1], L2, [X|L3]) :-     
    not(member(X, L2)),
    diffSets(L1, L2, L3).
    
