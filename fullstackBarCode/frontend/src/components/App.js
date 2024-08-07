import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import Inventory from "./Inventory";


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <>
                <HomePage />
                <Inventory />
            </>
        )
    }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);