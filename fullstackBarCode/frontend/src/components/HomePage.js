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
                        <p>this is the home page</p>
                    
            <Inventory />
        </>
        
    )

}

export default HomePage;