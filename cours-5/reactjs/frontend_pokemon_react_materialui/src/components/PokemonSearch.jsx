import React, { useState } from "react";
import { TextField, Button, Box, Typography } from "@mui/material";
import API from "../api/apiClient.js";

function PokemonSearch({ setPokemon }) {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      alert("Veuillez entrer un nom ou un ID de Pokémon.");
      return;
    }

    try {
      const response = await API.get(`pokemon/${searchTerm.toLowerCase()}`);
      setPokemon(response.data);
    } catch (error) {
      const errorMessage = error.response
        ? `Erreur ${error.response.status}: ${
            error.response.data || "Erreur inconnue"
          }`
        : "Erreur de réseau";
      alert(errorMessage);
    }
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: 2,
        alignItems: "center",
      }}
    >
      <Typography variant="h6">Rechercher un Pokémon :</Typography>
      <TextField
        id="search-input"
        label="Nom ou ID"
        variant="outlined"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <Button variant="contained" onClick={handleSearch}>
        Chercher
      </Button>
    </Box>
  );
}

export default PokemonSearch;
