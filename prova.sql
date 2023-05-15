-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mag 15, 2023 alle 16:38
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prova`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `esiti`
--

CREATE TABLE `esiti` (
  `IDPrenotazioni` int(11) NOT NULL,
  `esito` varchar(45) NOT NULL,
  `cf` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `esiti`
--

INSERT INTO `esiti` (`IDPrenotazioni`, `esito`, `cf`) VALUES
(1, 'negativo', 'prova');

-- --------------------------------------------------------

--
-- Struttura della tabella `fidelitycard`
--

CREATE TABLE `fidelitycard` (
  `IDFidelity` int(11) NOT NULL,
  `Nome` varchar(45) NOT NULL,
  `Cognome` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `SaldoCashback` double NOT NULL,
  `IDUtilizzatore` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `fidelitycard`
--

INSERT INTO `fidelitycard` (`IDFidelity`, `Nome`, `Cognome`, `Email`, `Telefono`, `SaldoCashback`, `IDUtilizzatore`) VALUES
(1, 'Alessandra', 'Danno', 'aledanna1@hotmail.it', '328569745', 0, 4),
(2, 'Alessio', 'Cruciani', 'alessiocruciani64@gmail.com', '3288660608', 0, 4),
(3, 'Valeria', 'Cannone', 'valeriacannone@gmail.com', '369874526', 0, 4),
(4, 'Valeria', 'Cannone', 'valeriacannone@gmail.com', '369874526', 0, 4);

-- --------------------------------------------------------

--
-- Struttura della tabella `ordine`
--

CREATE TABLE `ordine` (
  `IdOrdine` int(11) NOT NULL,
  `DataOrdine` date NOT NULL,
  `Consegnato` tinyint(1) NOT NULL,
  `DataConsegna` date NOT NULL,
  `IDUtilizzatore` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `ordine`
--

INSERT INTO `ordine` (`IdOrdine`, `DataOrdine`, `Consegnato`, `DataConsegna`, `IDUtilizzatore`) VALUES
(1, '2023-05-15', 0, '2023-05-18', 2),
(2, '2023-05-15', 0, '2023-05-18', 4),
(3, '2023-05-15', 0, '2023-05-18', 4),
(4, '2023-05-15', 0, '2023-05-18', 4),
(5, '2023-05-15', 0, '2023-05-18', 4),
(6, '2023-05-15', 0, '2023-05-18', 4),
(7, '2023-05-15', 0, '2023-05-15', 4),
(8, '2023-05-15', 0, '2023-05-18', 4),
(9, '2023-05-15', 0, '2023-05-18', 4),
(10, '2023-05-15', 0, '2023-05-18', 4),
(12, '2023-05-15', 0, '2023-05-18', 4),
(13, '2023-05-15', 0, '2023-05-18', 4),
(14, '2023-05-15', 0, '2023-05-18', 4);

-- --------------------------------------------------------

--
-- Struttura della tabella `prenotazioni`
--

CREATE TABLE `prenotazioni` (
  `IDPrenotazioni` int(11) NOT NULL,
  `Nome` varchar(45) NOT NULL,
  `Cognome` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `DataPrenotazione` date NOT NULL,
  `Ora` time NOT NULL,
  `IDUtilizzatore` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `prenotazioni`
--

INSERT INTO `prenotazioni` (`IDPrenotazioni`, `Nome`, `Cognome`, `Email`, `DataPrenotazione`, `Ora`, `IDUtilizzatore`) VALUES
(1, 'Alessandra', 'Danna', 'aledanna1@hotmail.it', '2022-05-19', '17:00:00', 4);

-- --------------------------------------------------------

--
-- Struttura della tabella `prodotto`
--

CREATE TABLE `prodotto` (
  `IDProdotto` int(11) NOT NULL,
  `NomeProdotto` varchar(45) NOT NULL,
  `PrezzoAcquisto` float NOT NULL,
  `PrezzoVendita` float NOT NULL,
  `DataUltimaVendita` date NOT NULL,
  `IDSconto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `prodotto`
--

INSERT INTO `prodotto` (`IDProdotto`, `NomeProdotto`, `PrezzoAcquisto`, `PrezzoVendita`, `DataUltimaVendita`, `IDSconto`) VALUES
(234, 'Gaviscon', 6, 9, '0000-00-00', 1),
(1234, 'Aspirina', 12, 18, '2023-05-15', 1),
(4512, 'Oki', 20, 30, '0000-00-00', 1),
(5678, 'Tachipirina', 10, 15, '0000-00-00', 1);

-- --------------------------------------------------------

