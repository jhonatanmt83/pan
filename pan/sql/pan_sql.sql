-- MySQL dump 10.13  Distrib 5.1.66, for debian-linux-gnu (i486)
--
-- Host: localhost    Database: pan
-- ------------------------------------------------------
-- Server version	5.1.66-0ubuntu0.10.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `pan`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `pan` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pan`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add TipoAlmacen',8,'add_tipoalmacen'),(23,'Can change TipoAlmacen',8,'change_tipoalmacen'),(24,'Can delete TipoAlmacen',8,'delete_tipoalmacen'),(25,'Can add TipoPan',9,'add_tipopan'),(26,'Can change TipoPan',9,'change_tipopan'),(27,'Can delete TipoPan',9,'delete_tipopan'),(28,'Can add Producion',10,'add_producion'),(29,'Can change Producion',10,'change_producion'),(30,'Can delete Producion',10,'delete_producion'),(31,'Can add Cliente',11,'add_cliente'),(32,'Can change Cliente',11,'change_cliente'),(33,'Can delete Cliente',11,'delete_cliente'),(34,'Can add Ingreso',12,'add_ingreso'),(35,'Can change Ingreso',12,'change_ingreso'),(36,'Can delete Ingreso',12,'delete_ingreso'),(37,'Can add Venta',13,'add_venta'),(38,'Can change Venta',13,'change_venta'),(39,'Can delete Venta',13,'delete_venta'),(40,'Can add Deuda',14,'add_deuda'),(41,'Can change Deuda',14,'change_deuda'),(42,'Can delete Deuda',14,'delete_deuda'),(43,'Can add Pago',15,'add_pago'),(44,'Can change Pago',15,'change_pago'),(45,'Can delete Pago',15,'delete_pago'),(46,'Can add Egreso',16,'add_egreso'),(47,'Can change Egreso',16,'change_egreso'),(48,'Can delete Egreso',16,'delete_egreso');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','','','admin@jap.com','pbkdf2_sha256$10000$9Xf8YJ1DnQwQ$BObXIM1RZmoagJZh3I+3z5NkCl+aq8NZqVjxw0C/6Ng=',1,1,1,'2012-12-16 23:07:06','2012-12-16 23:06:11');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2012-12-16 23:07:19',1,9,'11','Chavata',1,''),(2,'2012-12-16 23:07:56',1,9,'12','Cachito',1,''),(3,'2012-12-16 23:08:11',1,9,'13','Cevita',1,''),(4,'2012-12-16 23:08:32',1,9,'14','Yema',1,''),(5,'2012-12-16 23:08:43',1,9,'15','Caracol',1,''),(6,'2012-12-16 23:08:59',1,9,'16','Caracol',1,''),(7,'2012-12-16 23:09:21',1,9,'17','Frances',1,''),(8,'2012-12-16 23:09:39',1,9,'18','Bollo',1,''),(9,'2012-12-16 23:09:54',1,9,'19','Baguett',1,''),(10,'2012-12-16 23:12:27',1,9,'20','Tortas',1,''),(11,'2012-12-16 23:12:49',1,9,'21','Alfajores',1,''),(12,'2012-12-16 23:13:07',1,9,'22','Mil hojas',1,''),(13,'2012-12-16 23:13:30',1,9,'23','Pastel de Manzana',1,''),(14,'2012-12-16 23:13:46',1,9,'24','Pionono',1,''),(15,'2012-12-16 23:13:59',1,9,'25','Orejitas',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'TipoAlmacen','panaderia','tipoalmacen'),(9,'TipoPan','panaderia','tipopan'),(10,'Producion','panaderia','producion'),(11,'Cliente','panaderia','cliente'),(12,'Ingreso','panaderia','ingreso'),(13,'Venta','panaderia','venta'),(14,'Deuda','panaderia','deuda'),(15,'Pago','panaderia','pago'),(16,'Egreso','panaderia','egreso');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9804518a6f98a18ad1a70b6e1075897b','MmYxMTdhYzI2ZDg0MDdiZDQxMjU1MjBjZjI5ODI5Y2UyNjA3NmIxZjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2012-12-30 23:07:06');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_cliente`
--

DROP TABLE IF EXISTS `panaderia_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_cliente`
--

