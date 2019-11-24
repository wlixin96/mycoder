clear;clc

%% 左右合并: 行数相同
A=ones(3,4)
B=zeros(3,2)
C=[A,B]

%% 上下合并: 列数相同
% A=ones(2,4)
% B=zeros(4,4)
% C=[A;B]

%% 多个矩阵合并
% A=zeros(2,2)
% B=rand(2,3)
% C=eye(3,3)
% D=ones(3,2)
% E=[A,B;C,D]