--
-- Struttura della tabella `prodottoacquistato`
--

CREATE TABLE `prodottoacquistato` (
  `IDOrdine` int(11) NOT NULL,
  `IDProdotto` int(11) NOT NULL,
  `QuantitaAcquistata` int(11) NOT NULL,
  `TotaleAcquisto` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `prodottoacquistato`
--

INSERT INTO `prodottoacquistato` (`IDOrdine`, `IDProdotto`, `QuantitaAcquistata`, `TotaleAcquisto`) VALUES
(7, 1234, 50, 600),
(7, 5678, 100, 1000),
(7, 234, 20, 120),
(7, 4512, 25, 500);

-- --------------------------------------------------------

--
-- Struttura della tabella `prodottovenduto`
--

CREATE TABLE `prodottovenduto` (
  `IDVendita` int(11) NOT NULL,
  `IDProdotto` int(11) NOT NULL,
  `QuantitaVenduta` int(11) NOT NULL,
  `TotaleVendita` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `prodottovenduto`
--

INSERT INTO `prodottovenduto` (`IDVendita`, `IDProdotto`, `QuantitaVenduta`, `TotaleVendita`) VALUES
(1, 1234, 1, 18),
(2, 1234, 5, 90),
(2, 1234, 5, 90);

-- --------------------------------------------------------

--
-- Struttura della tabella `sconto`
--

CREATE TABLE `sconto` (
  `IDSconto` int(11) NOT NULL,
  `PercentualeSconto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `sconto`
--

INSERT INTO `sconto` (`IDSconto`, `PercentualeSconto`) VALUES
(1, 0);

-- --------------------------------------------------------

--
-- Struttura della tabella `utilizzatore`
--

CREATE TABLE `utilizzatore` (
  `IDUtilizzatore` int(11) NOT NULL,
  `Nome` varchar(45) NOT NULL,
  `Cognome` varchar(45) NOT NULL,
  `cf` varchar(16) NOT NULL,
  `DataNascita` date NOT NULL,
  `Stipendio` double NOT NULL,
  `Permessi` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Psw` varchar(45) NOT NULL,
  `Impiegato` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `utilizzatore`
--

INSERT INTO `utilizzatore` (`IDUtilizzatore`, `Nome`, `Cognome`, `cf`, `DataNascita`, `Stipendio`, `Permessi`, `Email`, `Telefono`, `Psw`, `Impiegato`) VALUES
(1, 'Alessio', 'Cruciani', 'CRCLSS01S16H769T', '2001-11-16', 10000, 'high', 'alessiocruciani64@gmail.com', '3288660608', 'Emanuela99*', 0),
(2, 'Admin', 'Admin', 'adminadmin', '2001-03-11', 3000, 'high', 'admin@admin.com', '123456789', '', 1),
(3, 'prova', 'prova', 'prova', '1999-05-06', 123, 'low', 'prova', 'prova', '123', 1),
(4, '', '', '', '0000-00-00', 1, 'high', '', '', '', 0);

-- --------------------------------------------------------

--
-- Struttura della tabella `vendita`
--

CREATE TABLE `vendita` (
  `IDVendita` int(11) NOT NULL,
  `DataVendita` date NOT NULL,
  `Orario` time NOT NULL,
  `IDUtilizzatore` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `vendita`
--

INSERT INTO `vendita` (`IDVendita`, `DataVendita`, `Orario`, `IDUtilizzatore`) VALUES
(1, '2023-05-15', '16:09:20', 4),
(2, '2023-05-15', '16:26:48', 4),
(3, '2023-05-15', '16:34:41', 4),
(4, '2023-05-15', '16:34:41', 4);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `esiti`
--
ALTER TABLE `esiti`
  ADD KEY `IDPrenotazione` (`IDPrenotazioni`);

--
-- Indici per le tabelle `fidelitycard`
--
ALTER TABLE `fidelitycard`
  ADD PRIMARY KEY (`IDFidelity`),
  ADD KEY `IDUtilizzatore` (`IDUtilizzatore`);

--
-- Indici per le tabelle `ordine`
--
ALTER TABLE `ordine`
  ADD PRIMARY KEY (`IdOrdine`),
  ADD KEY `IDUtilizzatore` (`IDUtilizzatore`);

--
-- Indici per le tabelle `prenotazioni`
--
ALTER TABLE `prenotazioni`
  ADD PRIMARY KEY (`IDPrenotazioni`),
  ADD KEY `IDUtilizzatore` (`IDUtilizzatore`);

--
-- Indici per le tabelle `prodotto`
--
ALTER TABLE `prodotto`
  ADD PRIMARY KEY (`IDProdotto`),
  ADD KEY `IDSconto` (`IDSconto`);

--
-- Indici per le tabelle `prodottoacquistato`
--
ALTER TABLE `prodottoacquistato`
  ADD KEY `IDOrdine` (`IDOrdine`),
  ADD KEY `IDProdotto` (`IDProdotto`);

--
-- Indici per le tabelle `prodottovenduto`
--
ALTER TABLE `prodottovenduto`
  ADD KEY `IDVendita` (`IDVendita`),
  ADD KEY `IDProdotto` (`IDProdotto`);

--
-- Indici per le tabelle `sconto`
--
ALTER TABLE `sconto`
  ADD PRIMARY KEY (`IDSconto`);

--
-- Indici per le tabelle `utilizzatore`
--
ALTER TABLE `utilizzatore`
  ADD PRIMARY KEY (`IDUtilizzatore`);

--
-- Indici per le tabelle `vendita`
--
ALTER TABLE `vendita`
  ADD PRIMARY KEY (`IDVendita`),
  ADD KEY `IDUtilizzatore` (`IDUtilizzatore`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `fidelitycard`
--
ALTER TABLE `fidelitycard`
  MODIFY `IDFidelity` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT per la tabella `ordine`
--
ALTER TABLE `ordine`
  MODIFY `IdOrdine` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT per la tabella `prenotazioni`
--
ALTER TABLE `prenotazioni`
  MODIFY `IDPrenotazioni` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT per la tabella `prodotto`
--
ALTER TABLE `prodotto`
  MODIFY `IDProdotto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5679;

--
-- AUTO_INCREMENT per la tabella `sconto`
--
ALTER TABLE `sconto`
  MODIFY `IDSconto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT per la tabella `utilizzatore`
--
ALTER TABLE `utilizzatore`
  MODIFY `IDUtilizzatore` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT per la tabella `vendita`
--
ALTER TABLE `vendita`
  MODIFY `IDVendita` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `esiti`
--
ALTER TABLE `esiti`
  ADD CONSTRAINT `esiti_ibfk_1` FOREIGN KEY (`IDPrenotazioni`) REFERENCES `prenotazioni` (`IDPrenotazioni`);

--
-- Limiti per la tabella `fidelitycard`
--
ALTER TABLE `fidelitycard`
  ADD CONSTRAINT `fidelitycard_ibfk_1` FOREIGN KEY (`IDUtilizzatore`) REFERENCES `utilizzatore` (`IDUtilizzatore`);

--
-- Limiti per la tabella `ordine`
--
ALTER TABLE `ordine`
  ADD CONSTRAINT `ordine_ibfk_1` FOREIGN KEY (`IDUtilizzatore`) REFERENCES `utilizzatore` (`IDUtilizzatore`);

--
-- Limiti per la tabella `prenotazioni`
--
ALTER TABLE `prenotazioni`
  ADD CONSTRAINT `prenotazioni_ibfk_1` FOREIGN KEY (`IDUtilizzatore`) REFERENCES `utilizzatore` (`IDUtilizzatore`);

--
-- Limiti per la tabella `prodotto`
--
ALTER TABLE `prodotto`
  ADD CONSTRAINT `IDSconto` FOREIGN KEY (`IDSconto`) REFERENCES `sconto` (`IDSconto`);

--
-- Limiti per la tabella `prodottoacquistato`
--
ALTER TABLE `prodottoacquistato`
  ADD CONSTRAINT `prodottoacquistato_ibfk_1` FOREIGN KEY (`IDOrdine`) REFERENCES `ordine` (`IDOrdine`),
  ADD CONSTRAINT `prodottoacquistato_ibfk_2` FOREIGN KEY (`IDProdotto`) REFERENCES `prodotto` (`IDProdotto`);

--
-- Limiti per la tabella `prodottovenduto`
--
ALTER TABLE `prodottovenduto`
  ADD CONSTRAINT `prodottovenduto_ibfk_1` FOREIGN KEY (`IDVendita`) REFERENCES `vendita` (`IDVendita`),
  ADD CONSTRAINT `prodottovenduto_ibfk_2` FOREIGN KEY (`IDProdotto`) REFERENCES `prodotto` (`IDProdotto`);

--
-- Limiti per la tabella `vendita`
--
ALTER TABLE `vendita`
  ADD CONSTRAINT `vendita_ibfk_1` FOREIGN KEY (`IDUtilizzatore`) REFERENCES `utilizzatore` (`IDUtilizzatore`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
