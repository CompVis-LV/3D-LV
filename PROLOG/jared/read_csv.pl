% :- csv_read_file('../../Datasets/cube/0_file.csv',Rows,[functor(table)]),
% maplist(assert,Rows).

%%%%%%%%%%%%%%%%%%%%%%%

:- use_module(library(apply)).
:- use_module(library(csv)).

get_rows_data(File, Lists):-
  csv_read_file(File, Rows, []),
  rows_to_lists(Rows, Lists).

rows_to_lists(Rows, Lists):-
  maplist(row_to_list, Rows, Lists).

row_to_list(Row, List):-
  Row =.. [row|List],
  write(Row).
  
read_list([]).
read_list([Head|Tail]) :-
    read_list_head(Head),
    read_list(Tail).

read_list_head(Word):-
    format("~w~n",[Word]).

read_list_head([Head|Tail]):-
    format("~w~n",[Head]),
    read_list_head(Tail).

%%%%%%%%%%%%%%%%%%%%%%%%%
    
% :- [library(csv)].

% :- dynamic samples/3.
% :- dynamic column_keys/1.

% prepare_db(File) :-
%     retractall(column_keys(_)),
%     retractall(samples(_,_,_,_,_)),
%     %( nonvar(File) ; File = '0_file.csv'),
%     forall(read_row(File, Row), store_row(Row)).

% store_row(Row) :-
%     Row =.. [row|Cols],
%     (   column_keys(ColKeys)
%     ->  Cols = [RowKeyDirty|Samples],
%         clean_rowkey(RowKeyDirty, RowKey),
%         maplist(store_sample(RowKey), ColKeys, Samples)
%     ;   assertz(column_keys(Cols))
%     ).

% store_sample(RowKey, ColKey, Sample) :-
%     assertz(samples(RowKey, ColKey, Sample)).

% clean_rowkey(RowKeyDirty, RowKey) :-
%     atom_concat(RowKey, '.CEL', RowKeyDirty).

% read_row(File, Row) :-
%     csv_read_file_row(File, Row, [separator(0',), strip(true), convert(true)]),
%     writeln(read_row(Row)).

%%%%%%%%%%%%%%%%%%%%%%%%%%%

% :- dynamic samples/3.

% prepare_db(File) :-
%     ( nonvar(File) ; File = '0_file.csv' ),
%     open(File, read, S),
%     read_row(S, [_Empty|ColKeys]),
%     forall(read_row(S, [RowKeyDirty|Samples]),
%         (   clean_rowkey(RowKeyDirty, RowKey),
%             maplist(store_sample(RowKey), ColKeys, Samples)
%         )),
%     close(S).

% store_sample(RowKey, ColKey, Sample) :-
%     assertz(samples(RowKey, ColKey, Sample)).

% clean_rowkey(RowKeyDirty, RowKey) :- append(RowKey, ".CEL", RowKeyDirty).