import { useState } from "react";
import PropTypes from "prop-types";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";

import {
  SearchWrapper,
  SearchRow,
  SearchButton,
} from "../styles/PokemonSearch.styles";

import API from "../api/apiClient";

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
    <SearchWrapper elevation={0}>
      <Typography variant="h6" align="center" sx={{ mb: 2 }}>
        Rechercher un Pokémon :
      </Typography>

      <SearchRow>
        <TextField
          label="Nom ou ID"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        <SearchButton variant="contained" onClick={handleSearch}>
          Chercher
        </SearchButton>
      </SearchRow>
    </SearchWrapper>
  );
}

export default PokemonSearch;

PokemonSearch.propTypes = {
  setPokemon: PropTypes.func.isRequired,
};
