const cell = document.getElementById("cell");

var game_board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]];


function generate_piece() {
    var piece = {};
    piece['row'] = Math.floor(Math.random() * (4 - 0) + 0);
    piece['col'] = Math.floor(Math.random() * (4 - 0) + 0);
    piece['val'] = 2;
    return piece;
}

function move_left() {
    
}

function initialize() {
    console.log('Welcome to the 2048 game');
    var piece = generate_piece();
    console.log(piece);
    game_board[piece['row']][piece['col']] = piece['val'];
    // console.log(game_board[0])
    // console.log(game_board[1])
    // console.log(game_board[2])
    // console.log(game_board[3])
    let computerTurn = true;

    // while (true) {
    //     if (computerTurn === true) {
    //         piece = generate_piece();
    //         console.log(piece);
    //         game_board[piece['row']][piece['col']] = piece['val'];
    //         computerTurn = false;
    //         break;
    //     }
    //     computerTurn = true;
    // }
}

initialize();