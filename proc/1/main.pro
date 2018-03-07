topostfix(N, S, [N | S]) :-
    number(N).
topostfix(E, S, R) :-
    E =.. [Op, A, B],
    member(Op, [*, /, +, -]),
    topostfix(A, [Op | S], S1),
    topostfix(B, S1, R).

calc([], [R], R).
calc([N|CS], S, R) :-
    number(N),
    calc(CS, [N|S], R).
calc([OP|CS], [N1, N2|S], R) :-
    E =.. [OP, N1, N2],
    N is E,
    calc(CS, [N | S], R).

run(E, R1) :-
    topostfix(E, S, R),
    calc(R, S, R1),
    !.
