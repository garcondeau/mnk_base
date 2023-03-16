import React from "react";
import {
  Dialog,
  DialogContent,
  DialogBody,
  DialogTitle,
  DialogSurface,
  DialogActions,
  DialogTrigger,
} from "@fluentui/react-components/unstable";

import { Button } from "@fluentui/react-northstar";

const ConfirmationModal = ({
  title,
  message,
  handler,
  visible,
  setVisible,
  setLoading,
}) => {
  return (
    <Dialog open={visible} modalType="alert">
      <DialogSurface>
        <DialogBody>
          <DialogTitle>{title ? title : "Confirmation"}</DialogTitle>
          <DialogContent>{message}</DialogContent>
          <DialogActions>
            <DialogTrigger>
              <Button
                onClick={() => (setVisible(false), setLoading(false))}
                appearance="secondary"
              >
                Close
              </Button>
            </DialogTrigger>
            <Button primary onClick={() => (handler(), setVisible(false))}>
              Submit
            </Button>
          </DialogActions>
        </DialogBody>
      </DialogSurface>
    </Dialog>
  );
};

export default ConfirmationModal;
