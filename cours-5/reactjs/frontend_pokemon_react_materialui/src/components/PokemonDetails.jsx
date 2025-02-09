import React from "react";
import {
  Card,
  CardContent,
  Typography,
  CardMedia,
  Chip,
  Grid,
  Stack,
} from "@mui/material";
import typeColors from "../styles/typeColors.js";

function PokemonDetails({ pokemon }) {
  if (!pokemon) return <Typography>Aucun Pokémon sélectionné</Typography>;

  return (
    <Card>
      <CardContent>
        <Typography variant="h4" component="div">
          {pokemon.name.toUpperCase()} <span>#{pokemon.id}</span>
        </Typography>

        <CardMedia
          component="img"
          image={pokemon.sprites.front_default}
          alt={pokemon.name}
          sx={{ width: 150, height: 150, margin: "auto" }}
        />

        <Typography variant="body1">
          Poids : {pokemon.weight / 10} kg
        </Typography>
        <Typography variant="body1">
          Taille : {pokemon.height / 10} m
        </Typography>

        <Stack
          direction="row"
          spacing={1}
          sx={{ marginTop: 1 }}
          justifyContent="center"
        >
          {pokemon.types.map((typeInfo) => (
            <Chip
              key={typeInfo.type.name}
              label={typeInfo.type.name.toUpperCase()}
              sx={{
                backgroundColor: typeColors[typeInfo.type.name],
                color: "white",
              }}
            />
          ))}
        </Stack>

        <Typography variant="h6" sx={{ marginTop: 2 }}>
          Statistiques
        </Typography>
        {pokemon.stats.map((stat) => (
          <Typography key={stat.stat.name} variant="body2">
            {stat.stat.name.replace("-", " ").toUpperCase()} : {stat.base_stat}
          </Typography>
        ))}
      </CardContent>
    </Card>
  );
}

export default PokemonDetails;
