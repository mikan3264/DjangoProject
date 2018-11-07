-- テーブルの構造 `testapp_choice`
--

DROP TABLE IF EXISTS `testapp_choice`;
CREATE TABLE `testapp_choice` (
  `id` int(11) NOT NULL,
  `choice_text` varchar(200) NOT NULL,
  `votes` int(11) NOT NULL,
  `question_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

