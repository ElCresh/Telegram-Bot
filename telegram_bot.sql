-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generato il: Set 17, 2015 alle 21:34
-- Versione del server: 5.5.44-0ubuntu0.14.04.1
-- Versione PHP: 5.5.9-1ubuntu4.11

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
  `ID` mediumint(9) NOT NULL,
  `message` text NOT NULL,
  `reply` text NOT NULL,
  `Type` text NOT NULL,
  PRIMARY KEY (`ID`)
);

--
-- Dump dei dati per la tabella `reply`
--

INSERT INTO `reply` (`ID`, `message`, `reply`, `Type`) VALUES
(1, 'hi', 'Hello!', 'text'),
(2, 'come ti chiami?', 'Di certo non Siri... Ti pare?!?!?', 'text'),
(3, 'bravo', 'Grazie!', 'text'),
(4, 'ciao', 'Ciao!', 'text'),
(5, 'mi canti una canzone?', 'Tralalala laaa laaa.... Mi dispiace ma non so cantare....', 'text'),
(6, 'hi', 'Hi!', 'text'),
(7, 'chi ti ha creato?', 'Qualcuno di molto bravo! https://github.com/CreshZmine/Telegram-Bot', 'text'),
(8, 'buongiorno', 'Buongiorno! Non pensa che oggi sia una meravigliosa giornata?', 'text'),
(9, 'prova', 'Sa... Sa.. 1-2-3 PROVA!!', 'text'),
(10, 'mi canti qualcosa?', 'audio/song.wav', 'voice'),
(11, 'conosci roma?', 'http://www.romanticarooms.it/wp-content/uploads/2013/12/romanticarooms-foto-roma1-1.jpg', 'photo');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
