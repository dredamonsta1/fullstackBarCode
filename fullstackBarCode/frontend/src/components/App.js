import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
// import Inventory from "./Inventory";


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <>
                <HomePage />
                <Button
                    title="press me"
                />
            </>
        )
    }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);