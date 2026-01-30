import React, { useState } from "react";
import { Container, Typography } from "@mui/material";
import PokemonSearch from "./components/PokemonSearch";
import PokemonDetails from "./components/PokemonDetails";

const App = () => {
  const [pokemon, setPokemon] = useState(null);

  return (
    <Container sx={{ textAlign: "center", marginTop: 4 }}>
      <Typography variant="h3">Pokédex</Typography>
      <PokemonSearch setPokemon={setPokemon} />
      <PokemonDetails pokemon={pokemon} />
    </Container>
  );
};

export default App;
