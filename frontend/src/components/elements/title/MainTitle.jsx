import React from "react";

import { StyledMainTitleWrapper } from "./styledTitle";
import { Header } from "@fluentui/react-northstar";

const MainTitle = ({ text, description }) => {
  return (
    <StyledMainTitleWrapper>
      <Header color="grey" content={text} description={description} />
    </StyledMainTitleWrapper>
  );
};

export default MainTitle;
