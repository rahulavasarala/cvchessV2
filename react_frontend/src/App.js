//you can import css files in this bitch
import {useState, useEffect} from 'react'
import ChessBoard from './Chessboard/ChessBoard';
import "./App.css";

const dummy_api = [["wp","wp","wp", "wp", "wp", "wp", "wp", "wp"],
["wp","wp","wp", "e", "wp", "wp", "wp", "wp"],
["wp","wp","wp", "wp", "wp", "wp", "wp", "wp"],
["wp","wp","wp", "wp", "wp", "wp", "wp", "wp"],
["wp","wp","wp", "wp", "wp", "wp", "wp", "wp"],
["wp","wp","wp", "wp", "wp", "wp", "wp", "wp"],
["wp","wp","wp", "wp", "wp", "wp", "wp", "wp"],
["wp","wp","wp", "wp", "wp", "wp", "wp", "wp"]];

function App() {

  const [chess_data, setdata] = useState(dummy_api)

  //make some code that logs update in the console every 5 seconds


  useEffect(() => {

    const interval = setInterval(() => {
      fetch("./chess_data").then(

        res => res.json()
      ).then(
  
        data => {
          setdata(data)
          console.log("This is the data: ", data)
        }
      )
    }, 1000);
  
    return () => clearInterval(interval);
    
  }, []);

  return(

    <>
      <h1 id="Title">Chess Display App</h1>

      <div id="board">
        
        <ChessBoard board_data={chess_data}/>
      </div>

    </>
    


  ); 
}

export default App;
