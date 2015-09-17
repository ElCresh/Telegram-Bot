-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generato il: Set 17, 2015 alle 21:34
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
  `Type` text NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dump dei dati per la tabella `reply`
--

INSERT INTO `reply` (`ID`, `message`, `reply`, `Type`) VALUES
(1, 'hi', 'Hello!', 'text'),
(4, 'Come ti chiami?', 'Di certo non Siri... Ti pare?!?!?', 'text'),
(5, 'Bravo', 'Grazie!', 'text'),
(6, 'Ciao', 'Ciao!', 'text'),
(8, 'Mi canti una canzone?', 'Tralalala laaa laaa.... Mi dispiace ma non so cantare....', 'text'),
(10, 'Hi', 'Hi!', 'text'),
(14, 'Chi ti ha creato?', 'Qualcuno di molto bravo! https://github.com/CreshZmine/Telegram-Bot', 'text'),
(16, 'Buongiorno', 'Buongiorno! Non pensa che oggi sia una meravigliosa giornata?', 'text'),
(18, 'Prova', 'Sa... Sa.. 1-2-3 PROVA!!', 'text'),
(19, 'prova', 'Sa... Sa.. 1-2-3 PROVA!!', 'text'),
(20, 'Mi canti qualcosa?', 'audio/song.ogg', 'aud'),
(21, 'Conosci Roma?', 'http://www.romanticarooms.it/wp-content/uploads/2013/12/romanticarooms-foto-roma1-1.jpg', 'img'),
(22, 'conosci roma?', 'http://www.romanticarooms.it/wp-content/uploads/2013/12/romanticarooms-foto-roma1-1.jpg', 'img');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
