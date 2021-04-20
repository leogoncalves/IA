







/*
    Exercícios sobre o capítulo 3 do livro
    Bratko
*/

/*
    Definimos a relação conc para trabalhar com listas
    em prolog
*/
conc([], L, L).
conc([X | L1], L2, [X | L3]) :- 
    conc(L1, L2, L3).


/*
    3.1
    a) Usando conc, escreva uma regra que permita remover os últimos
    três elementos de uma lista L produzindo uma lista L1
*/
removeLastThreeElements(L, L1) :- 
    conc(L1, [_,_,_], L).

/*
    b) Escreva uma regra que permita remover os primeiros três
    items de uma lista e gere uma nova lista.
    Pedir por solução

*/
removeFirstThreeElements(LA,LB) :- 
    conc(L1, [_,_,_], LA), 
    conc([_,_,_], LB, L1).

/*
    3.2
    Selecionar o último elemento de uma lista 
    utilizando o conc definido acima
*/

getLastWithConc(Item, List) :-
    conc([_], [Item], List).
getLastWithConc(Item, List) :-
    conc([_], L, List),
    getLastWithConc(Item, L).
% Exemplo: getLastWithConc(L, [1,2,3,4,5])


/*
    3.2
    Selecionar o último elemento de uma lista 
    sem utilizar o conc definido acima
*/
getLastWithoutConc(Item, List) :- 
    [_|[Item]] = List.
getLastWithoutConc(Item, List) :- 
    [_|Tail] = List,
    getLastWithoutConc(Item, Tail).

% Exemplo: getLastWithoutConc(L, [1,2,3,4,5])

/*
 * Caso quisessemos adicionar um item em 
 * uma lista, podemos utilizar o método 
 * add criando um fato que fosse algo como
 * add(Item, List, [Item | List]).
 * add(Item, List) :- add(Item, List, [Item | List]).
 * 	
 * */
add(Item, List, [Item | List]).
add(Item, List) :- add(Item, List, [Item | List]).

/*
 * Remover um elemento da lista
 */

del(X, [X | Tail], Tail).
del(X, [Y | Tail], [Y | Tail1]):-
    del(X, Tail, Tail1).

insert(X, List, BiggerList) :-
    del(X, BiggerList, List).

sublist(S, L) :- 
    conc(L1, L2, L),
    conc(S, L3, L2).

permutation([], []).
permutation([X|L], P) :-
    permutation(L, L1),
    insert(X, L1, P).


/*
 * Consideramos a lista que tem 0 elementos
 * como uma lista de tamanho par e uma lista
 * que ao menos 1 elemento como uma lista de 
 * tamanho ímpar. Vamos definir os 
 * predicados iniciais como lista vazia e lista 
 * com um único elemento. Depois, fazemos a checagem 
 * do tamanho da lista nos baseando na cauda. 
 * */

evenlength([]).
evenlength([_|Tail]) :- 
    oddlength(Tail).

oddlength([_]).
oddlength([_|Tail]) :- 
    evenlength(Tail).

reverse([], []).
reverse([Head|Tail], ReversedList):- 
    reverse(Tail, RL),
    conc(RL, [Head], ReversedList).
    

palindrome(List) :- reverse(List, List).

myshift([Head | Tail], List2) :-
    conc(Tail, [Head], List2).


means(0, zero).
means(1, one).
means(2, two).
means(3, three).
means(4, four).
means(5, five).
means(6, six).
means(7, seven).
means(8, eigth).
means(9, nine).

translate([], []).
translate([H1 | T1], [H2 | T2]) :- 
    translate(T1, T2),
    means(H1, H2).



 % Revisar
subset(_, []).

% 3.11
flatten([], []) :- !.
flatten(L, [L]). 
flatten([Head|Tail], FlatList) :-
    !,
    flatten(Head, L1),
    flatten(Tail, L2),
    append(L1, L2, FlatList).

% 3.16
max(X, Y, Max) :- X >= Y, Max = X.
max(X, Y, Max) :- X < Y, Max = Y.


% 3.17
maxlist([Head|Tail], Max) :- 
    max(Head, Tail, Max).
maxlist([Head|Tail], Max) :- 
    maxlist(Tail, M, Max),
    max(Head, M, Max).

% 3.18
sumlist([], 0).
sumlist([Head | Tail], Total) :-
    sumlist(Tail, S1),
    Total is Head + S1.


% 3.19

% 3.20

% 3.21


    
    















# 3.19)
ordered([]).
ordered([X]).
ordered([H|T]) :- [T1|T2] = T, H =< T1, ordered(T).