-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2018 年 11 朁E07 日 12:50
-- サーバのバージョン： 5.6.39-log
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_test`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `testapp_question`
--

DROP TABLE IF EXISTS `testapp_question`;
CREATE TABLE `testapp_question` (
  `id` int(11) NOT NULL,
  `question_text` varchar(200) NOT NULL,
  `pub_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- テーブルのデータのダンプ `testapp_question`
--

INSERT INTO `testapp_question` (`id`, `question_text`, `pub_date`) VALUES
(3, 'who are you?', '2018-10-30 11:16:47.000000'),
(4, 'who am i?', '2018-10-30 11:17:07.000000'),
(5, '好きな食べ物', '2018-11-05 10:29:21.000000'),
(6, 'testq', '2018-11-07 10:09:09.000000'),
(7, 'test add from shell', '2018-11-07 10:17:18.413226');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `testapp_question`
--
ALTER TABLE `testapp_question`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `testapp_question`
--
ALTER TABLE `testapp_question`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
