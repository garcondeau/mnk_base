import React, { useState, useEffect } from "react";
import axios from "axios";
import Logo from "../logo/Logo";

import { StyledContainer } from "../../styles/styledContainer";
import { HeaderWrapper, StyledHeaderContainer } from "./styledHeader";

const Header = () => {
  const [info, setInfo] = useState();

  const fetchInfo = () => {
    axios
      .get("/app-info")
      .then((response) => {
        setInfo(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };
  useEffect(() => {
    fetchInfo();
  }, []);
  return (
    <HeaderWrapper>
      <StyledHeaderContainer>
        <Logo />
        <div className="header__version">{info && info[1] + " " + info[0]}</div>
      </StyledHeaderContainer>
    </HeaderWrapper>
  );
};

export default Header;
