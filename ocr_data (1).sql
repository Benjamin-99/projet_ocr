-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 17 mai 2022 à 09:45
-- Version du serveur : 10.4.22-MariaDB
-- Version de PHP : 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `ocr_data`
--

-- --------------------------------------------------------

--
-- Structure de la table `carte_grise`
--

CREATE TABLE `carte_grise` (
  `num_immatriculation` varchar(255) NOT NULL,
  `date_immatriculation` varchar(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `adresse` varchar(255) NOT NULL,
  `marque` varchar(255) NOT NULL,
  `version` varchar(255) NOT NULL,
  `code_identification` varchar(255) NOT NULL,
  `categorie` varchar(255) NOT NULL,
  `genre_national` varchar(255) NOT NULL,
  `carrosserie` varchar(255) NOT NULL,
  `cylindre` varchar(255) NOT NULL,
  `puissance` varchar(255) NOT NULL,
  `type_carburant` varchar(255) NOT NULL,
  `date_visite_technique` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `carte_grise`
--

INSERT INTO `carte_grise` (`num_immatriculation`, `date_immatriculation`, `nom`, `prenom`, `adresse`, `marque`, `version`, `code_identification`, `categorie`, `genre_national`, `carrosserie`, `cylindre`, `puissance`, `type_carburant`, `date_visite_technique`) VALUES
('R255GHHJJ', '15/02/2021', 'TALLA', 'Viviane', '5 rue d\'oslo', 'renault megane', '5', 'ZER789', '89', '456', 'VP', '1900', '95', 'GO', '06/07/2022'),
('PRT568', '15/02/2011', 'TERRET', 'Thomas', '4 avenue garibaldi', 'PEUGEOT', '45', 'YU96', '54', '23', 'CI', '1506', '60', 'SU', '12/10/2012'),
('l', 'g', 'df', 'dfff', 'fgggg', 'gg', 'az', 'er', 'yt', 'deed', 'sszs', 'rty', 'aze', 'tyu', 'ffg');

-- --------------------------------------------------------

--
-- Structure de la table `carte_identite`
--

CREATE TABLE `carte_identite` (
  `id_carte` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `sexe` varchar(50) NOT NULL,
  `nationalite` varchar(50) NOT NULL,
  `date_naissance` date NOT NULL,
  `lieu_naissance` varchar(50) NOT NULL,
  `nom_usage` varchar(50) NOT NULL,
  `numero_document` varchar(50) NOT NULL,
  `date_expiration` date NOT NULL,
  `numero_carte` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `carte_identite`
--

INSERT INTO `carte_identite` (`id_carte`, `nom`, `prenom`, `sexe`, `nationalite`, `date_naissance`, `lieu_naissance`, `nom_usage`, `numero_document`, `date_expiration`, `numero_carte`) VALUES
(1, 'MOUAFFO', 'zidane', 'F', 'Francais', '2012-05-01', 'paris', 'takoumbo', '45fg55', '2023-05-24', '345126'),
(5, 'Toukam', 'celine', 'F', 'Camerounaise', '2013-05-01', 'cecec', 'sando', '45fg55', '2030-05-01', '25104'),
(6, 'Ade', 'randy', 'M', 'Nigerien', '2012-04-01', 'bamenda', 'dilane', '87k956', '2028-05-09', '541200'),
(15552, 'MOUAFFO', 'zidane', 'F', 'Francais', '2012-05-01', 'paris', 'takoumbo', '45fg55', '2022-03-30', '345126');

-- --------------------------------------------------------

--
-- Structure de la table `permis`
--

CREATE TABLE `permis` (
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(20) NOT NULL,
  `date_naissance` date NOT NULL,
  `lieu_naissance` varchar(20) NOT NULL,
  `date_creation` date NOT NULL,
  `date_expiration` date NOT NULL,
  `lieu_creation` varchar(20) NOT NULL,
  `categorie` varchar(3) NOT NULL,
  `bande_mrz` varchar(30) NOT NULL,
  `numero_permis` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `permis`
--

INSERT INTO `permis` (`nom`, `prenom`, `date_naissance`, `lieu_naissance`, `date_creation`, `date_expiration`, `lieu_creation`, `categorie`, `bande_mrz`, `numero_permis`) VALUES
('MOUAFFO', 'zidane', '2022-03-22', 'Yaoundé', '2022-03-02', '2022-03-30', '0000-00-00', 'b', 'fghjklkjhgfcvbn,', '211214522355'),
('', '', '0000-00-00', '', '0000-00-00', '0000-00-00', '0000-00-00', '', '', ''),
('MOUAFFO', 'zidane', '2022-03-22', 'paris', '2022-03-08', '2022-03-14', 'amiens', 'b', 'fghjklokj,n', '1112'),
('', '', '0000-00-00', '', '0000-00-00', '0000-00-00', '', '', '', ''),
('MOUAFFO', 'zidane', '2022-03-22', 'paris', '2022-03-08', '2022-03-14', 'amiens', 'b', 'fghjklokj,n', '1112'),
('Toukam', 'cvrvrv', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
('Nanda', 'vianney', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
('NandaNV', 'vianney', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
('NandaNV', 'vianney', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
('NandaNV2', 'vianney', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
('NandaNV2', 'vianney', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
('NandaNV2', 'vianney', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
('NandaNV3', 'vianney', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `carte_identite`
--
ALTER TABLE `carte_identite`
  ADD PRIMARY KEY (`id_carte`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `carte_identite`
--
ALTER TABLE `carte_identite`
  MODIFY `id_carte` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15553;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
