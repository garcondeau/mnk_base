import React, { useEffect, useState } from "react";
import { StyledSuppliersContainer } from "../styledSuppliers";

const CreateSupplierWrapper = () => {
  const [files_n, setFiles_n] = useState(1);
  const [files_arr, setFiles_arr] = useState([])

  const handleChange = (e) => {
    setFiles_n(e.target.value);
    for (let i = 1; i <= e.target.value; i++) {
      files_arr.push(i);
    }
    console.log(files_arr);
  };

  useEffect(() => {
    files_arr.push(files_n);
  }, []);

  return (
    <StyledSuppliersContainer>
      <form action="post">
        <label>
          Supplier name
          <input type="text" name="name" id="" />
        </label>
        <label>
          Files amount
          <input
            min={1}
            onChange={(e) => handleChange(e)}
            type="number"
            name="files_count"
            value={files_n}
          />
        </label>
        {files_arr.map((id) => (
          <>
            <label>
              FTP URL
              <input type="text" name="url" id="" />
            </label>
            <label>
              Pass encoding errors
              <input type="checkbox" name="encoding" id="" />
            </label>
            <label>
              Separator
              <select name="sep">
                <option value=";">;</option>
                <option value="\t">\t</option>
                <option value=",">,</option>
              </select>
            </label>
            <label>
              Remove default header
              <input type="checkbox" name="header" id="" />
            </label>
            <label>
              Use low memory
              <input type="checkbox" name="memory" id="" />
            </label>
            <label>
              Archive type
              <select name="sep">
                <option value="infer">No</option>
                <option value="zip">zip</option>
                <option value="gzip">gzip</option>
              </select>
            </label>
            <label>
              Skip bad lines
              <input type="checkbox" name="error_bad_lines" id="" />
            </label>
          </>
        ))}
      </form>
    </StyledSuppliersContainer>
  );
};

export default CreateSupplierWrapper;
