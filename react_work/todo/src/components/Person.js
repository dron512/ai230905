import React, {useState} from 'react';

const Person = ({name,age})=>{
    const [myAge,setMyAge] = useState(age);
    const addClick = ()=>{
        setMyAge(myAge+1);
    }
    const subClick = function(){
        setMyAge(myAge-1);
    }
    return (
        <div>
            <ul>
                <li><h1>Person</h1></li>
                <li>이름 = {name}</li>
                <li>나이 = {myAge}</li>
                <button onClick={addClick}>나이증가</button>
                <button onClick={subClick}>나이감소</button>
            </ul>
        </div>
    );
}

export default Person;