import React, { memo, useEffect, useMemo } from "react";
import { Route } from "react-router-dom";
import nprogress from "nprogress";

import "nprogress/nprogress.css";

const LoadRoute = (props) => {
  useMemo(() => {
    nprogress.start();
  }, []);

  useEffect(() => {
    nprogress.done();
  }, []);

  return <Route {...props} />;
};

export default memo(LoadRoute);
