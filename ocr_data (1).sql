-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Jeu 24 Mars 2022 à 15:25
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `ocr_data`
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
-- Contenu de la table `carte_grise`
--

INSERT INTO `carte_grise` (`num_immatriculation`, `date_immatriculation`, `nom`, `prenom`, `adresse`, `marque`, `version`, `code_identification`, `categorie`, `genre_national`, `carrosserie`, `cylindre`, `puissance`, `type_carburant`, `date_visite_technique`) VALUES
('R255GHHJJ', '15/02/2021', 'TALLA', 'Viviane', '5 rue d\'oslo', 'renault megane', '5', 'ZER789', '89', '456', 'VP', '1900', '95', 'GO', '06/07/2022'),
('PRT568', '15/02/2011', 'TERRET', 'Thomas', '4 avenue garibaldi', 'PEUGEOT', '45', 'YU96', '54', '23', 'CI', '1506', '60', 'SU', '12/10/2012'),
('l', 'g', 'df', 'dfff', 'fgggg', 'gg', 'az', 'er', 'yt', 'deed', 'sszs', 'rty', 'aze', 'tyu', 'ffg');

-- --------------------------------------------------------


--
-- Structure de la table `permis`
--

CREATE TABLE `permis` (
  `id_permis` int(11) NOT NULL,
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
-- Contenu de la table `permis`
--

INSERT INTO `permis` (`id_permis`, `nom`, `prenom`, `date_naissance`, `lieu_naissance`, `date_creation`, `date_expiration`, `lieu_creation`, `categorie`, `bande_mrz`, `numero_permis`) VALUES
(1, 'MOUAFFO', 'zidane', '2022-03-22', 'Yaoundé', '2022-03-02', '2022-03-30', '0000-00-00', 'b', 'fghjklkjhgfcvbn,', '211214522355'),
(2, '', '', '0000-00-00', '', '0000-00-00', '0000-00-00', '0000-00-00', '', '', ''),
(3, 'MOUAFFO', 'zidane', '2022-03-22', 'paris', '2022-03-08', '2022-03-14', 'amiens', 'b', 'fghjklokj,n', '1112'),
(4, '', '', '0000-00-00', '', '0000-00-00', '0000-00-00', '', '', '', ''),
(5, 'MOUAFFO', 'zidane', '2022-03-22', 'paris', '2022-03-08', '2022-03-14', 'amiens', 'b', 'fghjklokj,n', '1112'),
(6, 'Toukam', 'cvrvrv', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
(7, 'Nanda', 'vianney', '2022-03-09', 'cecec', '2022-03-09', '2022-03-16', 'amiens', 'df', 'feff', '222'),
(17, 'RICHARD', 'RICHARD', '1997-10-15', 'RICHARD', '1997-10-15', '1997-10-15', 'RICHARD', 'B', 'RICHARD', '22524451336'),
(29, 'Richard', 'Jean', '1585-10-12', 'Foumbot', '2020-10-15', '2025-10-15', 'Limoges', 'B', '123456789', '9876543210'),
(30, 'Richard', 'Jean', '1585-10-12', 'Foumbot', '2020-10-15', '2025-10-15', 'Limoges', 'B', '123456789', '9876543210'),
(31, 'Vanessa', 'MAPA', '1585-10-12', 'Baganté', '2020-10-15', '2025-10-15', 'Limoges', 'B', '123456789', '9876543210');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `permis`
--
ALTER TABLE `permis`
  ADD PRIMARY KEY (`id_permis`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `permis`
--
ALTER TABLE `permis`
  MODIFY `id_permis` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
