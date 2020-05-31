:- use_module('../metagol').

%% metagol settings
body_pred(poly/1).
body_pred(joins/2).
body_pred(sides_4/1).
body_pred(allSides_4/1).
body_pred(angle_90_aux/2).
body_pred(angle/2).

% Poly - defines a face (polygon), of a 3D object
% Grouped to define an object as seen in a photo
% Joins - Which faces (polygons) share an edge

%% background knowledge
poly(c_1).                poly(c_4).                   
poly(c_2).                poly(c_5).               
poly(c_3).                poly(c_6).

poly(p_1).                poly(t_1). 
poly(p_2).                poly(t_2).
poly(p_3).                poly(t_3).
poly(p_4).

joins(c_1,c_2).           joins(c_4,c_5).       
joins(c_1,c_3).           joins(c_4,c_6).        
joins(c_2,c_3).           joins(c_5,c_6).   
joins(c_2,c_1).           joins(c_5,c_4).       
joins(c_2,c_1).           joins(c_6,c_4).        
joins(c_3,c_2).           joins(c_6,c_5). 

joins(p_1,p_2).           joins(t_1,t_2).
joins(p_1,p_3).           joins(t_1,t_3).
joins(p_1,p_4).           joins(t_2,t_3).
joins(p_2,p_3).           joins(t_2,t_1).
joins(p_3,p_4).           joins(t_2,t_1).
joins(p_2,p_1).           joins(t_3,t_2).
joins(p_3,p_1).           
joins(p_4,p_1).
joins(p_3,p_2).            
joins(p_4,p_3).

angle_90_aux(c_1,c_2).    angle_90_aux(c_4,c_5).   
angle_90_aux(c_1,c_3).    angle_90_aux(c_4,c_6).   
angle_90_aux(c_2,c_3).    angle_90_aux(c_5,c_6).
angle_90_aux(c_2,c_1).    angle_90_aux(c_5,c_4). 
angle_90_aux(c_3,c_1).    angle_90_aux(c_6,c_4).    
angle_90_aux(c_3,c_2).    angle_90_aux(c_6,c_5).

angle_90_aux(p_1,p_2).    angle_90_aux(t_1,t_2).        
angle_90_aux(p_1,p_3).    angle_90_aux(t_1,t_3).          
angle_90_aux(p_1,p_4).    angle_90_aux(t_2,t_3).
angle_90_aux(p_2,p_1).    angle_90_aux(t_2,t_1).       
angle_90_aux(p_3,p_1).    angle_90_aux(t_3,t_1).          
angle_90_aux(p_4,p_1).    angle_90_aux(t_3,t_2).
% \+ angle_90_aux(p_2,p_3).
% \+ angle_90_aux(p_3,p_4).


% sides(c_1, 4).      sides(c_4, 4).     
% sides(c_2, 4).      sides(c_5, 4).       
% sides(c_3, 4).      sides(c_6, 4).
           
% sides(p_1, 6).      sides(t_1, 3). 
% sides(p_2, 4).      sides(t_2, 4).
% sides(p_3, 4).      sides(t_3, 4).
% sides(p_4, 4).

sides_4(c_1).      sides_4(c_4).     
sides_4(c_2).      sides_4(c_5).       
sides_4(c_3).      sides_4(c_6).
           
% sides(p_1, 6).      sides(t_1, 3). 
sides_4(p_2).      sides_4(t_2).
sides_4(p_3).      sides_4(t_3).
sides_4(p_4).

%Background
angle(First, []).
angle(First, [Second|Tail]):-
  angle_90_aux(First, Second),
  angle(Second, Tail).


% allSides(Num, []).
% allSides_4(Num, [H|T]):-
%   sides(H, Num),
%   allSides(Num, T).

allSides_4([]).
allSides_4([H|T]):-
  sides_4(H),
  allSides_4(T).

%% metarules
metarule([P,Q], [P,A,B], [[Q,A,B]]). %% identity
metarule([P,Q], [P,A,B], [[Q,B,A]]). %% inverse
metarule([P,Q,R], [P,A,B], [[Q,A],[R,A,B]]). %% precon
metarule([P,Q,R], [P,A,B], [[Q,A,B],[R,B]]). %% postcon


%% learning task
:-
  %% positive examples
  Pos = [
    cube(c_1,[c_2,c_3]),
    cube(c_2,[c_1,c_3]),   %Not sure if nessesary but shows shape can be expressed in any order 
    cube(c_3,[c_2,c_1]),
    cube(c_5,[c_4,c_6])
  ],
  %% negative examples
  Neg = [
    cube(p_1,[p_2,p_3,p_4]),
    cube(p_2,[p_1,p_4,p_3]),
    cube(t_1,[t_2,t_3]),
    cube(t_2,[t_1,t_3])
  ],
  learn(Pos,Neg).

%Target
%   cube/2.
%   cube(First, List):-
%     angle(First, List),
%     allSides_4(first),
%     allSides_4(list)

%Result
%  cube/2.
%    cube(A,B):-sides_4(A),cube_1(A,B).
%    cube_1(A,B):-angle(A,B),allSides_4(B).