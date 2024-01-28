-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].
two_sum(Nums, Target) ->
    L=lists:seq(0,length(Nums)-1),
    N=lists:zip(L,Nums),
    Ti = [[Xi,Yi] || {Xi,X}<-N,{Yi,Y}<- N--[{Xi,X}],X+Y == Target],
    hd(Ti).
