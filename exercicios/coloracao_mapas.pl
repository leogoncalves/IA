/*
 * Coloração de mapas
 * 
 * */

/*
 * 
 * Vamos considerar nesse trabalhos as fronteiras entre 
 * países da América do Sul. 
 * Para o programa, definimos uma lista de países como a lista de países 
 * que existem na América do Sul e definimos suas fronteiras como 
 * frontier(pais, [lista_de_paises]).
 * 
 * As cores do mapa são passadas através de uma lista do tipo colors([cor1, cor2, cor3, cor4]).
 * Utilizamos apenas 4 cores.
 * 
 * O retorno esperado do programa é uma lista de listas, onde cada lista interna retorna
 * o nome do país e sua cor que deve ser utilizada no mapa.
 *
 * 
 * */
continent([brasil, uruguai, argentina, chile, 
          paraguai, bolivia, peru, equador, 
          colombia, venezuela, guiana, suriname, 
          guianaFrancesa]).

frontier(brasil, [uruguai, argentina, paraguai, bolivia, peru, colombia, venezuela, guiana, suriname, guianaFrancesa]).
frontier(uruguai, [brasil, argentina]).
frontier(argentina, [brasil, chile, paraguai, bolivia, uruguai]).
frontier(chile, [argentina, peru, bolivia]).
frontier(paraguai, [argentina, bolivia, brasil]).
frontier(bolivia, [peru, chile, paraguai, argentina, brasil]).
frontier(peru, [equador, bolivia, chile, brasil, colombia]).
frontier(equador, [peru, colombia]).
frontier(colombia, [equador, peru, brasil, venezuela]).
frontier(venezuela, [colombia, guiana, brasil]).
frontier(guiana, [venezuela, suriname, brasil]).
frontier(suriname, [guiana, guianaFrancesa, brasil]).
frontier(guianaFrancesa, [guiana, brasil]).

% Definimos as quatro cores que usaremos para colorir o mapa
% as cores serao verde, amarelo, azul e branco
colors([verde, amarelo, azul, branco]).


/*
 * Precisamos definir algumas regras auxiliares.
 * member[X, T] - verifica se um elemento é membro de uma lista
 * 
 * */

member(X, [X|_]).
member(X, [_|T]) :-
    member(X, T).



/*
    Checa a cor da lista de países
*/
verifyColor([Country|[]], CountryColoredList, []) :-
    not(getColorNeighbor(Country, CountryColoredList, _)),
    !.

verifyColor([Country|[]], CountryColoredList, [Color|[]]) :-
    getColorNeighbor(Country, CountryColoredList, Color),
    !.

verifyColor([Country|N], CountryColoredList, NColors) :-
    verifyColor(N, CountryColoredList, NColors),
    not(getColorNeighbor(Country, CountryColoredList, _)),
    !.

verifyColor([Country|N], CountryColoredList, [Color|NColors]) :-
    verifyColor(N, CountryColoredList, NColors),
    getColorNeighbor(Country, CountryColoredList, Color),
    !.
        
verifyColor([Country|T], [[H, I]|CountryColoredList], [I|ColoredCountry]) :-
    Country = H,
    ColoredCountry = I, 
    !;
    verifyColor(T, CountryColoredList, ColoredCountry).


/*
    Verifica e retorna a cor dos países vizinhos
*/
getColorNeighbor(Country, [[H, I]|[]], Color) :-
    Country = H,
    Color = I, 
    !.

getColorNeighbor(Country, [[H, I]|ListColoredCountries], Color) :-
    Country = H,
    Color = I, 
    !;
    getColorNeighbor(Country, ListColoredCountries, Color).



/*
    Define a cor de uma país
*/
defineColor([C|[]], NColor, Color) :-
    not(member(C, NColor)),
    Color = C, 
    !.

defineColor([C | ColorsList], NColor, Color) :-
    not(member(C, NColor)),
    Color = C, 
    !;
    defineColor(ColorsList, NColor, Color).


/*
    Pinta o mapa
*/
painting([H|[]], ColorsList, [[H, CountryColor] | []]) :-
    defineColor(ColorsList, [], CountryColor),
    !.

painting([H|L], ColorsList, [[H, CountryColor] | ListColoredCountries]) :-
    painting(L, ColorsList, ListColoredCountries),
    frontier(H, N),
    verifyColor(N, ListColoredCountries, NeighborColor),
    defineColor(ColorsList, NeighborColor, CountryColor).
   


/*
 * 
 * Retorna o mapa com suas cores
 * 
 * */
getColoredCountries(ColoredList) :-
    continent(Countries),
    colors(ColorsList),
    painting(Countries, ColorsList, ColoredList).




/*
    Para retornar o mapa com suas cores, faça
    getColoredCountries(List)

    Uma saída possivel para List foi 
    List = [
        [brasil, branco], [uruguai, verde], [argentina, azul], [chile, amarelo], 
        [paraguai, amarelo], [bolivia, verde], [peru, azul], [equador, amarelo], 
        [colombia, verde], [venezuela, amarelo], [guiana, verde], [suriname, amarelo], 
        [guianaFrancesa, verde]
    ]
    Podemos checar que essa é uma lista válida colorindo os paises. 
    Para isso, podemos utilizar o https://mapchart.net/americas.html.
*/
