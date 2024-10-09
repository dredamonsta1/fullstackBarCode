import React, { Component } from "react";
import Inventory from "./Inventory";
import {
    BrowserRouter as router,
    Switch,
    Route,
    Link,
    redirect,
    Router,
} from "react-router-dom";

function HomePage(path) {

    return (
        <>
                        <p>refresh please</p>
                    
            <Inventory />
        </>
        
    )

}

export default HomePage;