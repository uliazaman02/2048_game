import React, { Component } from 'react';
import Tile from './Tile';

export default class Board extends Component {
    renderTile(i){
        return <Tile/>
    }
    render() {
        return (
            <div>
                <div className="row">
                    {this.renderTile(0)}
                    {this.renderTile(1)}
                    {this.renderTile(2)}
                    {this.renderTile(3)}
                </div>
                <div className="row">
                    {this.renderTile(4)}
                    {this.renderTile(5)}
                    {this.renderTile(6)}
                    {this.renderTile(7)}
                </div>
                <div className="row">
                    {this.renderTile(8)}
                    {this.renderTile(9)}
                    {this.renderTile(10)}
                    {this.renderTile(11)}
                </div>
                <div className="row">
                    {this.renderTile(12)}
                    {this.renderTile(13)}
                    {this.renderTile(14)}
                    {this.renderTile(15)}
                </div>
            </div>
        )
    }
}