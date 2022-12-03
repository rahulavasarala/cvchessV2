import React from 'react'
import "./chessboard.css";
import Tile from '../Tile/Tile';

const board_width = 8;
const board_height = 8;

export default function ChessBoard({board_data}) {

    let board = [];

    for(var i = 0; i < board_height; i++) {
        for(var j = 0; j < board_width; j++) {
            var number = i + j;
            board.push(<Tile num={number} piece_id={board_data[i][j]}/>)
        }
    } 


    return (
        <div id="chessboard">{board}</div>
    )
}
