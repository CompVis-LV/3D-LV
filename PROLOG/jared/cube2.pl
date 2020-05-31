:- use_module('../metagol').

%% metagol settings
% body_pred(square/1).
% body_pred(triangle/1).
% body_pred(pentagon/1).
body_pred(joins/2).
body_pred(sides/2).
% body_pred(angle_60_aux/2).
body_pred(angle_90_aux/2).
% body_pred(angle_120_aux/2).
% body_pred(angle_60/2).
body_pred(angle_90/2).
% body_pred(angle_120/2).

%% background knowledge
poly(c_1).               
poly(c_2).                 
poly(c_3).
poly(c_4).               
poly(c_5).                 
poly(c_6).
poly(t_1).               
poly(s_2).                 
poly(s_3).
poly(p_1).
poly(p_2).
poly(p_3).
poly(p_4).
joins(c_1,c_2).          
joins(c_1,c_3).            
joins(c_2,c_3).
joins(c_4,c_5).          
joins(c_4,c_6).            
joins(c_5,c_6).
joins(t_1,s_2).          
joins(t_1,s_3).            
joins(s_2,s_3).
joins(p_1,p_2).          
joins(p_1,p_3).            
joins(p_1,p_4).
joins(p_2,p_3).            
joins(p_3,p_4).
angle_90_aux(c_1,c_2).   
angle_90_aux(c_1,c_3).     
angle_90_aux(c_2,c_3).
angle_90_aux(c_4,c_5).   
angle_90_aux(c_4,c_6).     
angle_90_aux(c_5,c_6).
angle_90_aux(t_1,s_2).   
angle_90_aux(t_1,s_3).     
% angle_120_aux(s_2,s_3).
% angle_90_aux(p_1,p_2).          
% angle_90_aux(p_1,p_3).            
% angle_90_aux(p_1,p_4).
% angle_60_aux(p_2,p_3).
% angle_60_aux(p_3,p_4).
sides(c_1, 4).           
sides(c_2, 4).             
sides(c_3, 4).
sides(c_4, 4).           
sides(c_5, 4).             
sides(c_6, 4).
sides(t_1, 3).           
sides(s_2, 4).             
sides(s_3, 4).
sides(p_1, 6).
sides(p_2, 4).
sides(p_3, 4).
sides(p_4, 4).
% square(A) :-
% 	sides(A,4).
% triangle(B) :-
% 	sides(B,3).
% pentagon(C) :-
% 	sides(C,6).

% angle_90(Plane9, []).
% angle_90(Plane9, [Plane19|RestPlanes9]):-
%   angle_90_aux(Plane9, Plane19),
%   angle_90(Plane9, RestPlanes9).

% angle_60(Plane6, []).
% angle_60(Plane6, [Plane16|RestPlanes6]):-
%   angle_60_aux(Plane6, Plane16),
%   angle_60(Plane6, RestPlanes6).

% angle_120(Plane12, []).
% angle_120(Plane12, [Plane112|RestPlanes12]):-
%   angle_120_aux(Plane12, Plane112),
%   angle_120(Plane12, RestPlanes12).

%angle_90(c_1, [c_2, c_2]).


