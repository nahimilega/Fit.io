CREATE TABLE `userorder` (
  `oid` int PRIMARY KEY AUTO_INCREMENT,
  `uid` int,
  `datetime_c` date,
  `rid` int,
    `ordereditem` text
);
INSERT INTO `userorder` (`uid`, `datetime_c`, `rid`, `ordereditem`) VALUES
(1, '2020-04-29', 22, 'Paneer paratha'),
(6, '2020-04-30', 15, 'Aloo paratha'),
(1, '2020-04-26', 22, 'Shai paneer and butter naan'),
(4, '2020-04-28', 18, 'Idli smabar'),
(20, '2020-04-27', 34, 'Maggi'),
(3, '2020-04-29', 26, 'Chilli potato');
