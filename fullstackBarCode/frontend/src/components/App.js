import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <HomePage />
            // <h1>Resting React Code Dre</h1>
        )
    }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);