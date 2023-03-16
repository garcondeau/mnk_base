import {createGlobalStyle} from "styled-components";

const mainFont = "Segoe UI, sans-serif";
const mainFontSize = "14px";

export const GlobalStyle = createGlobalStyle`
  * {
    box-sizing: border-box;
  }

  html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    color: #656565;
    font-family: ${mainFont};
    font-size: ${mainFontSize};
    letter-spacing: 0.2px;
    scroll-behavior: smooth;
  }

  .im_being_held_in_sexual_slavery_call_911{
    padding-top: 400px;
    width: 100%;
  }

  h1, h2, h3, h4, h5, h6, p, span, select, input {
    margin: 0;
    padding: 0;
    border: none;
    outline: none;
  }

  ul, ol {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  input::-webkit-search-decoration,
  input::-webkit-search-cancel-button,
  input::-webkit-search-results-button,
  input::-webkit-search-results-decoration {
    display: none;
  }
  input {
    border: 1px solid rgba(0,0,0,0.5);
  }

  button {
    padding: 0;
    font: inherit;
    background-color: transparent;
    cursor: pointer;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  a:hover, a:focus, a:active {
    text-decoration: none;
  }
  
  .default-link {
    color: #c8b19b;
    &:hover {
      text-decoration: underline;
    }
  }
  `