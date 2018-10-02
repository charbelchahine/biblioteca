-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: soen343.live    Database: django_db
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth`
--

DROP TABLE IF EXISTS `auth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth` (
  `user_id` int(11) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth`
--

LOCK TABLES `auth` WRITE;
/*!40000 ALTER TABLE `auth` DISABLE KEYS */;
INSERT INTO `auth` VALUES (1,'test'),(5,'test'),(17,'password'),(18,'test'),(19,'test'),(20,'test'),(21,'test'),(22,'test'),(23,'test'),(24,'test'),(25,'test'),(26,'test'),(27,'test'),(28,'yyfiyfiygi'),(29,'user'),(30,'test'),(31,'Soen343'),(32,'test4'),(33,'test');
/*!40000 ALTER TABLE `auth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add choice',7,'add_choice'),(26,'Can change choice',7,'change_choice'),(27,'Can delete choice',7,'delete_choice'),(28,'Can view choice',7,'view_choice'),(29,'Can add question',8,'add_question'),(30,'Can change question',8,'change_question'),(31,'Can delete question',8,'delete_question'),(32,'Can view question',8,'view_question'),(33,'Can add c user',9,'add_cuser'),(34,'Can change c user',9,'change_cuser'),(35,'Can delete c user',9,'delete_cuser'),(36,'Can view c user',9,'view_cuser');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$RbLOARWBxDWG$Ijof55hMZxc7VXodnFQeHMRSOj71a/AfZWkMxzktIJk=','2018-09-14 15:16:05.476157',1,'admin','','','admin@example.com',1,1,'2018-09-14 15:15:24.107165');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalog`
--

DROP TABLE IF EXISTS `catalog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `catalog` (
  `item_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `loan_duration` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog`
--

LOCK TABLES `catalog` WRITE;
/*!40000 ALTER TABLE `catalog` DISABLE KEYS */;
/*!40000 ALTER TABLE `catalog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `clients` (
  `user_id` int(11) NOT NULL,
  `f_name` varchar(255) NOT NULL,
  `l_name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone_num` int(11) DEFAULT NULL,
  `loan_item_count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'admin','admin','admin','123 Front Street West, Toronto, ON, M5J 2M2',1,0),(5,'john','doe','test@test.com','123 Front Street West, Toronto, ON, M5J 2M2',22222,0),(17,'plouffe','mathew','m_plo@encs.concordia.ca','123 Front Street West, Toronto, ON, M5J 2M2',1111111111,0),(18,'luca','popesco','luca@popesco.io','123 Front Street West, Toronto, ON, M5J 2M2',69,0),(19,'admin2','admin2','admin2','123 Front Street West, Toronto, ON, M5J 2M2',22,0),(20,'admin3','admin3','testadmin@admin.com','123 Front Street West, Toronto, ON, M5J 2M2',33333,0),(21,'admin4','admin4','admin4@admin.com','123 Front Street West, Toronto, ON, M5J 2M2',44444,0),(22,'admin420','admin420','admin420','123 Front Street West, Toronto, ON, M5J 2M2',420420,0),(23,'client1','client1','client1@client.com','123 Front Street West, Toronto, ON, M5J 2M2',111111,0),(24,'client2','client2','client2@client.com','123 Front Street West, Toronto, ON, M5J 2M2',22222,0),(25,'admin7','admin7','admin7@admin.com','123 Front Street West, Toronto, ON, M5J 2M2',7777,0),(26,'client66','client66','client66@client.com','123 Front Street West, Toronto, ON, M5J 2M2',666,0),(27,'client77','client77','client77@client.com','123 Front Street West, Toronto, ON, M5J 2M2',77777,0),(28,'iftiutfutf','uovov','kuffliflhlf','123 Front Street West, Toronto, ON, M5J 2M2',1,0),(29,'Nomaan','Ahmed','test@test.com','123 Front Street West, Toronto, ON, M5J 2M2',-14,0),(30,'client','client','client','123 Front Street West, Toronto, ON, M5J 2M2',1,0),(31,'Jam','Berge','james.bergeron@hotmail.com','123 Front Street West, Toronto, ON, M5J 2M2',11,0),(32,'testing','testerson','test@test4.com','123 test street',1234123,0),(33,'Ezio','Auditore','TestAdmin','83223239 Mojave Blvd',213412412,0);
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'biblioteca','cuser'),(5,'contenttypes','contenttype'),(7,'polls','choice'),(8,'polls','question'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-09-08 01:17:24.268061'),(2,'auth','0001_initial','2018-09-08 01:17:26.210455'),(3,'admin','0001_initial','2018-09-08 01:17:26.816132'),(4,'admin','0002_logentry_remove_auto_add','2018-09-08 01:17:26.955526'),(5,'admin','0003_logentry_add_action_flag_choices','2018-09-08 01:17:27.090244'),(6,'contenttypes','0002_remove_content_type_name','2018-09-08 01:17:27.439795'),(7,'auth','0002_alter_permission_name_max_length','2018-09-08 01:17:27.674517'),(8,'auth','0003_alter_user_email_max_length','2018-09-08 01:17:27.845170'),(9,'auth','0004_alter_user_username_opts','2018-09-08 01:17:27.966173'),(10,'auth','0005_alter_user_last_login_null','2018-09-08 01:17:28.165775'),(11,'auth','0006_require_contenttypes_0002','2018-09-08 01:17:28.290148'),(12,'auth','0007_alter_validators_add_error_messages','2018-09-08 01:17:28.403137'),(13,'auth','0008_alter_user_username_max_length','2018-09-08 01:17:28.640200'),(14,'auth','0009_alter_user_last_name_max_length','2018-09-08 01:17:28.895791'),(15,'sessions','0001_initial','2018-09-08 01:17:29.207446'),(16,'polls','0001_initial','2018-09-14 14:30:21.680744'),(17,'biblioteca','0001_initial','2018-09-26 16:28:55.472523');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0726z4xj7xkq1w2u9r7xgyt7twj4jzj4','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:26:48.868598'),('0dkl90cddj1nrzcv9y28gq4heuef69so','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 03:29:31.303717'),('2prreqy1tvxev2ta55hugghn8cxdpp81','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:05:22.579943'),('3ag6orjvi5m5ndbpnj5klmx1asjdzhox','ZThlOGNkOGU1MDE3OTk2MzA5OWQ0MmZhNmMzOTIwYmYzOGRhMzRjOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:03:24.518446'),('3w5g5orofpslhoa41jcp819fa5vylxk3','NjNlYTQwYTNlNzU4YzY2NTgwNWQ0MTJlMjkzNzk5NjE2ZTNiZTVjYTp7fQ==','2018-10-10 20:15:40.429792'),('4rsqrd5b90kbuze9t0e8bzu5hid5eame','ZThlOGNkOGU1MDE3OTk2MzA5OWQ0MmZhNmMzOTIwYmYzOGRhMzRjOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-09 02:53:34.805550'),('5yqbcigvog3n812m80iq5y2kpdt0fei6','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 03:36:23.593365'),('84wpks5hwee3eqtm2yengaedm1g9deen','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 01:58:09.014080'),('90hxld85sugvh379rwg2in8lczfjo7m4','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:12:02.290548'),('95gfm1g2eot5yetfso627vp87cmh2chy','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:05:29.693354'),('9y1eyeudogonrl0gz5qfd6prtkwcvmxd','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:15:30.652223'),('a4srj24mg27qjr15wul92r6jpxr4bqqj','NjcyMzFlODJlNThjZDlhYTQxOGEyYmM5Nzc1MTU5YzU4Mjg5MGVkNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2N2E5NTAxMjlhZGFiYzdiMTEwZTk5OTkzMzY1ODc1MmZkZmJkOTZjIn0=','2018-09-28 15:16:05.526717'),('bdfzfcl7l3j9qoskwj0pjao6own89czo','NDRkMDMzMTMzMjQxZDJjNzRlNTZmNjM4ZDZmMjE1ZmZhMDlkYjQwYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZTI4ZjQ0NjBhNjE2YzAxMGVlNjQ5MDNiMzgxOGQ2YTRjYjk4YWM0In0=','2018-10-10 20:41:07.892469'),('bj5foi7z83chc1emj5831w7p2mzivn0r','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:51:07.348440'),('d7omx9mbu8nhc3mc911zp48iqibzgq6u','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:30:19.579772'),('ds40pt4isxkh2fhinqj1oqdlpuvxigtg','NDRkMDMzMTMzMjQxZDJjNzRlNTZmNjM4ZDZmMjE1ZmZhMDlkYjQwYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZTI4ZjQ0NjBhNjE2YzAxMGVlNjQ5MDNiMzgxOGQ2YTRjYjk4YWM0In0=','2018-10-10 20:12:18.012209'),('i3rtf9zcf8ixprw6j7g0a80izh8jbhq8','NjNlYTQwYTNlNzU4YzY2NTgwNWQ0MTJlMjkzNzk5NjE2ZTNiZTVjYTp7fQ==','2018-10-10 20:36:51.386883'),('jtfbxiv8c8zmcg8wzg7r2zno6mdi0csl','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:21:53.042831'),('k7uvcuclplnhqlerofyjudeo93w93cp0','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:28:01.840523'),('kpk98549lzx0ur2cyz7rqeu9y6fi3zmm','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:19:46.400580'),('ktucpqydrdtsik3c7vq8uzry8ul5kvyz','NDRkMDMzMTMzMjQxZDJjNzRlNTZmNjM4ZDZmMjE1ZmZhMDlkYjQwYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZTI4ZjQ0NjBhNjE2YzAxMGVlNjQ5MDNiMzgxOGQ2YTRjYjk4YWM0In0=','2018-10-10 20:20:26.374265'),('lawy41t8uraquxde7do8jlcb4lr1lenr','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:17:45.962379'),('lazd62b48vo6cr5ve8tb8wu6jgtf67lw','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 03:37:52.565444'),('lfma5fhn1p1yy2x2j2kk5zx0gnneufbp','NDRkMDMzMTMzMjQxZDJjNzRlNTZmNjM4ZDZmMjE1ZmZhMDlkYjQwYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZTI4ZjQ0NjBhNjE2YzAxMGVlNjQ5MDNiMzgxOGQ2YTRjYjk4YWM0In0=','2018-10-10 21:11:40.414152'),('m0cnj1st9yciren48hdpeoj1cp3ilgej','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:21:23.440414'),('nmidpw5cimij7haqlda9eede8dmei28w','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 03:07:05.699403'),('opxtiy90i4mzubzyfpdpfry4ma8ixyut','NDRkMDMzMTMzMjQxZDJjNzRlNTZmNjM4ZDZmMjE1ZmZhMDlkYjQwYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZTI4ZjQ0NjBhNjE2YzAxMGVlNjQ5MDNiMzgxOGQ2YTRjYjk4YWM0In0=','2018-10-10 21:11:26.571662'),('px7bs1v6ol0a3irgsd8h17oyi7czpaex','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 02:53:04.562739'),('qdtccrjc8utuy4tkmcvwzt64mqq7biic','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:19:03.404563'),('qr3p691wuvgfzx55lhpxs5p1ullnmu8b','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:29:32.915899'),('r8vbdt4c2wjwbwbdyd1f4q2o38o9d8bq','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:04:36.060276'),('u9fcf0r264iuwxmnzyokfxlbwnk8582o','ZThlOGNkOGU1MDE3OTk2MzA5OWQ0MmZhNmMzOTIwYmYzOGRhMzRjOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-08 22:41:39.043108'),('vhzzuw9znzib71vymdevdlk8yozvqnj5','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:24:52.410254'),('vjyww0v64q0vv0ud8dogd9eslq9bc360','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:16:58.016365'),('vxp8li4v84bgopl3imkf2aadtx14uj7x','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 02:28:54.909544'),('vzl4h00abikplsvuzq5713cgkcy9o93n','MzMzMGI4NGJkOGM3MzViMTI4MTUwODIzZGVhOGI4MDFlZDQ2MjFhYjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MGU2MzEyN2E4ZDBiNTFiODU2ZWE0OWZlMTRhZjUyNzY4NzQzZGJiIn0=','2018-10-07 03:24:31.827001'),('wi11wy90ploqaz4qg8e5ztosh8ufxwna','NDlkNjlhYTZlYWE3YjA1YWY1MWU4YzQ0NmI3NTBiZjk0ZGFhYjAyYjp7fQ==','2018-10-07 03:30:11.063231'),('za5t4iah2rbxl1o8s93v4lzeubrire9o','MTBhMzMwODA0NTk3NWVmMDk1MzZmMmUxNjhkNDNhNDkxZDdiZjA3YTp7Il9hdXRoX3VzZXJfaWQiOiJOb25lIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2Njc3MmU1YjY5YmE5MWMxZmQ5N2Q1NDhkMDhhODE3MmFhZWM5MGFhIn0=','2018-10-07 03:12:42.909406');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `has_role`
--

DROP TABLE IF EXISTS `has_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `has_role` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `has_role`
--

LOCK TABLES `has_role` WRITE;
/*!40000 ALTER TABLE `has_role` DISABLE KEYS */;
INSERT INTO `has_role` VALUES (1,1),(5,2),(17,2),(18,1),(19,1),(20,1),(21,1),(22,1),(23,2),(24,2),(25,1),(26,2),(27,2),(28,2),(29,2),(30,2),(31,1),(32,2),(33,1);
/*!40000 ALTER TABLE `has_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_properties`
--

DROP TABLE IF EXISTS `item_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `item_properties` (
  `item_id` int(11) NOT NULL,
  `property` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_properties`
--

LOCK TABLES `item_properties` WRITE;
/*!40000 ALTER TABLE `item_properties` DISABLE KEYS */;
/*!40000 ALTER TABLE `item_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_items`
--

DROP TABLE IF EXISTS `loan_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `loan_items` (
  `loan_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_items`
--

LOCK TABLES `loan_items` WRITE;
/*!40000 ALTER TABLE `loan_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `loan_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_states`
--

DROP TABLE IF EXISTS `loan_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `loan_states` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_states`
--

LOCK TABLES `loan_states` WRITE;
/*!40000 ALTER TABLE `loan_states` DISABLE KEYS */;
/*!40000 ALTER TABLE `loan_states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loans`
--

DROP TABLE IF EXISTS `loans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `loans` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `return_date` timestamp NOT NULL,
  `lent_date` timestamp NOT NULL,
  `state_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loans`
--

LOCK TABLES `loans` WRITE;
/*!40000 ALTER TABLE `loans` DISABLE KEYS */;
/*!40000 ALTER TABLE `loans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'admin'),(2,'client');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1),(5),(17),(18),(19),(20),(21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'django_db'
--

--
-- Dumping routines for database 'django_db'
--
/*!50003 DROP PROCEDURE IF EXISTS `new_client` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `new_client`(l_name VARCHAR(255), f_name VARCHAR(255), email VARCHAR(255), address VARCHAR(255), phone_num INT, pw VARCHAR(255), role INT)
    DETERMINISTIC
BEGIN
        DECLARE id INT;
        DECLARE error_no INT;
        DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            
            GET CURRENT DIAGNOSTICS CONDITION 1 error_no = MYSQL_ERRNO;
            SELECT error_no AS mysql_error;
            ROLLBACK;
        END;
        START TRANSACTION;
            INSERT INTO users VALUES();
            SET id = LAST_INSERT_ID();
            INSERT INTO auth  VALUES (id, pw);
            INSERT INTO clients VALUES(id, f_name, l_name, email, address, phone_num, 0);
            INSERT INTO has_role VALUES(id, role);
        COMMIT;
    END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-01 18:29:53
