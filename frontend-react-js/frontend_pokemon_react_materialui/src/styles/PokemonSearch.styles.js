import { styled } from "@mui/material/styles";
import { Paper, Box, Button } from "@mui/material";

export const SearchWrapper = styled(Paper)(() => ({
  width: "45rem",
  margin: "0 auto",
  padding: "2rem 1rem",
  backgroundColor: "#f0f1f7",
  borderRadius: "2rem",
  boxShadow: "1rem 1rem #aeacb2",
}));

export const SearchRow = styled(Box)(() => ({
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  gap: "1rem",
}));

export const SearchButton = styled(Button)(() => ({
  padding: "12px 24px",
  borderRadius: "2rem",
  backgroundColor: "#7f21ab",
  "&:hover": {
    backgroundColor: "#9b30c8",
  },
}));
