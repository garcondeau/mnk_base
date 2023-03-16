import React from "react";
import Logo from "../logo/Logo";

import { HeaderWrapper, StyledHeaderContainer } from "./styledHeader"

const Header = () => {
    return(
        <HeaderWrapper>
            <StyledHeaderContainer>
                <Logo/>
            </StyledHeaderContainer>
        </HeaderWrapper>
    )
}

export default Header;