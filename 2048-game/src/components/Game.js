import React, { Component } from 'react';
import Board from './Board';

export default class Game extends Component {
    constructor(props) {
        super(props);
        this.state = {
            move: "",
            moveNum: 0,
            history: [
                { tiles: Array(16).fill(null)}
            ]
        }
    }
    render() {
        const history = this.state.history;
        const current = history[this.state.moveNum];

        return (
            <div className="game">
                <div className="game_board">
                    <Board tiles={current.tiles}/>
                </div>
            </div>
        )
    }
}