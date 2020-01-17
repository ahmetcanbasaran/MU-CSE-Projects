%move(State1, Move, State2): Makingmove in State1 results in State2
%a state is represented by: state(Monkey Horizontal, Monkey Vertical, Boz Position, HasBanana)
move(state(middle, onbox, middle,hasnot), grasp, state(middle,onbox,middle,has)).
move(state(P,onflooe,P,H), climb, state(P, onbox, P2, H)).
move(state(P1, onfloor,P1,H), push(P1,P2), state(P2,onfloor,P2,H)).
move(state(P1,onfloor,B,H), walk(P1,P2),state(P2,onfloor,B,H)).
canget(state(_,_,_,has)).
canget(State1):-move(State1,Move,State2),canget(State2)
%canget(State): monkey can get banana starting from State