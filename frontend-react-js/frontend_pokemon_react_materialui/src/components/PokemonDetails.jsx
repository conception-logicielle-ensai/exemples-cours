import PropTypes from "prop-types";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import CardMedia from "@mui/material/CardMedia";

import {
  PokemonCard,
  SpriteContainer,
  TypeChip,
  StatsContainer,
} from "../styles/PokemonDetails.styles";

import typeColors from "../styles/typeColors";

function PokemonDetails({ pokemon }) {
  if (!pokemon) {
    return <p></p>;
  }

  return (
    <PokemonCard>
      <Typography variant="h5" fontWeight="bold">
        {pokemon.name.toUpperCase()}{" "}
        <Typography
          component="span"
          sx={{ fontSize: "0.9rem", color: "text.secondary" }}
        >
          #{pokemon.id}
        </Typography>
      </Typography>

      <SpriteContainer>
        <CardMedia
          component="img"
          image={pokemon.sprites.front_default}
          alt={pokemon.name}
          sx={{ width: 120 }}
        />
      </SpriteContainer>

      <Typography>Poids : {pokemon.weight / 10} kg</Typography>
      <Typography>Taille : {pokemon.height / 10} m</Typography>

      <Stack direction="row" spacing={1} justifyContent="center">
        {pokemon.types.map((typeInfo) => (
          <TypeChip
            key={typeInfo.type.name}
            label={typeInfo.type.name.toUpperCase()}
            sx={{
              backgroundColor: typeColors[typeInfo.type.name],
            }}
          />
        ))}
      </Stack>

      <StatsContainer>
        <Typography variant="h6" align="center">
          Statistiques
        </Typography>

        {pokemon.stats.map((stat) => (
          <Typography key={stat.stat.name} variant="body2">
            {stat.stat.name.replace("-", " ").toUpperCase()} : {stat.base_stat}
          </Typography>
        ))}
      </StatsContainer>
    </PokemonCard>
  );
}

export default PokemonDetails;

PokemonDetails.propTypes = {
  pokemon: PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    height: PropTypes.number.isRequired,
    weight: PropTypes.number.isRequired,

    sprites: PropTypes.shape({
      front_default: PropTypes.string,
    }).isRequired,

    types: PropTypes.arrayOf(
      PropTypes.shape({
        slot: PropTypes.number.isRequired,
        type: PropTypes.shape({
          name: PropTypes.string.isRequired,
        }).isRequired,
      })
    ).isRequired,

    stats: PropTypes.arrayOf(
      PropTypes.shape({
        base_stat: PropTypes.number.isRequired,
        stat: PropTypes.shape({
          name: PropTypes.string.isRequired,
        }).isRequired,
      })
    ).isRequired,
  }).isRequired,
};
