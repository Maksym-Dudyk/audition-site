-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema audition-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema audition-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `audition-db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `audition-db` ;

-- -----------------------------------------------------
-- Table `audition-db`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `audition-db`.`user` (
  `id` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;




-- -----------------------------------------------------
-- Table `audition-db`.`tariff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `audition-db`.`tariff` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `price` FLOAT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `audition-db`.`feedback`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `audition-db`.`feedback` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `content` VARCHAR(500) NOT NULL,
  `date` DATE NOT NULL,
  `user_id` INT NOT NULL,
  `tariff_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `feedback_user_idx` (`user_id` ASC) VISIBLE,
  INDEX `feedback_tariff_idx` (`tariff_id` ASC) VISIBLE,
  CONSTRAINT `feedback_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `audition-db`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `feedback_tariff`
    FOREIGN KEY (`tariff_id`)
    REFERENCES `audition-db`.`tariff` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `audition-db`.`post_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `audition-db`.`post_type` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `audition-db`.`post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `audition-db`.`post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `text` VARCHAR(500) NOT NULL,
  `img_link` VARCHAR(200) NOT NULL,
  `type_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `post_post_type_idx` (`type_id` ASC) VISIBLE,
  CONSTRAINT `post_post_type`
    FOREIGN KEY (`type_id`)
    REFERENCES `audition-db`.`post_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `audition-db`.`service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `audition-db`.`service` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO `feedback` VALUES (1,'Дуже задодолений','Все чудово. У компанії мені надали корисні поради та рекомендації, які допомогли моєму бізнесу рости.','2020-04-05',1,1), (2,'Буду повертатись ще!','Професіоналізм, який проявляють працівники цієї компанії, дійсно вражає. Вони завжди готові допомогти та відповісти на всі запитання.','2020-04-05',4,2), (3,'Рекомендую!','Дякую за чудову роботу! Якість послуг на висоті, а співпраця з компанією - це справжнє задоволення.','2020-04-05',5,3);
INSERT INTO `user` VALUES (1,'Олександр','Пристай'),(2,'Назарій','Цюприк'), (3, "Олексій", "Дубровський"), (4, "Настя", "Крук"), (5, "Марк", "Турко");
INSERT INTO `tariff` VALUES (1,'Базовий','Пакет для початківців',500),(2,'Стандартний','Пакет для невеликих компаній',1000),(3,'Преміум','Пакет для великих компаній',2000);
INSERT INTO `post_type` VALUES (1,'Інформаційний'),(2,'Навчальний');
INSERT INTO `post` VALUES (1,'Забезпечення безпеки даних в інформаційній системі аудиторської компанії','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVDCYP4vRI1kTJLGt_Y0lCJPIPVhxmQE14Bw&usqp=CAU',1),(2,'Як використовувати інформаційну систему для аналізу та звітування результатів аудиту','https://i.pinimg.com/474x/5b/c9/2d/5bc92dfc200766bb913023576d270fc4.jpg',2),(3,'Роль інформаційної системи в аудиторській компанії: переваги та виклики','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5D6D1lBVg7Q5Yy7ckAUCSYTLm5vIffGiCqg&usqp=CAU',1);
INSERT INTO `service` VALUES (1,'Аудиторські послуги','Надаємо повний спектр аудиторських послуг, що допоможуть Вашому бізнесу розвиватися та ефективно працювати.'),(2,'Податкові консультації','Допоможемо Вам з питань оподаткування та податкового планування, a також допоможемо вирішити податкові спори.'),(3,'Консультації з управління','Надаємо консультації з управління бізнесом, зокрема з питань стратегічного планування, бізнес-аналізу та оптимізації бізнес-процесів.');
