:- use_module('../metagol').
%% metagol settings
body_pred(square/1).
body_pred(plane/1).
body_pred(joins/2).
body_pred(on_plane/2).
body_pred(sides/2).
body_pred(angle_plane/3).
%% background knowledge
square(A) :-
	sides(A, 4).
square(c_1).         square(c_2).           square(c_3).
plane(cp_1).         plane(cp_2).           plane(cp_3).
joins(c_1,c_2).      joins(c_1,c_3).        joins(c_2,c_3).
on_plane(c_1, cp_1). on_plane(c_2, cp_2).   on_plane(c_3, cp_3).
angle_plane(cp_1, cp_2, '90'). 
angle_plane(cp_1, cp_3, '90').
angle_plane(cp_2, cp_3, '90').
%% metarules
metarule([P,Q], [P,A,B], [[Q,A,B]]). % identity
metarule([P,Q], [P,A,B], [[Q,B,A]]). % inverse
metarule([P,Q,R], [P,A,B], [[Q,A],[R,A,B]]). % precon
metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,B]]). % postcon
metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]). % chain
metarule([P,Q], [P,A,B], [[Q,A,C],[P,C,B]]). % recursion
%% learning task
  Pos = [
    cube(c_1, c_2, c_3)
  ],
  learn(Pos,[]).