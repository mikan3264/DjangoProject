-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2018 年 11 朁E07 日 12:48
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


--
-- テーブルのデータのダンプ `testapp_choice`
--

INSERT INTO `testapp_choice` (`id`, `choice_text`, `votes`, `question_id`) VALUES
(3, 'choice000', 0, 3),
(4, 'choice001', 3, 4),
(5, 'choice002', 0, 3),
(6, 'choice003', 0, 4),
(7, 'choice004', 0, 3),
(8, 'choice005', 0, 4),
(9, 'りんご', 4, 5),
(10, 'ばなな', 3, 5),
(11, 'ぶどう', 2, 5),
(12, 'みかん', 4, 5),
(13, 'かき', 2, 5),
(14, '114', 0, 6),
(15, '514', 0, 6),
(16, '1919', 0, 6),
(17, '810', 0, 6),
(18, 'ｲｸｲｸ', 0, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `testapp_choice`
--
ALTER TABLE `testapp_choice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `testapp_choice_question_id_49b58598_fk_testapp_question_id` (`question_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `testapp_choice`
--
ALTER TABLE `testapp_choice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- ダンプしたテーブルの制約
--

--
-- テーブルの制約 `testapp_choice`
--
ALTER TABLE `testapp_choice`
  ADD CONSTRAINT `testapp_choice_question_id_49b58598_fk_testapp_question_id` FOREIGN KEY (`question_id`) REFERENCES `testapp_question` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
