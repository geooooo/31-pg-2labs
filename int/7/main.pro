% граф: (s) ---> (a)
trans(s, a).
trans(s, d).
trans(a, b).
trans(a, d).
trans(b, c).
trans(b, e).
trans(d, e).
trans(e, f).
trans(f, g).

% вставка пустого списка [] в L даёт L
insrt(L,[],L).
% вставка "вперемешку"
insrt(L, [H|T], Res):-
    random_select(H, Z, L),
	insrt(Z, T, Res).

transit([A|Tail], [B, A|Tail]):-
    (trans(A, B); trans(B, A)),
	not(member(B, [A|Tail])).

ndfs1([[Goal|Tail]|_], Goal,[Goal|Tail]).
ndfs1([TempPath|OtherPaths], Goal, Path):-
	findall(W, transit(TempPath, W), Paths),
	insrt(OtherPaths, Paths, Paths1),
	ndfs1(Paths1, Goal, Path).

% предикат для поиска всех путей
% из Start в Goal, результат помещается в NPath
ndfs(Start, Goal, NPath):-
	ndfs1([[Start]], Goal, Path),
	reverse(Path, NPath).













