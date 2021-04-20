conc([], L, L).
conc([X | L1], L2, [X | L3]) :- conc(L1, L2, L3).

# 1- Faça um programa Prolog que dadas duas listas L1 e L2, retorne a lista 
# L3 que é a união de L1 e L2. Note que nesta união não pode haver elementos repetidos.

isMember(H, L, L) :-
    member(H, L).

isMember(H, L, [H|L]) :-
    not(member(H, L)).

union([], [], []).

union([H|[]], [], [H]).

union([H|T], [], L):-
    union(T, [], L1),
    !,
    isMember(H, L1, L).

union([], [H|T], L):-
    union(T, [], L1),
    !,
    isMember(H, L1, L).

union([H1|T1], [H2|T2], L) :- 
    conc([H1|T1], [H2|T2], L3),
    union([], L3, L).
    

# Faça um programa Prolog que dadas duas listas L1 e L2, retorne a lista L3 que 
# contém todos os elementos de L2 que não estão em L1. Você deve usar not.

intersect(_, [], []) :- !.
intersect(L, [H|T1], [H|T2]) :-
    not(member(H, L)),
    !,
    intersect(L, T1, T2).

intersect(L, [H|T1], L2) :- 
    member(H, L),
    !,
    intersect(L, T1, L2).
    
