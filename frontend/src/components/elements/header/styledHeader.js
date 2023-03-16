import styled from "styled-components";
import { StyledContainer } from "../../styles/styledContainer";

export const HeaderWrapper = styled.div`
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    /* background: url('https://preview.redd.it/gkk5s1iw29oz.jpg?auto=webp&s=25d1287ec7e2c3c99364cba5ea8df82f42d72b30'); */
    /* background-position-y: 340px; */
    /* background-size: cover; */
    background-color: #ffffff;
    box-shadow: 3px 3px 3px rgba(0,0,0,0.1);
    color: #3f3f3f;
`
export const StyledHeaderContainer = styled(StyledContainer)`
    display: flex;
    justify-content: space-between;
    .header {
        &__version {
            font-size: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            opacity: 0.5;
        }
    }
`