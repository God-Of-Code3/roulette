import React from 'react';
import ReactDOM from 'react-dom';

const App = () => {

    return (
        <div className="">
            <h1>Наконец-то!!!</h1>
            <button className="btn btn-primary">Hello</button>
            <input type="text" className="form-control" />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt velit, numquam error deleniti veniam, omnis commodi nobis porro hic odio doloribus deserunt maxime in a voluptatem provident soluta sapiente ipsum?</p>
        </div>
    );
}

ReactDOM.render(<App></App>, document.getElementById('app'));

export default App;