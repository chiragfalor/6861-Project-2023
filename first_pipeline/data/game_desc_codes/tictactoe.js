var isValidMove = function(state, move) {
    return state[move.x][move.y] === '?';
  };
  
var movePrior = dp.cache(function(state){
return Infer({ model() {
    var move = {
    x: randomInteger(3),
    y: randomInteger(3)
    };
    condition(isValidMove(state, move));
    return move;
}});
});

var assign = function(obj, k, v) {
var newObj = _.clone(obj);
return Object.defineProperty(newObj, k, {value: v})
};

var transition = function(state, move, player) {
var newRow = assign(state[move.x], move.y, player);
return assign(state, move.x, newRow);
};

var diag1 = function(state) {
return mapIndexed(function(i, x) {return x[i];}, state);
};

var diag2 = function(state) {
var n = state.length;
return mapIndexed(function(i, x) {return x[n - (i + 1)];}, state);
};

var hasWon = dp.cache(function(state, player) {
var check = function(xs){
    return _.countBy(xs)[player] == xs.length;
};
return any(check, [
    state[0], state[1], state[2], // rows
    map(first, state), map(second, state), map(third, state), // cols
    diag1(state), diag2(state) // diagonals
]);
});
///
var isDraw = function(state) {
return !hasWon(state, 'x') && !hasWon(state, 'o');
};