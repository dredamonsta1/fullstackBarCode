import React, { Component } from "react";
import Inventory from "./Inventory";
import {
    BrowserRouter as router,
    Switch,
    Route,
    Link,
    redirect,
} from "react-router-dom";

function HomePage() {

    return (
        <>
            <Inventory />
        </>
        
    )

}

export default HomePage;