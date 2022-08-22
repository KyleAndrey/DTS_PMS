-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: dts
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add business style',6,'add_businessstyle'),(22,'Can change business style',6,'change_businessstyle'),(23,'Can delete business style',6,'delete_businessstyle'),(24,'Can view business style',6,'view_businessstyle'),(25,'Can add category',7,'add_category'),(26,'Can change category',7,'change_category'),(27,'Can delete category',7,'delete_category'),(28,'Can view category',7,'view_category'),(29,'Can add client',8,'add_client'),(30,'Can change client',8,'change_client'),(31,'Can delete client',8,'delete_client'),(32,'Can view client',8,'view_client'),(33,'Can add content',9,'add_content'),(34,'Can change content',9,'change_content'),(35,'Can delete content',9,'delete_content'),(36,'Can view content',9,'view_content'),(37,'Can add department',10,'add_department'),(38,'Can change department',10,'change_department'),(39,'Can delete department',10,'delete_department'),(40,'Can view department',10,'view_department'),(41,'Can add formal letter',11,'add_formalletter'),(42,'Can change formal letter',11,'change_formalletter'),(43,'Can delete formal letter',11,'delete_formalletter'),(44,'Can view formal letter',11,'view_formalletter'),(45,'Can add item',12,'add_item'),(46,'Can change item',12,'change_item'),(47,'Can delete item',12,'delete_item'),(48,'Can view item',12,'view_item'),(49,'Can add project type',13,'add_projecttype'),(50,'Can change project type',13,'change_projecttype'),(51,'Can delete project type',13,'delete_projecttype'),(52,'Can view project type',13,'view_projecttype'),(53,'Can add quotation form',14,'add_quotationform'),(54,'Can change quotation form',14,'change_quotationform'),(55,'Can delete quotation form',14,'delete_quotationform'),(56,'Can view quotation form',14,'view_quotationform'),(57,'Can add tag',15,'add_tag'),(58,'Can change tag',15,'change_tag'),(59,'Can delete tag',15,'delete_tag'),(60,'Can view tag',15,'view_tag'),(61,'Can add task',16,'add_task'),(62,'Can change task',16,'change_task'),(63,'Can delete task',16,'delete_task'),(64,'Can view task',16,'view_task'),(65,'Can add unit',17,'add_unit'),(66,'Can change unit',17,'change_unit'),(67,'Can delete unit',17,'delete_unit'),(68,'Can view unit',17,'view_unit'),(69,'Can add sales inv form',18,'add_salesinvform'),(70,'Can change sales inv form',18,'change_salesinvform'),(71,'Can delete sales inv form',18,'delete_salesinvform'),(72,'Can view sales inv form',18,'view_salesinvform'),(73,'Can add project',19,'add_project'),(74,'Can change project',19,'change_project'),(75,'Can delete project',19,'delete_project'),(76,'Can view project',19,'view_project'),(77,'Can add file model',20,'add_filemodel'),(78,'Can change file model',20,'change_filemodel'),(79,'Can delete file model',20,'delete_filemodel'),(80,'Can view file model',20,'view_filemodel'),(81,'Can add delivery receipt',21,'add_deliveryreceipt'),(82,'Can change delivery receipt',21,'change_deliveryreceipt'),(83,'Can delete delivery receipt',21,'delete_deliveryreceipt'),(84,'Can view delivery receipt',21,'view_deliveryreceipt'),(85,'Can add billing inv form',22,'add_billinginvform'),(86,'Can change billing inv form',22,'change_billinginvform'),(87,'Can delete billing inv form',22,'delete_billinginvform'),(88,'Can view billing inv form',22,'view_billinginvform'),(89,'Can add assigned task',23,'add_assignedtask'),(90,'Can change assigned task',23,'change_assignedtask'),(91,'Can delete assigned task',23,'delete_assignedtask'),(92,'Can view assigned task',23,'view_assignedtask'),(93,'Can add assigned item',24,'add_assigneditem'),(94,'Can change assigned item',24,'change_assigneditem'),(95,'Can delete assigned item',24,'delete_assigneditem'),(96,'Can view assigned item',24,'view_assigneditem'),(97,'Can add user',25,'add_customuser'),(98,'Can change user',25,'change_customuser'),(99,'Can delete user',25,'delete_customuser'),(100,'Can view user',25,'view_customuser');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_system_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_system_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `system_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-08-21 04:08:59.261594','1','dts',2,'[{\"changed\": {\"fields\": [\"Account Type\"]}}]',25,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(24,'system','assigneditem'),(23,'system','assignedtask'),(22,'system','billinginvform'),(6,'system','businessstyle'),(7,'system','category'),(8,'system','client'),(9,'system','content'),(25,'system','customuser'),(21,'system','deliveryreceipt'),(10,'system','department'),(20,'system','filemodel'),(11,'system','formalletter'),(12,'system','item'),(19,'system','project'),(13,'system','projecttype'),(14,'system','quotationform'),(18,'system','salesinvform'),(15,'system','tag'),(16,'system','task'),(17,'system','unit');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-08-21 04:04:29.181044'),(2,'contenttypes','0002_remove_content_type_name','2022-08-21 04:04:29.276239'),(3,'auth','0001_initial','2022-08-21 04:04:29.661845'),(4,'auth','0002_alter_permission_name_max_length','2022-08-21 04:04:29.748955'),(5,'auth','0003_alter_user_email_max_length','2022-08-21 04:04:29.760113'),(6,'auth','0004_alter_user_username_opts','2022-08-21 04:04:29.772026'),(7,'auth','0005_alter_user_last_login_null','2022-08-21 04:04:29.784366'),(8,'auth','0006_require_contenttypes_0002','2022-08-21 04:04:29.792231'),(9,'auth','0007_alter_validators_add_error_messages','2022-08-21 04:04:29.805879'),(10,'auth','0008_alter_user_username_max_length','2022-08-21 04:04:29.816439'),(11,'auth','0009_alter_user_last_name_max_length','2022-08-21 04:04:29.827645'),(12,'auth','0010_alter_group_name_max_length','2022-08-21 04:04:29.851549'),(13,'auth','0011_update_proxy_permissions','2022-08-21 04:04:29.861719'),(14,'auth','0012_alter_user_first_name_max_length','2022-08-21 04:04:29.874457'),(15,'system','0001_initial','2022-08-21 04:04:32.785831'),(16,'admin','0001_initial','2022-08-21 04:04:33.025317'),(17,'admin','0002_logentry_remove_auto_add','2022-08-21 04:04:33.041008'),(18,'admin','0003_logentry_add_action_flag_choices','2022-08-21 04:04:33.053525'),(19,'sessions','0001_initial','2022-08-21 04:04:33.112809');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0guhqf0afc5a955heasm0lyd16ogxv90','.eJx1j0FPwzAMhf9Lz6hKO7om3LYDEhK7IMG1chJnNWTJlqRDCPHfcVGRQAwfIjvP79PzezXAVMZhypgGstVN1VRXP_80mBcMs2CfIexjbWIoiXQ9r9SLmuuN9_GVn0f25F206LeL8RdthDwyCkE2K2Whb3ttO9Uo1a1aIzVCZ51UnRGul9edWet2rWTboBLSASijUWsjFUOPKTryyLD2u4QQLLiYDuDvsRRMt9w_YSJHmJbT5sTcgj1Q2JhCZ_yKzApn5im9PaBBOpYL3gwe8104RzJ4CU3eU9j_v3CaYoFCMfzRPj4BM9qD6w:1oPfog:fPfDS5hOfDRvXeVMQCi4TZN8TjCrItrfs6oB-OsMrmM','2022-09-04 07:56:18.253005'),('1tn7r69z5onn8kcirwqin07pdwqk34hf','.eJx1j8FqwzAMht8l5xKatG7s3dbDYLDBKHTXIMtyo9W1N9tpGWPvPgdy2CC76PB_-j-hr6qHMQ_9mCj2bKq7qqlWvzMNeCY_AfMG_hRqDD5H1vW0Us801ffOhVsZx9JJz8GQ28_FP7YB0lBUBLLZKANd22kjVKOU2LQoNYEwViqBa9vJrcCdbndKtg2ptbQACjVpjVIV6XS5mMBc2L_EYNlRSctdvlL8PBASv-eHEC-vFNkyxfm1BI7So78GRlrAH2PIkDn4BWZLBO6Jcqa4gDU7x_70n_v7B1jxfB0:1oQ2Lk:qiCzT8c08UZ1UUFM1gn5usIY64H22g4AEGciI70boqA','2022-09-05 07:59:56.327992'),('6u4iknk3c2ertudltq3y7owlseuwl3ie','.eJxVj70OgkAQhN-F2lz48eDWTkNjYWlNdvcWAS-c4SAWxnf3MBTabDI7M18yr6TBZe6aJcjU9DY5JFmy-_0R8l3G1bADjjev2I_z1JNaI2pzgzo655_xXGMnXLwVd9qKf7QOQxdRgiYrwGKVV2Q1ZAC6yNmQoLatAc1pW5m95pLyEkyeCaSmRQQmIWIDEfqY_CA8n-uIK6Jm18s4156_E94fpXRG2g:1oPd9e:G_ZTJhng68ECWX3w5PvtFCdbhfz4tofplfo0qX143xI','2022-09-04 05:05:46.791896'),('8qhtcoq0remz1772ple5lrmppx681hdo','.eJxVjLEOgkAQRP_lanPhDg927bS3tCa7e4ughEs4iIXx34WEQpspZua9t2lombtmyTo1fTQn48zht2OSp47bEB803pOVNM5Tz3a72H3N9jwM6bXGbWXyNUUdLjv4Z-sod6tKCVyJkWpfcwzoEEPpBVgpxBYwSNHWcAxSsa8QvFMsoCVCYWUWQPP5AloHPYE:1oQ8Ci:rgWjAFP-z4LFzaLD6bo_cGMCcjbJg5aDkmF4tE4mTHU','2022-09-05 14:15:00.808663'),('9thjmiyp82x205xqy0jif11spko44fo3','.eJxVjLEOgkAQRP_lanPhDg927bS3tCa7e4ughEs4iIXx34WEQpspZua9t2lombtmyTo1fTQn48zht2OSp47bEB803pOVNM5Tz3a72H3N9jwM6bXGbWXyNUUdLjv4Z-sod6tKCVyJkWpfcwzoEEPpBVgpxBYwSNHWcAxSsa8QvFMsoCVCYWUWQPP5AloHPYE:1oQ0lM:rRMhDVJDcdVFwRW-1AhXzC6WGHzIj8HYUy9pF4EBA0I','2022-09-05 06:18:16.636770'),('grqbm7h8a0bqmxewwtn129utdvww26dl','.eJxtjrFuwjAQht8lM4ripCa-bjAgdWBBomt0Pl-IIbWL7VChqu-OI2Wgapcb7vv_7-676HBKQzdFDp01xWshitXzTiNd2M3AnNGdfEnepWB1OUfKhcZyM47-K49j7sS9Nzxul-Iv24BxyCpGJRow2NatNhIEgGxqUppRml6BpKpv1Yukta7XoGrBUKkeEUiz1qQgS6-TT5isdzsfPt452N5yWN7P1-2Nw_3AxPYz_ZOIOHJ8czdvif_gnwfH3F5H:1oPz9e:iAGm_BlUgPqNu89RPJXhIem6Mkq0MlONc4XgDeuGOIE','2022-09-05 04:35:14.616435'),('iu1u67l5bokrkse5tla7w49qurvciiwe','.eJx1T01LxDAQ_S89S-mH3SbedhFhQS-CXsskmWxnzSZrkq6I-N-dSgWFOocwL2_emzcfxQBTHocpYRzIFDdFXVz9_lOgX9DPhDmCP4RSB58jqXIeKRc2lVvnwhs_T6xJD8Gg2y3CP24jpJGtEETdSgN90yvTyVrKrm20UAidsUJ2urK9uO70RjUbKZoaZSUsgNQKldJCsmkCh2nvL4E03oV4esZIljAuF5xjOKLO-1vGLeM5KLdgTuS3OtMFv5MyY1kM7h5zxrhipMg58of_N_Gp7BbfH1EjnfPKxOsUMmQKfj2nJYeMmp-qqqr4_ALhSYiQ:1oQ1iC:kPhdG9kYuaZGvD3TmfuDZhLlTZ90k7HeMV3TUqjx7oA','2022-09-05 07:19:04.367786'),('iy3kcege4nig6wty5n9g4immmh30qjax','.eJxVjLEOgkAQRP_lanPhDg927bS3tCa7e4ughEs4iIXx34WEQpspZua9t2lombtmyTo1fTQn48zht2OSp47bEB803pOVNM5Tz3a72H3N9jwM6bXGbWXyNUUdLjv4Z-sod6tKCVyJkWpfcwzoEEPpBVgpxBYwSNHWcAxSsa8QvFMsoCVCYWUWQPP5AloHPYE:1oPnal:KKFJq16dqjwyxjvkXg_MvaACDbAjL2ETKStWIKuKIyM','2022-09-04 16:14:27.928813');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_assigneditem`
--

DROP TABLE IF EXISTS `system_assigneditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_assigneditem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `itemQuantity` varchar(20) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `billingInvID_id` int DEFAULT NULL,
  `deliveryReceiptID_id` int DEFAULT NULL,
  `itemID_id` int DEFAULT NULL,
  `quotationFormID_id` int DEFAULT NULL,
  `salesInvFormID_id` int DEFAULT NULL,
  `unit_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `system_assigneditem_billingInvID_id_7890eccc_fk_system_bi` (`billingInvID_id`),
  KEY `system_assigneditem_deliveryReceiptID_id_af52b708_fk_system_de` (`deliveryReceiptID_id`),
  KEY `system_assigneditem_itemID_id_b9a37225_fk_system_item_itemID` (`itemID_id`),
  KEY `system_assigneditem_quotationFormID_id_28318843_fk_system_qu` (`quotationFormID_id`),
  KEY `system_assigneditem_salesInvFormID_id_20eae537_fk_system_sa` (`salesInvFormID_id`),
  KEY `system_assigneditem_unit_id_42f5b38b_fk_system_unit_unitID` (`unit_id`),
  CONSTRAINT `system_assigneditem_billingInvID_id_7890eccc_fk_system_bi` FOREIGN KEY (`billingInvID_id`) REFERENCES `system_billinginvform` (`billingInvID`),
  CONSTRAINT `system_assigneditem_deliveryReceiptID_id_af52b708_fk_system_de` FOREIGN KEY (`deliveryReceiptID_id`) REFERENCES `system_deliveryreceipt` (`deliveryRecID`),
  CONSTRAINT `system_assigneditem_itemID_id_b9a37225_fk_system_item_itemID` FOREIGN KEY (`itemID_id`) REFERENCES `system_item` (`itemID`),
  CONSTRAINT `system_assigneditem_quotationFormID_id_28318843_fk_system_qu` FOREIGN KEY (`quotationFormID_id`) REFERENCES `system_quotationform` (`quotationFormID`),
  CONSTRAINT `system_assigneditem_salesInvFormID_id_20eae537_fk_system_sa` FOREIGN KEY (`salesInvFormID_id`) REFERENCES `system_salesinvform` (`salesInvID`),
  CONSTRAINT `system_assigneditem_unit_id_42f5b38b_fk_system_unit_unitID` FOREIGN KEY (`unit_id`) REFERENCES `system_unit` (`unitID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_assigneditem`
--

LOCK TABLES `system_assigneditem` WRITE;
/*!40000 ALTER TABLE `system_assigneditem` DISABLE KEYS */;
INSERT INTO `system_assigneditem` VALUES (1,'5','500',NULL,1,1,NULL,NULL,1),(2,'10','1000',NULL,NULL,1,NULL,1,1),(3,'1','100',1,NULL,1,NULL,NULL,1),(7,'20','2000',NULL,NULL,1,1,NULL,1);
/*!40000 ALTER TABLE `system_assigneditem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_assignedtask`
--

DROP TABLE IF EXISTS `system_assignedtask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_assignedtask` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `taskFile` varchar(100) DEFAULT NULL,
  `is_file_uploaded` tinyint(1) NOT NULL,
  `is_done` tinyint(1) NOT NULL,
  `projectID_id` bigint DEFAULT NULL,
  `taskID_id` bigint DEFAULT NULL,
  `fileCreatedAt` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `system_assignedtask_projectID_id_86459a50_fk_system_project_id` (`projectID_id`),
  KEY `system_assignedtask_taskID_id_f79af713_fk_system_task_id` (`taskID_id`),
  CONSTRAINT `system_assignedtask_projectID_id_86459a50_fk_system_project_id` FOREIGN KEY (`projectID_id`) REFERENCES `system_project` (`id`),
  CONSTRAINT `system_assignedtask_taskID_id_f79af713_fk_system_task_id` FOREIGN KEY (`taskID_id`) REFERENCES `system_task` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_assignedtask`
