import styled from "styled-components";

export const StyledTable = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
`;

export const StyledTableHead = styled.div`
  width: 100%;
  color: #0f0f0f;
  font-weight: 600;
  display: grid;
  ${({ col }) => col && `grid-template-columns: repeat(${col}, 1fr)`};
  border-bottom: 1px solid rgba(0,0,0,0.5)
`;

export const StyledTableHeadCol = styled.div`
  padding: 10px 15px;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const StyledTableRow = styled.div`
  display: grid;
  ${({ col }) => col && `grid-template-rows: repeat(${col}, 1fr)`};
`;

export const StyledTableBody = styled.div`
  display: grid;
  ${({ col }) => col && `grid-template-columns: repeat(${col}, 1fr)`};
`

export const StyledTableCol = styled.div`
  padding: 10px 15px;
  display: flex;
  justify-content: center;
  align-items: center;
  &:nth-child(2n) {
    background: rgba(0, 0, 0, 0.05);
  }
`;
