:- use_module('../metagol').

%% metagol settings
metagol:functional.

%% tell metagol to use the BK
body_pred(mergesort/2).
body_pred(tail/2).
body_pred(head/2).
body_pred(element/2).
body_pred(mylast/2).

%% metarules
metarule(dident, [P,Q,R], [P,A,B], [[Q,A,B],[R,A,B]]).
metarule(chain, [P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]).
metarule(tailrec, [P,Q], [P,A,B], [[Q,A,C],[P,C,B]]).

%% background knowledge
head([H|_],H).
tail([_|T],T).
mylast([A],A):-!.
mylast([_|T],A):-
    mylast(T,A).

element([X|_T],X).
element([_|T],X):-
    element(T,X).
mergesort([H|T],B):-
    msort([H|T],B).

%% functional test
func_test(Atom1,Atom2,Condition):-
  Atom1 = [P,A,B],
  Atom2 = [P,A,Z],
  Condition = (Z = B).

a:-
    Pos = [
        f([1,3,3,4,2,5],3),
        f([6,4,2,5,3,5,1],5),
        f([7,3,4,2,1,5,6,7,8],7),
        f([6,5,7,8,4,2,1,3,7],7),
        f([14,4,13,6,12,1,9,2,10,8,15,5,7,14,3,11],14)
    ],
    learn(Pos,[]).

:- time(a).



%Background
% angle_90(Plane, []).
% angle_90(Plane, [Plane1|RestPlanes]):-
%   angle_90_aux(Plane, Plane1),
%   angle_90(Plane, RestPlanes).

%Target
% cube/2.
% cube(first, [head|tail]):-
%   angle_90_aux(first, head),
%   angle_90(first, tail).

-----

%Background
% angle(first, [second|Tail], deg):-
%   angle_between(first, second, deg)
%   angle(second, Tail, deg)

%Target
% cube/2.
% cube(first, [list]):-
%   angle(first, list, 90),
%   sides(first, 4),
%   allSides(list, 4)


------

%Background
% angle(first, []).
% angle(first, [Head|Tail]):-
%   angle_90(first, Head)
%   angle(Head, Tail)

%Target
% cube/2.
% cube(First, List):-
%   angle(First, List),
%   sides(first, 4),
%   allSides(list, 4)




