import React, { Suspense } from "react";
import routes from "./routes/routes"
import LoadRoute from "./routes/LoadRoute";
import Header from "./components/elements/header/Header";
import { GlobalStyle } from "./components/styles/globalStyles";
import { BrowserRouter as Router, Redirect, Switch } from "react-router-dom";

import { Loader } from "@fluentui/react-northstar";

import "./App.css";
import "rc-checkbox/assets/index.css";
import "rc-dialog/assets/index.css";

function App() {
  return (
    <Router>
      <Header />
      <Suspense fallback={<Loader/>}>
        <Switch>
          {routes.map((route, i) => (
            <LoadRoute key={i} {...route} />
          ))}
          <Redirect to="/page-not-found" />
        </Switch>
        {/* <img
          className="im_being_held_in_sexual_slavery_call_911"
          src="https://hips.hearstapps.com/digitalspyuk.cdnds.net/17/28/1499875933-twin-peaks-agent-cooper-coffee.gif?resize=480:*"
        /> */}
      </Suspense>
      <GlobalStyle />
    </Router>
  );
}

export default App;
