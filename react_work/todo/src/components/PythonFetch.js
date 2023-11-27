import React, {useState} from 'react';

const PythonFetch = ()=>{
    const [result,setResult] = useState(' ');
    const [myStyle,setMyStyle] = useState({ 'display':'block'} );
    const chartData = ()=>{
        setMyStyle({ 'display':'none'});
        // get 방식...
        fetch('http://127.0.0.1:5000/chartData')
        .then((res)=>{
            return res.text();
        })
        .then((ar)=>{
            setResult(ar);
            setMyStyle({ 'display':'block'});
        })
    }
    const knnData = ()=>{
        const MyData = {
            "len":"10",
            "wei":"11"
        }
        setMyStyle({ 'display':'none'});
        // get 방식...
        fetch('http://127.0.0.1:5000/',{
            method:"POST",
            headers:{ 
                'Content-Type':'application/json'
            },
            body: JSON.stringify(MyData)
        })
        .then((res)=>{
            return res.json();
        })
        .then((ar)=>{
            setResult(JSON.stringify(ar));
            setMyStyle({ 'display':'block'});
        })
    }
    return (
        <div>
            <h1>PythonFetch</h1>
            <div>
                <h1>결과</h1>
                <p>{result}</p>
            </div>
            <button onClick={chartData} style={myStyle}>chartData</button>
            <button>pieData</button>
            <button>barData</button>
            <button onClick={knnData}>KNN</button>
        </div>
    );
}

export default PythonFetch;