LOCK TABLES `panaderia_cliente` WRITE;
/*!40000 ALTER TABLE `panaderia_cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `panaderia_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_deuda`
--

DROP TABLE IF EXISTS `panaderia_deuda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_deuda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipopan_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `monto` decimal(8,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `panaderia_deuda_3f886ec` (`tipopan_id`),
  KEY `panaderia_deuda_52f540a3` (`cliente_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_deuda`
--

LOCK TABLES `panaderia_deuda` WRITE;
/*!40000 ALTER TABLE `panaderia_deuda` DISABLE KEYS */;
/*!40000 ALTER TABLE `panaderia_deuda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_egreso`
--

DROP TABLE IF EXISTS `panaderia_egreso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_egreso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `monto` decimal(8,2) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_egreso`
--

LOCK TABLES `panaderia_egreso` WRITE;
/*!40000 ALTER TABLE `panaderia_egreso` DISABLE KEYS */;
/*!40000 ALTER TABLE `panaderia_egreso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_ingreso`
--

DROP TABLE IF EXISTS `panaderia_ingreso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_ingreso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipopan_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `panaderia_ingreso_3f886ec` (`tipopan_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_ingreso`
--

LOCK TABLES `panaderia_ingreso` WRITE;
/*!40000 ALTER TABLE `panaderia_ingreso` DISABLE KEYS */;
/*!40000 ALTER TABLE `panaderia_ingreso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_pago`
--

DROP TABLE IF EXISTS `panaderia_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_pago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipopan_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `monto` decimal(8,2) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `panaderia_pago_3f886ec` (`tipopan_id`),
  KEY `panaderia_pago_52f540a3` (`cliente_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_pago`
--

LOCK TABLES `panaderia_pago` WRITE;
/*!40000 ALTER TABLE `panaderia_pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `panaderia_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_producion`
--

DROP TABLE IF EXISTS `panaderia_producion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_producion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipopan_id` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `panaderia_producion_3f886ec` (`tipopan_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_producion`
--

LOCK TABLES `panaderia_producion` WRITE;
/*!40000 ALTER TABLE `panaderia_producion` DISABLE KEYS */;
/*!40000 ALTER TABLE `panaderia_producion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_tipoalmacen`
--

DROP TABLE IF EXISTS `panaderia_tipoalmacen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_tipoalmacen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_tipoalmacen`
--

LOCK TABLES `panaderia_tipoalmacen` WRITE;
/*!40000 ALTER TABLE `panaderia_tipoalmacen` DISABLE KEYS */;
INSERT INTO `panaderia_tipoalmacen` VALUES (1,'Embolsados'),(2,'Comerciales');
/*!40000 ALTER TABLE `panaderia_tipoalmacen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_tipopan`
--

DROP TABLE IF EXISTS `panaderia_tipopan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_tipopan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `tipoalmacen_id` int(11) NOT NULL,
  `precio` decimal(8,3) NOT NULL,
  `grupo` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `panaderia_tipopan_532d67b8` (`tipoalmacen_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_tipopan`
--

LOCK TABLES `panaderia_tipopan` WRITE;
/*!40000 ALTER TABLE `panaderia_tipopan` DISABLE KEYS */;
INSERT INTO `panaderia_tipopan` VALUES (1,'Chancay x24',1,'2.000',24),(2,'Chalaco x24',1,'2.000',24),(3,'Hamburguesa x10',1,'2.000',10),(4,'Integral x12',1,'0.900',12),(5,'Integral x8',1,'0.900',8),(6,'Molde Blanco',1,'2.500',NULL),(7,'Molde Clasico',1,'2.800',NULL),(8,'Molde Integral',1,'2.500',NULL),(9,'Caramanduka',1,'0.800',NULL),(10,'Tostadas',1,'0.900',NULL),(11,'Chavata',2,'0.125',1),(12,'Cachito',2,'0.125',1),(13,'Cevita',2,'0.125',1),(14,'Yema',2,'0.125',1),(15,'Caracol',2,'0.125',1),(16,'Caracol',2,'0.125',1),(17,'Frances',2,'0.125',1),(18,'Bollo',2,'0.125',1),(19,'Baguett',2,'1.000',1),(20,'Tortas',2,'2.500',1),(21,'Alfajores',2,'0.500',1),(22,'Mil hojas',2,'1.000',1),(23,'Pastel de Manzana',2,'1.000',1),(24,'Pionono',2,'1.000',1),(25,'Orejitas',2,'0.500',1);
/*!40000 ALTER TABLE `panaderia_tipopan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panaderia_venta`
--

DROP TABLE IF EXISTS `panaderia_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panaderia_venta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipopan_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `panaderia_venta_3f886ec` (`tipopan_id`),
  KEY `panaderia_venta_52f540a3` (`cliente_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panaderia_venta`
--

LOCK TABLES `panaderia_venta` WRITE;
/*!40000 ALTER TABLE `panaderia_venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `panaderia_venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-12-18  9:03:18