%% metarules
metarule([P,Q], [P,A,B], [[Q,A,B]]). %% identity
metarule([P,Q], [P,A,B], [[Q,B,A]]). %% inverse
metarule([P,Q,R], [P,A,B], [[Q,A],[R,A,B]]). %% precon
metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,B]]). %% postcon
metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,C,B]]). %% chain
metarule([P,Q], [P,A,B], [[Q,A,C],[P,C,B]]). %% recursion
metarule([P,Q], [P,A,B], [[Q,A,C],[P,C,B]]).
metarule([P,Q], [P,A],[[Q,A]]).
metarule([P,Q,R], [P,A], [[Q,A],[R,A]]).
metarule([P,Q,B], [P,A,B], [[Q,A],[Q,B]]).
metarule([P,Q,R], [P,A], [[Q,A,B],[R,B]]).
metarule([P,Q,X], [P,A], [[Q,A,X]]).
metarule([P,Q,X], [P,A,B], [[Q,A,B,X]]).
metarule([P,Q,R], [P,A], [[Q,A,B]]).
metarule([P,A], [P,A,_B], []).
metarule([P,B], [P,_A,B], []).
metarule([P,Q,X,Y], [P,X,A], [[Q,Y,A]]).
metarule([P,Q], [P,A], [[Q,A]]).
metarule([P,Q,F], [P,A,B], [[Q,A,B,F]]).
metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A,B]]).
metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,A]]).
metarule([P,Q,R], [P,A], [[Q,A,B],[R,A,B]]).
metarule([P,Q,R], [P,A,B], [[Q,A,C],[R,B,C]]).
metarule([P,Q], [P,A,B], [[Q,A,C], [P,C,B]]).
metarule([P,Q,B], [P,A], [[Q,A,B]]).
metarule([P,Q], [P,A,B], [[Q,B,C],[P,A,C]]).
metarule([P,Q],([P,A,B]:-[[Q,A,B]])).
metarule([P,Q,R],([P,A,B]:-[[Q,A,C],[R,C,B]])).
metarule([P,Q,R], [P,A,B], [[Q,B,A],[R,A]]).

%% learning task
:-
  %% positive examples
  Pos = [
    cube([c_1,c_2,c_3]),
    %cube(c_1,[c_3,c_2]),
    cube([c_2,c_1,c_3]),
    %cube(c_2,[c_3,c_1]),
    %cube(c_3,[c_1,c_2]),
    cube([c_3,c_2,c_1]),
    %cube(c_4,[c_5,c_6]),
    %cube(c_4,[c_6,c_5]),
    cube([c_5,c_4,c_6])
    %cube(c_5,[c_6,c_4]),
    %cube(c_6,[c_5,c_4])
    %cube(c_6,[c_4,c_5])
  ],
  %% negative examples
  Neg = [
    cube([t_1,s_2,s_3]),
    %cube(t_1,[s_3,s_2]),
    %%cube(t_2,[s_1,s_3])
    %cube(t_2,[s_3,s_1]),
    %cube(t_3,[s_2,s_1]),
    %cube(t_3,[s_1,s_2]),
    cube([p_1,p_2,p_3,p_4])
    %cube(p_1,[p_2,p_4,p_3]),
    %cube(p_1,[p_3,p_2,p_4]),
    %cube(p_1,[p_3,p_4,p_2]),
    %cube(p_1,[p_4,p_2,p_3]),
    %cube(p_1,[p_4,p_3,p_2]),
    %%cube(p_2,[p_1,p_3,p_4])
    %cube(p_2,[p_1,p_4,p_3]),
    %cube(p_2,[p_3,p_1,p_4]),
    %cube(p_2,[p_3,p_4,p_1]),
    %cube(p_2,[p_4,p_1,p_3]),
    %cube(p_2,[p_4,p_3,p_1]),
    %cube(p_3,[p_1,p_2,p_4]),
    %cube(p_3,[p_1,p_4,p_2]),
    %cube(p_3,[p_2,p_1,p_4]),
    %cube(p_3,[p_2,p_4,p_1]),
    %cube(p_3,[p_4,p_1,p_2]),
    %cube(p_3,[p_4,p_2,p_1]),
    %cube(p_4,[p_1,p_2,p_3])
    %cube(p_4,[p_1,p_3,p_2]),
    %cube(p_4,[p_2,p_1,p_3]),
    %cube(p_4,[p_2,p_3,p_1]),
    %cube(p_4,[p_3,p_1,p_2]),
    %cube(p_4,[p_3,p_2,p_1])
  ],
  learn(Pos,Neg).


%Background
% angle_90(Plane, []).
% angle_90(Plane, [Plane1|RestPlanes]):-
%   angle_90_aux(Plane, Plane1),
%   angle_90(Plane, RestPlanes).

%Target
% cube/2.
% cube(first, [head|tail]):-
%   angle_90_aux(first, head),
%   angle_90(head, tail).

% cube/1.
% cube([Head|Tail]) :-



