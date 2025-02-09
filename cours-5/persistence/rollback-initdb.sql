-- 3. Création de la table `users` si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,  -- identifiant unique auto-incrémenté
    name VARCHAR(100),
    age INT
);