
CREATE TABLE `insurance` (
  `id` int NOT NULL PRIMARY KEY,
  `name` varchar(100) NOT NULL,
  `location` varchar(200) NOT NULL
);

INSERT INTO `insurance` (`id`, `name`, `Location`) VALUES
(1, 'Apollo Munich Health Insurance Company', 'Delhi'),
(2, 'ICICI Lombard Health Insurance', 'Kerala'),
(3, 'Star Health Insurance', 'Gujarat'),
(4, 'HDFC ERGO Health Insurance', 'Gujarat'),
(5, 'New India Assurance Co. Ltd.', 'Andhra Pradesh'),
(6, 'Oriental Insurance Co. Ltd.', 'Uttar Pradesh'),
(7, 'National Insurance Co. Ltd.', 'Uttar Pradesh'),
(8, 'SBI General Insurance Co. Ltd.', 'Karnataka'),
(9, 'Star Health and Allied Insurance Co. Ltd.', 'Maharastra'),
(10, 'Religare Health Insurance Co. Ltd.', 'Andhra Pradesh'),
(11, 'Apollo Munich Health Insurance Co. Ltd', 'Bihar'),
(12, 'Max Bupa Health Insurance Co. Ltd', 'Uttar Pradesh'),
(13, 'Cigna TTK Health Insurance Co. Ltd', 'Maharastra'),
(14, 'ICICI Lombard General Insurance Co. Ltd', 'Chhattisgarh'),
(15, 'Bharti AXA General Insurance Co. Ltd', 'Bihar'),
(16, 'Cholamandalam MS General Insurance Co. Ltd', 'West Bengal'),
(17, 'Future Generali India Insurance Co. Ltd.', 'Uttar Pradesh'),
(18, 'HDFC ERGO General Insurance Co. Ltd', 'Maharastra'),
(19, 'IFFCO Tokio General Insurance Co. Ltd', 'Andhra Pradesh'),
(20, 'L&T General Insurance Co. Ltd', 'Karnataka'),
(21, 'Reliance General Insurance Co. Ltd', 'Punjab'),
(22, 'Royal Sundaram Alliance Insurance Co. Ltd', 'Uttar Pradesh'),
(23, 'Bajaj Allianz General Insurance Co. Ltd.', 'Maharastra'),
(24, 'Universal Sompo General Insurance Co. Ltd.', 'Gujarat'),
(25, 'United India Insurance Co. Ltd.', 'Gujarat'),
(26, 'Future Generali India Insurance Co. Ltd.', 'Madhya Pradesh'),
(27, 'Universal Sompo General Insurance Co. Ltd.', 'Haryana'),
(28, 'Magma HDI General Insurance Comapny Limited', 'Uttar Pradesh'),
(29, 'Shriram General Insurance Company', 'Uttarakhand'),
(30, 'Liberty Videocon General Insurance', 'Gujarat'),
(31, 'Raheja QBE General Insurance Company Limited', 'Rajasthan'),
(32, 'Tata AIG General Insurance Comapny Limited', 'Bihar'),
(33, 'ManipalCigna Health Insurance Commpany', 'Rajasthan');



CREATE TABLE `insureduser` (
  `iid` int NOT NULL,
  `uid` int NOT NULL PRIMARY KEY
);


INSERT INTO `insureduser` (`uid`, `iid`) VALUES
(1, 22),
(5, 6),
(6, 13),
(7, 13),
(8, 26),
(10, 33),
(11, 17),
(12, 24),
(17, 30),
(19, 5),
(20, 31),
(21, 19),
(22, 21),
(23, 19),
(28, 4),
(30, 1),
(31, 9),
(33, 2),
(34, 18),
(35, 0),
(36, 24),
(37, 6),
(38, 11),
(40, 12),
(41, 30),
(42, 25),
(45, 15),
(50, 7);



CREATE TABLE `potential_users` (
  `id` int NOT NULL PRIMARY KEY,
  `iid` int NOT NULL,
  `uid` int NOT NULL
);


INSERT INTO `potential_users` (`id`, `iid`, `uid`) VALUES
(1, 2, 22),
(2, 3, 30),
(3, 3, 3),
(4, 5, 11),
(5, 6, 50),
(6, 6, 7),
(7, 7, 35),
(8, 7, 50),
(9, 7, 17),
(10, 10, 5),
(11, 12, 15),
(12, 12, 25),
(13, 15, 33),
(14, 17, 37),
(15, 17, 14),
(16, 19, 49),
(17, 22, 3),
(18, 24, 8),
(19, 25, 26),
(20, 25, 41),
(21, 28, 5),
(22, 30, 4),
(23, 32, 16),
(24, 33, 2),
(25, 33, 21);