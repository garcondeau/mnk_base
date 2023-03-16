import React, { useState, useEffect } from "react";
import axios from "axios";
import Filter from "../../elements/filter/FilterContianer";
import ConfirmationModal from "../../elements/modal/ConfirmationModal";
import MainTitle from "../../elements/title/MainTitle";
import { NavLink, useHistory } from "react-router-dom";

import {
  SuppliersListHead,
  StyledSuppliersContainer,
  SuppliersList,
  SuppliersListBody,
  SupplersListRow,
  SuppliersListCol,
} from "../styledSuppliers";
import { Button, Checkbox, Tooltip } from "@fluentui/react-northstar";
import { TableHeaderCell } from "@fluentui/react-components/unstable";
import { EditFilled } from "@fluentui/react-icons";

const SuppliersListContainer = () => {
  const [suppliers, setSuppliers] = useState({});
  const [loading, setLoading] = useState(false);
  const [visible, setVisible] = useState(false);
  const [status, setStatus] = useState();
  const [editSupplier, setEditSupplier] = useState();

  const handleChange = (sup_status, supplier) => {
    setLoading(true);
    setVisible(true);
    setStatus(!sup_status);
    setEditSupplier(supplier);
  };

  const fetchSuppliers = () => {
    axios
      .get("/suppliers")
      .then((response) => {
        response.data.map((supplier) =>
          setSuppliers((prevState) => ({
            ...prevState,
            [supplier.name]: supplier.status,
          }))
        );
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const modalVisible = () => {
    setVisible(false);
  };

  const updateStatus = () => {
    setLoading(true);
    axios
      .post("/suppliers", {
        status: status,
        supplier: editSupplier,
      })
      .then((response) => {
        setLoading(false);
        setSuppliers((prevState) => ({
          ...prevState,
          [response.data.supplier]: response.data.status,
        }));
      })
      .catch((error) => {
        console.log(error);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchSuppliers();
  }, []);
  return (
    <>
      <ConfirmationModal
        setLoading={setLoading}
        visible={visible}
        setVisible={() => modalVisible()}
        message={
          "Do you want to change activity status of " + editSupplier + "?"
        }
        handler={() => updateStatus()}
      />
      <StyledSuppliersContainer>
        <MainTitle text="Suppliers list" />
        <Filter createItem />
        <SuppliersList>
          <SuppliersListHead>
            <SupplersListRow>
              <TableHeaderCell>Active</TableHeaderCell>
              <TableHeaderCell>Supplier name</TableHeaderCell>
              <TableHeaderCell />
            </SupplersListRow>
          </SuppliersListHead>
          <SuppliersListBody>
            {suppliers &&
              Object.keys(suppliers).map((supplier, key) => (
                <SupplersListRow key={key}>
                  <SuppliersListCol>
                    <Checkbox
                      toggle
                      disabled={loading}
                      supplier={supplier}
                      checked={suppliers[supplier]}
                      onChange={() => handleChange(suppliers[supplier], supplier)}
                    />
                  </SuppliersListCol>
                  <SuppliersListCol className="supplier_name">
                    <div className="supplier_name">
                      {supplier.replace("_", " ")}
                    </div>
                  </SuppliersListCol>
                  <SuppliersListCol>
                    <Tooltip content="Edit supplier" relationship="label">
                      <Button
                        as={NavLink}
                        to={`/suppliers/${supplier}`}
                        tinted
                        circular
                        icon={<EditFilled />}
                        size="small"
                        // onClick={}
                      />
                    </Tooltip>
                  </SuppliersListCol>
                </SupplersListRow>
              ))}
          </SuppliersListBody>
        </SuppliersList>
      </StyledSuppliersContainer>
    </>
  );
};

export default SuppliersListContainer;