--

LOCK TABLES `system_assignedtask` WRITE;
/*!40000 ALTER TABLE `system_assignedtask` DISABLE KEYS */;
INSERT INTO `system_assignedtask` VALUES (1,'',0,0,3,3,'2022-08-21 05:03:40.415705'),(2,'',0,0,3,8,'2022-08-21 05:03:40.421373'),(3,'',0,0,3,1,'2022-08-21 05:03:40.428533'),(4,'',0,0,3,14,'2022-08-21 05:03:40.433611');
/*!40000 ALTER TABLE `system_assignedtask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_billinginvform`
--

DROP TABLE IF EXISTS `system_billinginvform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_billinginvform` (
  `billingInvID` int NOT NULL AUTO_INCREMENT,
  `billingInvStatus` varchar(20) DEFAULT NULL,
  `dateIssued` date DEFAULT NULL,
  `terms` varchar(100) DEFAULT NULL,
  `jopoNum` varchar(255) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `grandTotal` varchar(100) DEFAULT NULL,
  `clients_id` bigint DEFAULT NULL,
  PRIMARY KEY (`billingInvID`),
  KEY `system_billinginvform_clients_id_6c153e6f_fk_system_client_id` (`clients_id`),
  CONSTRAINT `system_billinginvform_clients_id_6c153e6f_fk_system_client_id` FOREIGN KEY (`clients_id`) REFERENCES `system_client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_billinginvform`
--

LOCK TABLES `system_billinginvform` WRITE;
/*!40000 ALTER TABLE `system_billinginvform` DISABLE KEYS */;
INSERT INTO `system_billinginvform` VALUES (1,'Pending','2022-08-30','1','123',NULL,'100',1);
/*!40000 ALTER TABLE `system_billinginvform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_businessstyle`
--

DROP TABLE IF EXISTS `system_businessstyle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_businessstyle` (
  `businessStyleID` int NOT NULL AUTO_INCREMENT,
  `businessStyleName` varchar(255) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`businessStyleID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_businessstyle`
--

LOCK TABLES `system_businessstyle` WRITE;
/*!40000 ALTER TABLE `system_businessstyle` DISABLE KEYS */;
INSERT INTO `system_businessstyle` VALUES (1,'Test Style',0);
/*!40000 ALTER TABLE `system_businessstyle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_category`
--

DROP TABLE IF EXISTS `system_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_category` (
  `categoryID` int NOT NULL AUTO_INCREMENT,
  `categoryName` varchar(255) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`categoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_category`
--

LOCK TABLES `system_category` WRITE;
/*!40000 ALTER TABLE `system_category` DISABLE KEYS */;
INSERT INTO `system_category` VALUES (1,'Test Category',0),(2,'2',0);
/*!40000 ALTER TABLE `system_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_client`
--

DROP TABLE IF EXISTS `system_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_client` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `companyName` varchar(50) DEFAULT NULL,
  `companyAddress` varchar(200) DEFAULT NULL,
  `region` varchar(100) DEFAULT NULL,
  `province` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `barangay` varchar(100) DEFAULT NULL,
  `postalCode` varchar(5) DEFAULT NULL,
  `companyTIN` varchar(12) DEFAULT NULL,
  `contactPerson` varchar(50) DEFAULT NULL,
  `contactNumber` varchar(12) DEFAULT NULL,
  `contactPosition` varchar(30) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  `date_of_inactivity` datetime(6) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `businessStyle_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyTIN` (`companyTIN`),
  KEY `system_client_businessStyle_id_bfa6727f_fk_system_bu` (`businessStyle_id`),
  CONSTRAINT `system_client_businessStyle_id_bfa6727f_fk_system_bu` FOREIGN KEY (`businessStyle_id`) REFERENCES `system_businessstyle` (`businessStyleID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_client`
--

LOCK TABLES `system_client` WRITE;
/*!40000 ALTER TABLE `system_client` DISABLE KEYS */;
INSERT INTO `system_client` VALUES (1,'Test Company','123 Test St.','NATIONAL CAPITAL REGION (NCR)','NCR, CITY OF MANILA, FIRST DISTRICT','SAMPALOC','Barangay 420','1005','123456789000','Mx. Test','09123456789','Testing Staff',0,NULL,'2022-08-21 04:14:15.464522',1),(2,'2','2','NATIONAL CAPITAL REGION (NCR)','NCR, CITY OF MANILA, FIRST DISTRICT','PANDACAN','Barangay 850','2','222222222000','2','2','2',0,NULL,'2022-08-21 05:11:35.671539',1);
/*!40000 ALTER TABLE `system_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_content`
--

DROP TABLE IF EXISTS `system_content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_content` (
  `contentID` int NOT NULL AUTO_INCREMENT,
  `contentName` varchar(255) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`contentID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_content`
--

LOCK TABLES `system_content` WRITE;
/*!40000 ALTER TABLE `system_content` DISABLE KEYS */;
INSERT INTO `system_content` VALUES (1,'Test Content',0),(2,'2',0);
/*!40000 ALTER TABLE `system_content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_customuser`
--

DROP TABLE IF EXISTS `system_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `contactNumber` varchar(12) NOT NULL,
  `accountType` varchar(50) NOT NULL,
  `date_of_inactivity` datetime(6) DEFAULT NULL,
  `department_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `system_customuser_department_id_2038396b_fk_system_department_id` (`department_id`),
  CONSTRAINT `system_customuser_department_id_2038396b_fk_system_department_id` FOREIGN KEY (`department_id`) REFERENCES `system_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_customuser`
--

LOCK TABLES `system_customuser` WRITE;
/*!40000 ALTER TABLE `system_customuser` DISABLE KEYS */;
INSERT INTO `system_customuser` VALUES (1,'pbkdf2_sha256$320000$AMqBl6vkPSwF6q2FwgBxy2$Z2kJEfAW/uFYcZ++6ZTwSNr/UohWOLghqddwE4JA3b4=','2022-08-22 14:15:00.803178',1,'dts','','','dtssystemAWS@gmail.com',1,1,'2022-08-21 04:06:34.000000','','Administrator',NULL,NULL);
/*!40000 ALTER TABLE `system_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_customuser_groups`
--

DROP TABLE IF EXISTS `system_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_customuser_groups_customuser_id_group_id_d3a6bfbc_uniq` (`customuser_id`,`group_id`),
  KEY `system_customuser_groups_group_id_352c00a8_fk_auth_group_id` (`group_id`),
  CONSTRAINT `system_customuser_gr_customuser_id_9a75976c_fk_system_cu` FOREIGN KEY (`customuser_id`) REFERENCES `system_customuser` (`id`),
  CONSTRAINT `system_customuser_groups_group_id_352c00a8_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_customuser_groups`
--

LOCK TABLES `system_customuser_groups` WRITE;
/*!40000 ALTER TABLE `system_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_customuser_user_permissions`
--

DROP TABLE IF EXISTS `system_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_customuser_user_p_customuser_id_permission_a55385a5_uniq` (`customuser_id`,`permission_id`),
  KEY `system_customuser_us_permission_id_df394679_fk_auth_perm` (`permission_id`),
  CONSTRAINT `system_customuser_us_customuser_id_0619ec9d_fk_system_cu` FOREIGN KEY (`customuser_id`) REFERENCES `system_customuser` (`id`),
  CONSTRAINT `system_customuser_us_permission_id_df394679_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_customuser_user_permissions`
--

LOCK TABLES `system_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `system_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_deliveryreceipt`
--

DROP TABLE IF EXISTS `system_deliveryreceipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_deliveryreceipt` (
  `deliveryRecID` int NOT NULL AUTO_INCREMENT,
  `deliveryRecStatus` varchar(20) DEFAULT NULL,
  `dateIssued` date DEFAULT NULL,
  `terms` varchar(100) DEFAULT NULL,
  `clients_id` bigint DEFAULT NULL,
  PRIMARY KEY (`deliveryRecID`),
  KEY `system_deliveryreceipt_clients_id_c02f4a65_fk_system_client_id` (`clients_id`),
  CONSTRAINT `system_deliveryreceipt_clients_id_c02f4a65_fk_system_client_id` FOREIGN KEY (`clients_id`) REFERENCES `system_client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_deliveryreceipt`
--

LOCK TABLES `system_deliveryreceipt` WRITE;
/*!40000 ALTER TABLE `system_deliveryreceipt` DISABLE KEYS */;
INSERT INTO `system_deliveryreceipt` VALUES (1,'Pending','2022-08-20','5',1);
/*!40000 ALTER TABLE `system_deliveryreceipt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_department`
--

DROP TABLE IF EXISTS `system_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `departmentName` varchar(255) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_department`
--

LOCK TABLES `system_department` WRITE;
/*!40000 ALTER TABLE `system_department` DISABLE KEYS */;
INSERT INTO `system_department` VALUES (1,'sample',0);
/*!40000 ALTER TABLE `system_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_filemodel`
--

DROP TABLE IF EXISTS `system_filemodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_filemodel` (
  `fileID` int NOT NULL AUTO_INCREMENT,
  `fileName` varchar(255) DEFAULT NULL,
  `filePath` varchar(100) NOT NULL,
  `fileCreatedAt` datetime(6) NOT NULL,
  `clientID_id` bigint DEFAULT NULL,
  `fileCategory_id` int DEFAULT NULL,
  `fileContent_id` int DEFAULT NULL,
  PRIMARY KEY (`fileID`),
  KEY `system_filemodel_clientID_id_77a9df05_fk_system_client_id` (`clientID_id`),
  KEY `system_filemodel_fileCategory_id_bc317085_fk_system_ca` (`fileCategory_id`),
  KEY `system_filemodel_fileContent_id_77077865_fk_system_co` (`fileContent_id`),
  CONSTRAINT `system_filemodel_clientID_id_77a9df05_fk_system_client_id` FOREIGN KEY (`clientID_id`) REFERENCES `system_client` (`id`),
  CONSTRAINT `system_filemodel_fileCategory_id_bc317085_fk_system_ca` FOREIGN KEY (`fileCategory_id`) REFERENCES `system_category` (`categoryID`),
  CONSTRAINT `system_filemodel_fileContent_id_77077865_fk_system_co` FOREIGN KEY (`fileContent_id`) REFERENCES `system_content` (`contentID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_filemodel`
--

LOCK TABLES `system_filemodel` WRITE;
/*!40000 ALTER TABLE `system_filemodel` DISABLE KEYS */;
INSERT INTO `system_filemodel` VALUES (5,'system_task.sql','documents/system_task.sql','2022-08-21 07:30:02.928195',1,1,1),(6,'system_assignedtask.sql','documents/system_assignedtask.sql','2022-08-21 07:30:13.120243',1,1,1);
/*!40000 ALTER TABLE `system_filemodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_filemodel_fileTag`
--

DROP TABLE IF EXISTS `system_filemodel_fileTag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_filemodel_fileTag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `filemodel_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_filemodel_fileTag_filemodel_id_tag_id_7b98eac1_uniq` (`filemodel_id`,`tag_id`),
  KEY `system_filemodel_fileTag_tag_id_beabbc40_fk_system_tag_tagID` (`tag_id`),
  CONSTRAINT `system_filemodel_fil_filemodel_id_024310b3_fk_system_fi` FOREIGN KEY (`filemodel_id`) REFERENCES `system_filemodel` (`fileID`),
  CONSTRAINT `system_filemodel_fileTag_tag_id_beabbc40_fk_system_tag_tagID` FOREIGN KEY (`tag_id`) REFERENCES `system_tag` (`tagID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_filemodel_fileTag`
--

LOCK TABLES `system_filemodel_fileTag` WRITE;
/*!40000 ALTER TABLE `system_filemodel_fileTag` DISABLE KEYS */;
INSERT INTO `system_filemodel_fileTag` VALUES (5,5,1),(6,6,1);
/*!40000 ALTER TABLE `system_filemodel_fileTag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_formalletter`
--

DROP TABLE IF EXISTS `system_formalletter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_formalletter` (
  `formalID` int NOT NULL AUTO_INCREMENT,
  `formalStatus` varchar(20) DEFAULT NULL,
  `formalSubj` varchar(20) DEFAULT NULL,
  `dateIssued` date DEFAULT NULL,
  `companyName` varchar(255) DEFAULT NULL,
  `companyAddress` varchar(20) DEFAULT NULL,
  `receiverName` varchar(20) DEFAULT NULL,
  `position` varchar(20) DEFAULT NULL,
  `body` longtext,
  PRIMARY KEY (`formalID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_formalletter`
--

LOCK TABLES `system_formalletter` WRITE;
/*!40000 ALTER TABLE `system_formalletter` DISABLE KEYS */;
INSERT INTO `system_formalletter` VALUES (1,'Pending','Test Subject','2022-08-25','Test Company','Test Address','Test Receiver','Tester','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam id turpis sem. Phasellus dignissim dui ac felis condimentum interdum. Suspendisse mollis fermentum ipsum. Vestibulum ut libero condimentum, ullamcorper ante id, vehicula mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla vitae odio eget ligula efficitur viverra. Pellentesque eleifend sagittis velit rutrum vestibulum.');
/*!40000 ALTER TABLE `system_formalletter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_item`
--

DROP TABLE IF EXISTS `system_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_item` (
  `itemID` int NOT NULL AUTO_INCREMENT,
  `itemName` longtext,
  `itemPrice` varchar(20) DEFAULT NULL,
  `itemType` varchar(20) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_item`
--

LOCK TABLES `system_item` WRITE;
/*!40000 ALTER TABLE `system_item` DISABLE KEYS */;
INSERT INTO `system_item` VALUES (1,'Test Item','100','Product',0);
/*!40000 ALTER TABLE `system_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_project`
--

DROP TABLE IF EXISTS `system_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_project` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `projectType` varchar(20) DEFAULT NULL,
  `projectName` varchar(50) DEFAULT NULL,
  `projectPhase` varchar(20) NOT NULL,
  `projectStatus` varchar(20) NOT NULL,
  `paymentTerms` varchar(5) DEFAULT NULL,
  `deliveryTerms` varchar(5) DEFAULT NULL,
  `poDeadline` date DEFAULT NULL,
  `projectStart` date NOT NULL,
  `projectDeadline` date DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  `date_of_inactivity` datetime(6) DEFAULT NULL,
  `clients_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `system_project_clients_id_a81d2ff0_fk_system_client_id` (`clients_id`),
  CONSTRAINT `system_project_clients_id_a81d2ff0_fk_system_client_id` FOREIGN KEY (`clients_id`) REFERENCES `system_client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_project`
--

LOCK TABLES `system_project` WRITE;
/*!40000 ALTER TABLE `system_project` DISABLE KEYS */;
INSERT INTO `system_project` VALUES (3,'Test Type','Test Project','Obtain PO','Ongoing','5','5','2022-08-25','2022-08-21','2022-09-04',0,NULL,1);
/*!40000 ALTER TABLE `system_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_projecttype`
--

DROP TABLE IF EXISTS `system_projecttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_projecttype` (
  `projectTypeID` int NOT NULL AUTO_INCREMENT,
  `projectTypeName` varchar(255) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`projectTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_projecttype`
--

LOCK TABLES `system_projecttype` WRITE;
/*!40000 ALTER TABLE `system_projecttype` DISABLE KEYS */;
INSERT INTO `system_projecttype` VALUES (1,'Test Type',0);
/*!40000 ALTER TABLE `system_projecttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_quotationform`
--

DROP TABLE IF EXISTS `system_quotationform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_quotationform` (
  `quotationFormID` int NOT NULL AUTO_INCREMENT,
  `quotationStatus` varchar(20) DEFAULT NULL,
  `quotationSubj` varchar(20) DEFAULT NULL,
  `dateIssued` date DEFAULT NULL,
  `companyName` varchar(100) DEFAULT NULL,
  `companyAddress` varchar(255) DEFAULT NULL,
  `receiverName` varchar(100) DEFAULT NULL,
  `position` varchar(100) DEFAULT NULL,
  `contactNum` varchar(20) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `grandTotal` varchar(100) DEFAULT NULL,
  `deliveryTerms` varchar(100) DEFAULT NULL,
  `paymentTerms` varchar(100) DEFAULT NULL,
  `validityTerms` varchar(100) DEFAULT NULL,
  `warrantyTerms` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`quotationFormID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_quotationform`
--

LOCK TABLES `system_quotationform` WRITE;
/*!40000 ALTER TABLE `system_quotationform` DISABLE KEYS */;
INSERT INTO `system_quotationform` VALUES (1,'Approved','Test Subject','2022-08-10','Test Company','Test Address','Test Receiver','Test Position','09123456789',NULL,'1000','D','P','V','X');
/*!40000 ALTER TABLE `system_quotationform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_salesinvform`
--

DROP TABLE IF EXISTS `system_salesinvform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_salesinvform` (
  `salesInvID` int NOT NULL AUTO_INCREMENT,
  `salesInvStatus` varchar(20) DEFAULT NULL,
  `dateIssued` date DEFAULT NULL,
  `terms` varchar(100) DEFAULT NULL,
  `mop` varchar(255) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `grandTotal` varchar(100) DEFAULT NULL,
  `clients_id` bigint DEFAULT NULL,
  PRIMARY KEY (`salesInvID`),
  KEY `system_salesinvform_clients_id_af454c4f_fk_system_client_id` (`clients_id`),
  CONSTRAINT `system_salesinvform_clients_id_af454c4f_fk_system_client_id` FOREIGN KEY (`clients_id`) REFERENCES `system_client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_salesinvform`
--

LOCK TABLES `system_salesinvform` WRITE;
/*!40000 ALTER TABLE `system_salesinvform` DISABLE KEYS */;
INSERT INTO `system_salesinvform` VALUES (1,'Pending','2022-08-25','10','cash',NULL,'1100',1);
/*!40000 ALTER TABLE `system_salesinvform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_tag`
--

DROP TABLE IF EXISTS `system_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_tag` (
  `tagID` int NOT NULL AUTO_INCREMENT,
  `tagName` varchar(255) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`tagID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_tag`
--

LOCK TABLES `system_tag` WRITE;
/*!40000 ALTER TABLE `system_tag` DISABLE KEYS */;
INSERT INTO `system_tag` VALUES (1,'Test Tag',0),(2,'2',0);
/*!40000 ALTER TABLE `system_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_task`
--

DROP TABLE IF EXISTS `system_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_task` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phaseName` varchar(20) NOT NULL,
  `taskName` varchar(100) DEFAULT NULL,
  `has_file` tinyint(1) NOT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_task`
--

LOCK TABLES `system_task` WRITE;
/*!40000 ALTER TABLE `system_task` DISABLE KEYS */;
INSERT INTO `system_task` VALUES (1,'Obtain PO','Obtain copy of purchase order',0,0),(2,'Obtain PO','Print copy of purchase order',0,0),(3,'Confirm PO','Confirm purchase order to the client',0,0),(4,'Confirm PO','Follow up confirmation of order from supplier',0,0),(5,'Confirm PO','Sign the purchase order',0,0),(6,'Confirm PO','Print confirmed purchase order',0,0),(7,'Confirm PO','Confirmed Purchase Order File',1,0),(8,'Delivery','Obtain a copy of confirmed purchase order',0,0),(9,'Delivery','Obtain order from the supplier',0,0),(10,'Delivery','Obtain delivery receipt',0,0),(11,'Delivery','Deliver order',0,0),(12,'Delivery','Obtain signed delivery receipt',0,0),(13,'Delivery','Signed Delivery Receipt File',1,0),(14,'Payment','Obtain sales / billing invoice',0,0),(15,'Payment','Send sales / billing invoice to customer',0,0),(16,'Payment','Obtain signed sales / billing invoice',0,0),(17,'Payment','Signed Invoice File',1,0),(18,'Payment','Proof of Payment File',1,0);
/*!40000 ALTER TABLE `system_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_unit`
--

DROP TABLE IF EXISTS `system_unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_unit` (
  `unitID` int NOT NULL AUTO_INCREMENT,
  `unitName` varchar(255) DEFAULT NULL,
  `is_inactive` tinyint(1) NOT NULL,
  PRIMARY KEY (`unitID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_unit`
--

LOCK TABLES `system_unit` WRITE;
/*!40000 ALTER TABLE `system_unit` DISABLE KEYS */;
INSERT INTO `system_unit` VALUES (1,'Test Unit',0);
/*!40000 ALTER TABLE `system_unit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-22 14:20:40
