-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generato il: Set 15, 2015 alle 22:46
-- Versione del server: 5.5.44-0ubuntu0.14.04.1
-- Versione PHP: 5.5.9-1ubuntu4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `telegram_bot`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `reply`
--

CREATE TABLE IF NOT EXISTS `reply` (
  `ID` mediumint(9) NOT NULL AUTO_INCREMENT,
  `message` text NOT NULL,
  `reply` text NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dump dei dati per la tabella `reply`
--

INSERT INTO `reply` (`ID`, `message`, `reply`) VALUES
(1, 'hi', 'Hello!'),
(4, 'Come ti chiami?', 'Di certo non Siri... Ti pare?!?!?'),
(5, 'Bravo', 'grazie'),
(6, 'Ciao', 'Ciao!'),
(8, 'Mi canti una canzone?', 'Tralalala laaa laaa.... Mi dispiace ma non so cantare....');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
