import React, {useState, useEffect} from 'react';


export default function Test(){
    const [test, setTest] = useState('something');
    useEffect(()=>{
        console.log('console output');
    },[test]);
    return(
        <div>
        <h2>Abcd</h2>
        </div>
    )
}