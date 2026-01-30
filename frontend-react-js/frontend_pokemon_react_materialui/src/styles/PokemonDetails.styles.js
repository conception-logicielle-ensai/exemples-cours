import { styled } from "@mui/material/styles";
import { Card, Box, Chip } from "@mui/material";

export const PokemonCard = styled(Card)(() => ({
  textAlign: "center",
  backgroundColor: "#f8f8f8",
  padding: 16,
  borderRadius: 10,
  boxShadow: "0px 4px 8px rgba(0,0,0,0.2)",
  width: 300,
  margin: "16px auto",
}));

export const SpriteContainer = styled(Box)(() => ({
  display: "flex",
  justifyContent: "center",
  margin: "8px 0",
}));

export const TypeChip = styled(Chip)(() => ({
  color: "white",
  fontWeight: "bold",
}));

export const StatsContainer = styled(Box)(() => ({
  marginTop: 16,
  textAlign: "left",
}));