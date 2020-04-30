



ALTER TABLE `user_similarity` ADD FOREIGN KEY (`user_1`) REFERENCES `user` (`id`);

ALTER TABLE `user_similarity` ADD FOREIGN KEY (`user_2`) REFERENCES `user` (`id`);

ALTER TABLE `insureduser` ADD FOREIGN KEY (`iid`) REFERENCES `insurance` (`id`);

ALTER TABLE `userorder` ADD FOREIGN KEY (`datetime_c`) REFERENCES `usernutrition` (`datetime_c`);

ALTER TABLE `eaten_food` ADD FOREIGN KEY (`fid`) REFERENCES `food` (`id`);
ALTER TABLE `dish_similarity` ADD FOREIGN KEY (`dish_1`) REFERENCES `food` (`id`);

ALTER TABLE `dish_similarity` ADD FOREIGN KEY (`dish_2`) REFERENCES `food` (`id`);

