import './App.css';
import Person from './components/Person';
import PythonFetch from './components/PythonFetch';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <PythonFetch/>
        <Person name="홍길동" age={10}/>
        <Person name="김길동" age={20}/>
        <Person name="이길동" age={30}/>
      </header>
    </div>
  );
}

export default App;
