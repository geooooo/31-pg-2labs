topostfix(N, S, [N | S]) :-
    number(N).
topostfix(E, S, R) :-
    E =.. [Op, A, B],
    member(Op, [+, -, *, /]),
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

run(EXPR, RES).

% ?- calc([+], [4, 5], R).
% R = 9.
%
% ?- topostfix(1/1, [], R).
% R = [1, 1, /] .
%
% ?- calc([/], [4, 5], R).
% R = 0.8.
