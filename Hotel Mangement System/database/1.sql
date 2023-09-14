-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: management
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alldetail`
--

DROP TABLE IF EXISTS `alldetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alldetail` (
  `ref` varchar(45) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `datein` varchar(45) DEFAULT NULL,
  `dateout` varchar(45) DEFAULT NULL,
  `room` varchar(45) DEFAULT NULL,
  `amount` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alldetail`
--

LOCK TABLES `alldetail` WRITE;
/*!40000 ALTER TABLE `alldetail` DISABLE KEYS */;
INSERT INTO `alldetail` VALUES ('7638','Tina Shinde','9867119533','2023-09-11','2023-09-12','102','Rs.275.00'),('1428','Nikihil Shetty','8149653024','2023-09-11','2023-09-12','101','Rs.275.00'),('4727','Harish Shetty','9209474769','2023-09-11','2023-09-12','104','Rs.275.00'),('3781','Durga Wagh','9876123456','2023-09-11','2023-09-12','102','Rs.275.00'),('1428','Nikihil Shetty','8149653024','2023-09-11','2023-09-12','101','Rs.275.00'),('4597','Ishika Kadam','9321647894','2023-09-11','2023-09-12','103','Rs.275.00'),('7431','Farah Qureshi','9876543212','2023-09-11','2023-09-12','201','Rs.275.00'),('4727','Harish Shetty','9209474769','2023-09-11','2023-09-12','103','Rs.275.00');
/*!40000 ALTER TABLE `alldetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `avlroom`
--

DROP TABLE IF EXISTS `avlroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avlroom` (
  `room1` varchar(45) NOT NULL,
  PRIMARY KEY (`room1`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avlroom`
--

LOCK TABLES `avlroom` WRITE;
/*!40000 ALTER TABLE `avlroom` DISABLE KEYS */;
INSERT INTO `avlroom` VALUES ('104'),('201'),('202'),('204'),('301'),('302'),('303'),('304');
/*!40000 ALTER TABLE `avlroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `Ref` int NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Mother` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `PostCode` varchar(45) DEFAULT NULL,
  `Mobile` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Nationality` varchar(45) DEFAULT NULL,
  `Idproof` varchar(45) DEFAULT NULL,
  `Idnumber` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Ref`),
  UNIQUE KEY `Mobile_UNIQUE` (`Mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1428,'Nikihil Shetty','Sunita Shetty','Male','401208','8149653024','n@gmail.com','Indian','Aadhar Card','12345667879','Virar'),(3781,'Durga Wagh','Kalpana Wagh','Female','201302','9876123456','d@gmail.com','Indian','Aadhar Card','12345678789','Latur'),(4597,'Ishika Kadam','jostna kadam','Female','401408','9321647894','i@gmail.com','Indian','Aadhar Card','6789123456','Dadar'),(4727,'Harish Shetty','Sudari Shetty','Male','608909','9209474769','harish@gmail.com','Indian','Aadhar Card','123434567658','Vasai'),(4911,'Diksha Dhuri','Vina Dhuri','Female','601208','9876245631','d@gmail.com','Indian','Aadhar Card','9862457531','Worli'),(7431,'Farah Qureshi','Salma Qureshi','Male','50865','9876543212','f@gnail.com','Indian','Aadhar Card','8765432123456','Nanded'),(7638,'Tina Shinde','Sraswati Shinde','Male','203876','9867119533','t@gmail.com','Indian','Aadhar Card','531496279524','Byculla'),(8567,'Nikita Shetty','Sunita Shetty','Male','401208','7397864339','nikita@gmail.com','Indian','Passport','12345763456','Borivali');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `details`
--

DROP TABLE IF EXISTS `details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `details` (
  `Floor` varchar(45) DEFAULT NULL,
  `RoomNo` varchar(45) NOT NULL,
  PRIMARY KEY (`RoomNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `details`
--

LOCK TABLES `details` WRITE;
/*!40000 ALTER TABLE `details` DISABLE KEYS */;
INSERT INTO `details` VALUES ('1','101'),('1','102'),('1','103'),('1','104'),('2','201'),('2','202'),('2','203'),('2','204'),('3','301'),('3','302'),('3','303'),('3','304');
/*!40000 ALTER TABLE `details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `Contact1` varchar(45) NOT NULL,
  `Check_in` varchar(45) DEFAULT NULL,
  `Check_out` varchar(45) DEFAULT NULL,
  `Roomavailable` varchar(45) NOT NULL,
  `Noofdays` varchar(45) DEFAULT NULL,
  `tax` varchar(45) DEFAULT NULL,
  `total` varchar(45) DEFAULT NULL,
  `finaltotal` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Roomavailable`,`Contact1`),
  UNIQUE KEY `Contact1_UNIQUE` (`Contact1`),
  UNIQUE KEY `Roomavailable_UNIQUE` (`Roomavailable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES ('7397864339','2023-09-11','2023-09-12','101','1','Rs.25.00','Rs.250.00','Rs.275.00'),('9867119533','2023-09-11','2023-09-12','102','1','Rs.25.00','Rs.250.00','Rs.275.00'),('9876123456','2023-09-11','2023-09-12','103','1','Rs.25.00','Rs.250.00','Rs.275.00'),(' 9209474769','2023-09-11','2023-09-12','203','1','Rs.25.00','Rs.250.00','Rs.275.00');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-11 20:09:46
