import React, { useState, useEffect } from "react";
import axios from "axios";
import { StyledSuppliersContainer } from "../styledSuppliers";

import {
  Card,
  CardHeader,
  CardBody,
  Flex,
  Text,
  Avatar,
  Skeleton,
  FlexItem,
  Grid,
} from "@fluentui/react-northstar";
import { Divider, Badge } from "@fluentui/react-components";

const SupplierDetails = ({ match }) => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(false);

  const fetchSupplier = () => {
    axios
      .get("/suppliers/" + match.params.supplier)
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };
  useEffect(() => {
    fetchSupplier();
  }, []);

  data && console.log(data);

  return (
    <>
      <StyledSuppliersContainer>
        <Card fluid>
          {data ? (
            <>
              <CardHeader>
                <Flex gap="gap.small">
                  <Avatar
                    icon={data.name}
                    image={
                      "https://avatars.dicebear.com/api/initials/:" +
                      data.name +
                      ".svg"
                    }
                    size="large"
                    status={{
                      color: data.status ? "green" : "red",
                      title: data.status ? "active" : "disabled",
                    }}
                  />
                  <Flex column>
                    <Text content={data.name} weight="bold" />
                    <Text
                      content={"Last update: " + data.updated}
                      size="small"
                    />
                  </Flex>
                </Flex>
              </CardHeader>
              <Divider>
                <Text content="Files" size="largest" weight="bold" />
              </Divider>
              <Flex gap="gap.large" space="between" wrap>
                {data.files &&
                  data.files.map((file) => (
                    <FlexItem grow>
                      <Card elevated>
                        <CardHeader>
                          <Flex gap="gap.small">
                            <Flex column>
                              <Badge>
                                <Text
                                  content={`${file.file_name}.${file.file_type}`}
                                  weight="bold"
                                  size="medium"
                                />
                              </Badge>
                            </Flex>
                          </Flex>
                        </CardHeader>
                        <CardBody>
                          {Object.entries(file).map((value) => (
                            <Flex>
                              {console.log(value)}
                              <Text weight="bold" content={value[0]} />
                              {
                                value[1].map((val) => (
                                    <small>val</small>
                                ))
                              }
                            </Flex>
                          ))}
                        </CardBody>
                      </Card>
                    </FlexItem>
                  ))}
              </Flex>
            </>
          ) : (
            <Skeleton animation="wave">
              <Flex gap="gap.small">
                <Skeleton.Shape round width="32px" height="32px" />
                <div>
                  <Skeleton.Line width="200px" />
                  <Skeleton.Line width="150px" />
                </div>
              </Flex>
            </Skeleton>
          )}
        </Card>
      </StyledSuppliersContainer>
    </>
  );
};

export default SupplierDetails;
