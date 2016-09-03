-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 06, 2016 at 01:12 AM
-- Server version: 5.5.47
-- PHP Version: 5.4.45-0+deb7u2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `celse`
--
CREATE DATABASE IF NOT EXISTS `celse` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `celse`;

-- --------------------------------------------------------

--
-- Table structure for table `ctrls`
--

DROP TABLE IF EXISTS `ctrls`;
CREATE TABLE IF NOT EXISTS `ctrls` (
  `idctrls` int(11) NOT NULL AUTO_INCREMENT,
  `bus_id` int(11) NOT NULL COMMENT 'Адрес на шине',
  `online` int(11) DEFAULT NULL COMMENT '0 - не насвязи\n1 - насвязи',
  `type` int(11) NOT NULL COMMENT '0 - датчик температуры\n1 - термостат сервопривода\n3 - частотный преобразователь',
  `description` varchar(100) DEFAULT NULL,
  `last_update` datetime DEFAULT NULL,
  PRIMARY KEY (`idctrls`),
  UNIQUE KEY `idctrls_UNIQUE` (`idctrls`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `ctrls`
--

INSERT INTO `ctrls` (`bus_id`, `online`, `type`, `description`, `last_update`) VALUES
( 1, 0, 3, 'Фанкойл 1', '2000-01-01 02:11:49'),
(14, 0, 4, 'Модуль DO', '2000-01-01 02:11:49');
-- --------------------------------------------------------

--
-- Table structure for table `parametrs`
--

DROP TABLE IF EXISTS `parametrs`;
CREATE TABLE IF NOT EXISTS `parametrs` (
  `idparametrs` int(11) NOT NULL AUTO_INCREMENT,
  `bus_id` int(11) NOT NULL COMMENT 'Адрес в сети RTU \nили последнне число IP адреса',
  `addr` int(11) NOT NULL COMMENT 'Номер регистра.',
  `value` float DEFAULT NULL COMMENT 'Текущее значение',
  `to_log` int(11) NOT NULL DEFAULT '0',
  `description` varchar(45) DEFAULT NULL,
  `last_update` datetime DEFAULT NULL,
  `addr_type` int(11) NOT NULL COMMENT '1 - holding register',
  `direction` int(11) NOT NULL COMMENT 'Напревление информации:\n0 - в контроллер;\n1 - в интерфейс',
  `to_set` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`idparametrs`),
  UNIQUE KEY `idparametrs_UNIQUE` (`idparametrs`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=58 ;

--
-- Dumping data for table `parametrs`
--

INSERT INTO `parametrs` (`bus_id`, `addr`, `value`, `to_log`, `description`, `last_update`, `addr_type`, `direction`, `to_set`) VALUES
( 1, 0, 20, 0, 'Уставка температуры', '2000-01-01 02:11:17', 1, 0, 0),
( 1, 1, 1, 0, 'Режим OFF=0 AUTO=1 MANUAL=2', '2000-01-01 02:11:17', 1, 0, 0),
( 1, 2, 0, 0, 'Тепло=1/Холод=0', '2000-01-01 02:11:17', 1, 0, 0),
( 1, 3, 1, 0, 'Скорость ручной', '2000-01-01 02:11:17', 1, 0, 0),
( 1, 4, 0, 0, 'Коррекция лето', '2000-01-01 02:11:17', 1, 0, 0),
( 1, 5, 0, 0, 'Коррекция зима', '2000-01-01 02:11:17', 1, 0, 0),
( 1, 6, 0, 0, 'Состояние датчика температуры', '2016-02-28 13:13:52', 1, 1, 0),
( 1, 7, 20, 1, 'Температура', '2000-01-01 02:11:17', 1, 1, 0),
( 1, 8, 0, 0, 'Верных чтений температуры', '2000-01-01 02:11:50', 1, 1, 0),
( 1, 9, 0, 0, 'Ошибок чтения температуры', '2000-01-01 02:11:41', 1, 1, 0),
( 1, 10, 0, 0, 'Текущая скорость', '2000-01-01 02:11:17', 1, 1, 0),
( 1, 11, 0, 0, 'Ошибка DO0', '2000-01-01 02:11:17', 1, 1, 0),
( 1, 12, 0, 0, 'Ошибка DO1', '2000-01-01 02:11:17', 1, 1, 0),
( 1, 13, 0, 0, 'Ошибка DO2', '2000-01-01 02:11:17', 1, 1, 0),
( 1, 14, 0, 0, 'Ошибка DO3', '2000-01-01 02:11:17', 1, 1, 0),

(14, 0, 0, 0, 'DO0', '2000-01-01 02:11:17', 1, 0, 0),
(14, 1, 0, 0, 'DO1', '2000-01-01 02:11:17', 1, 0, 0),
(14, 2, 0, 0, 'DO2', '2000-01-01 02:11:17', 1, 0, 0),
(14, 3, 0, 0, 'DO3', '2000-01-01 02:11:17', 1, 0, 0),
(14, 4, 0, 0, 'DO4', '2000-01-01 02:11:17', 1, 0, 0),
(14, 5, 0, 0, 'DO5', '2000-01-01 02:11:17', 1, 0, 0),
(14, 6, 0, 0, 'DO6', '2000-01-01 02:11:17', 1, 0, 0),
(14, 7, 0, 0, 'DO7', '2000-01-01 02:11:17', 1, 0, 0),
(14, 8, 0, 0, 'DO8', '2000-01-01 02:11:17', 1, 0, 0),
(14, 10, 0, 0, 'Ошибка DO0', '2000-01-01 02:11:17', 1, 1, 0),
(14, 11, 0, 0, 'Ошибка DO1', '2000-01-01 02:11:17', 1, 1, 0),
(14, 12, 0, 0, 'Ошибка DO2', '2000-01-01 02:11:17', 1, 1, 0),
(14, 13, 0, 0, 'Ошибка DO3', '2000-01-01 02:11:17', 1, 1, 0),
(14, 14, 0, 0, 'Ошибка DO4', '2000-01-01 02:11:17', 1, 1, 0),
(14, 15, 0, 0, 'Ошибка DO5', '2000-01-01 02:11:17', 1, 1, 0),
(14, 16, 0, 0, 'Ошибка DO6', '2000-01-01 02:11:17', 1, 1, 0),
(14, 17, 0, 0, 'Ошибка DO7', '2000-01-01 02:11:17', 1, 1, 0),
(14, 18, 0, 0, 'Ошибка DO8', '2000-01-01 02:11:17', 1, 1, 0);

-- --------------------------------------------------------



--
-- Table structure for table `paramlog`
--

DROP TABLE IF EXISTS `paramlog`;
CREATE TABLE IF NOT EXISTS `paramlog` (
  `idparamlog` int(11) NOT NULL AUTO_INCREMENT,
  `bus_id` int(11) NOT NULL COMMENT 'Адрес в сети RTU \nили последнне число IP адреса',
  `addr` int(11) NOT NULL COMMENT 'Номер регистра.',
  `addr_type` int(11) NOT NULL COMMENT '1 - holding register',
  `value` float DEFAULT NULL COMMENT 'Значение',
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`idparamlog`),
  UNIQUE KEY `idparamlog_UNIQUE` (`idparamlog`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=47389 ;

--
-- Dumping data for table `paramlog`
--

-- --------------------------------------------------------

--
-- Table structure for table `t_ctrl`
--

DROP TABLE IF EXISTS `t_ctrl`;
CREATE TABLE IF NOT EXISTS `t_ctrl` (
  `idtable1` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) NOT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idtable1`),
  UNIQUE KEY `idtable1_UNIQUE` (`idtable1`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT='Типы контроллеров - определяет шаблон отображения' AUTO_INCREMENT=4 ;

--
-- Dumping data for table `t_ctrl`
--

INSERT INTO `t_ctrl` (`idtable1`, `type_id`, `description`) VALUES
(1, 0, 'Датчики температуры'),
(2, 1, 'Контроллеры сервопривода'),
(3, 2, 'Частотные преобразователи'),
(4, 3, 'Контроллер Фєнкоила'),
(5, 4, 'Модуль DO');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
