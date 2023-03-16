import React from "react";

import { StyledFilterWrapper } from "./styledFilter";
import { Button } from "@fluentui/react-northstar";
import { Divider } from "@fluentui/react-components";

const Filter = ({ createItem }) => {
  return (
    <StyledFilterWrapper>
      <div className="filter-actions">
        <Button primary>Filter</Button>
        {createItem && <Button primary>Create item</Button>}
      </div>
      <Divider />
    </StyledFilterWrapper>
  );
};

export default Filter;
