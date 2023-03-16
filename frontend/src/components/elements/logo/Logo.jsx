import React from "react";

import { StyledLogoWrapper } from "./styledLogo";

import logo from "../../../assets/logo.svg";

const Logo = () => {
  return (
    <StyledLogoWrapper>
      <img src={logo} alt="logo" />
      PELAGEIA
    </StyledLogoWrapper>
  );
};

export default Logo;
