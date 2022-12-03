import React from 'react'
import "./Tile.css";

//['black-bishop', 'black-king', 'black-knight', 'black-pawn', 'black-queen', 'black-rook', 'white-bishop', 'white-king', 'white-knight', 'white-pawn', 'white-queen', 'white-rook']

const piece_id_to_image = {}
piece_id_to_image[3] = "./pieces/black_pawn.png";
piece_id_to_image[2] = "./pieces/black_knight.png";
piece_id_to_image[0] = "./pieces/black_bish.png";
piece_id_to_image[1] = "./pieces/black_king.png";
piece_id_to_image[4] = "./pieces/black_queen.png";
piece_id_to_image[5] = "./pieces/black_rook.png";
piece_id_to_image[9] = "./pieces/white_pawn.png";
piece_id_to_image[8] = "./pieces/white_knight.png";
piece_id_to_image[6] = "./pieces/white_bish.png";
piece_id_to_image[10] = "./pieces/white_queen.png";
piece_id_to_image[7] = "./pieces/white_king.png";
piece_id_to_image[11] = "./pieces/white_rook.png";
piece_id_to_image[-1] = undefined;


export default function Tile({num, piece_id}) {
  
  if(num % 2 == 0) {
    return <div className="tile white_tile"><img src={piece_id_to_image[piece_id]}/></div>
  }else {
    return <div className="tile brown_tile"><img src={piece_id_to_image[piece_id]}/></div>
  }
}

