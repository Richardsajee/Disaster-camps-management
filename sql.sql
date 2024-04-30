/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - camp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`camp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `camp`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add adminmessage',7,'add_adminmessage'),(26,'Can change adminmessage',7,'change_adminmessage'),(27,'Can delete adminmessage',7,'delete_adminmessage'),(28,'Can view adminmessage',7,'view_adminmessage'),(29,'Can add alert',8,'add_alert'),(30,'Can change alert',8,'change_alert'),(31,'Can delete alert',8,'delete_alert'),(32,'Can view alert',8,'view_alert'),(33,'Can add bank',9,'add_bank'),(34,'Can change bank',9,'change_bank'),(35,'Can delete bank',9,'delete_bank'),(36,'Can view bank',9,'view_bank'),(37,'Can add camp',10,'add_camp'),(38,'Can change camp',10,'change_camp'),(39,'Can delete camp',10,'delete_camp'),(40,'Can view camp',10,'view_camp'),(41,'Can add donation',11,'add_donation'),(42,'Can change donation',11,'change_donation'),(43,'Can delete donation',11,'delete_donation'),(44,'Can view donation',11,'view_donation'),(45,'Can add login',12,'add_login'),(46,'Can change login',12,'change_login'),(47,'Can delete login',12,'delete_login'),(48,'Can view login',12,'view_login'),(49,'Can add precaution',13,'add_precaution'),(50,'Can change precaution',13,'change_precaution'),(51,'Can delete precaution',13,'delete_precaution'),(52,'Can view precaution',13,'view_precaution'),(53,'Can add subemergency',14,'add_subemergency'),(54,'Can change subemergency',14,'change_subemergency'),(55,'Can delete subemergency',14,'delete_subemergency'),(56,'Can view subemergency',14,'view_subemergency'),(57,'Can add userdb',15,'add_userdb'),(58,'Can change userdb',15,'change_userdb'),(59,'Can delete userdb',15,'delete_userdb'),(60,'Can view userdb',15,'view_userdb'),(61,'Can add whether',16,'add_whether'),(62,'Can change whether',16,'change_whether'),(63,'Can delete whether',16,'delete_whether'),(64,'Can view whether',16,'view_whether'),(65,'Can add volunteer',17,'add_volunteer'),(66,'Can change volunteer',17,'change_volunteer'),(67,'Can delete volunteer',17,'delete_volunteer'),(68,'Can view volunteer',17,'view_volunteer'),(69,'Can add subadmin',18,'add_subadmin'),(70,'Can change subadmin',18,'change_subadmin'),(71,'Can delete subadmin',18,'delete_subadmin'),(72,'Can view subadmin',18,'view_subadmin'),(73,'Can add slot',19,'add_slot'),(74,'Can change slot',19,'change_slot'),(75,'Can delete slot',19,'delete_slot'),(76,'Can view slot',19,'view_slot'),(77,'Can add needs',20,'add_needs'),(78,'Can change needs',20,'change_needs'),(79,'Can delete needs',20,'delete_needs'),(80,'Can view needs',20,'view_needs'),(81,'Can add feedback',21,'add_feedback'),(82,'Can change feedback',21,'change_feedback'),(83,'Can delete feedback',21,'delete_feedback'),(84,'Can view feedback',21,'view_feedback'),(85,'Can add complaintesandreply',22,'add_complaintesandreply'),(86,'Can change complaintesandreply',22,'change_complaintesandreply'),(87,'Can delete complaintesandreply',22,'delete_complaintesandreply'),(88,'Can view complaintesandreply',22,'view_complaintesandreply'),(89,'Can add campallocation',23,'add_campallocation'),(90,'Can change campallocation',23,'change_campallocation'),(91,'Can delete campallocation',23,'delete_campallocation'),(92,'Can view campallocation',23,'view_campallocation');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'myapp','adminmessage'),(8,'myapp','alert'),(9,'myapp','bank'),(10,'myapp','camp'),(23,'myapp','campallocation'),(22,'myapp','complaintesandreply'),(11,'myapp','donation'),(21,'myapp','feedback'),(12,'myapp','login'),(20,'myapp','needs'),(13,'myapp','precaution'),(19,'myapp','slot'),(18,'myapp','subadmin'),(14,'myapp','subemergency'),(15,'myapp','userdb'),(17,'myapp','volunteer'),(16,'myapp','whether'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-11-15 08:51:02.209264'),(2,'auth','0001_initial','2023-11-15 08:51:03.008193'),(3,'admin','0001_initial','2023-11-15 08:51:03.175849'),(4,'admin','0002_logentry_remove_auto_add','2023-11-15 08:51:03.183530'),(5,'admin','0003_logentry_add_action_flag_choices','2023-11-15 08:51:03.189749'),(6,'contenttypes','0002_remove_content_type_name','2023-11-15 08:51:03.298028'),(7,'auth','0002_alter_permission_name_max_length','2023-11-15 08:51:03.363328'),(8,'auth','0003_alter_user_email_max_length','2023-11-15 08:51:03.425730'),(9,'auth','0004_alter_user_username_opts','2023-11-15 08:51:03.433731'),(10,'auth','0005_alter_user_last_login_null','2023-11-15 08:51:03.486962'),(11,'auth','0006_require_contenttypes_0002','2023-11-15 08:51:03.489962'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-15 08:51:03.496964'),(13,'auth','0008_alter_user_username_max_length','2023-11-15 08:51:03.560977'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-15 08:51:03.625892'),(15,'auth','0010_alter_group_name_max_length','2023-11-15 08:51:03.690891'),(16,'auth','0011_update_proxy_permissions','2023-11-15 08:51:03.697910'),(17,'auth','0012_alter_user_first_name_max_length','2023-11-15 08:51:03.762946'),(18,'myapp','0001_initial','2023-11-15 08:51:05.043759'),(19,'sessions','0001_initial','2023-11-15 08:51:05.112607'),(20,'myapp','0002_volunteer_camp','2023-11-16 08:32:25.362143'),(21,'myapp','0003_rename_whether_whether_whetherdata','2023-11-16 09:32:33.410476'),(22,'myapp','0004_rename_whetherdata_whether_whether','2023-11-16 09:33:24.865495'),(23,'myapp','0005_remove_volunteer_camp','2023-11-27 07:15:12.847941');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('3ta0i5qlb17r0oqfm45t0i5xzt6gneuv','eyJsZyI6ImxpbiIsImxpZCI6M30:1r7YRU:sIcrWnW-Ac7mNceM2ryN0vpRLJSmdsMNF3VvH-yk_ZI','2023-12-11 10:02:16.958277');

/*Table structure for table `myapp_adminmessage` */

DROP TABLE IF EXISTS `myapp_adminmessage`;

CREATE TABLE `myapp_adminmessage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_adminmessage` */

insert  into `myapp_adminmessage`(`id`,`message`) values (4,'try'),(5,'vgu'),(6,'r5ty'),(7,'dfg'),(8,'iu');

/*Table structure for table `myapp_alert` */

DROP TABLE IF EXISTS `myapp_alert`;

CREATE TABLE `myapp_alert` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `alert` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_alert` */

insert  into `myapp_alert`(`id`,`alert`) values (4,'drykk'),(5,'fgh');

/*Table structure for table `myapp_bank` */

DROP TABLE IF EXISTS `myapp_bank`;

CREATE TABLE `myapp_bank` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `accno` varchar(200) NOT NULL,
  `ifsc` varchar(200) NOT NULL,
  `balance` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `myapp_bank` */

/*Table structure for table `myapp_camp` */

DROP TABLE IF EXISTS `myapp_camp`;

CREATE TABLE `myapp_camp` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `latitude` varchar(200) NOT NULL,
  `longitude` varchar(200) NOT NULL,
  `SUBADMIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_camp_SUBADMIN_id_c17fc91c_fk_myapp_subadmin_id` (`SUBADMIN_id`),
  CONSTRAINT `myapp_camp_SUBADMIN_id_c17fc91c_fk_myapp_subadmin_id` FOREIGN KEY (`SUBADMIN_id`) REFERENCES `myapp_subadmin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_camp` */

insert  into `myapp_camp`(`id`,`name`,`latitude`,`longitude`,`SUBADMIN_id`) values (1,'efw','thrtjr','drerheh',3),(2,'vbn','12345','12345',3),(3,'vhu','yiyuo8u','yu',3),(4,'fgh','23456','23456',4);

/*Table structure for table `myapp_campallocation` */

DROP TABLE IF EXISTS `myapp_campallocation`;

CREATE TABLE `myapp_campallocation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `CAMP_id` bigint(20) NOT NULL,
  `Volunteer_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_campallocation_CAMP_id_8183da2d_fk_myapp_camp_id` (`CAMP_id`),
  KEY `myapp_campallocation_Volunteer_id_7a617671_fk_myapp_volunteer_id` (`Volunteer_id`),
  CONSTRAINT `myapp_campallocation_CAMP_id_8183da2d_fk_myapp_camp_id` FOREIGN KEY (`CAMP_id`) REFERENCES `myapp_camp` (`id`),
  CONSTRAINT `myapp_campallocation_Volunteer_id_7a617671_fk_myapp_volunteer_id` FOREIGN KEY (`Volunteer_id`) REFERENCES `myapp_volunteer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_campallocation` */

insert  into `myapp_campallocation`(`id`,`CAMP_id`,`Volunteer_id`) values (1,1,1);

/*Table structure for table `myapp_complaintesandreply` */

DROP TABLE IF EXISTS `myapp_complaintesandreply`;

CREATE TABLE `myapp_complaintesandreply` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaints` varchar(200) NOT NULL,
  `reply` varchar(200) NOT NULL,
  `SUBADMIN_id` bigint(20) NOT NULL,
  `VOLUNTEER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaintesand_SUBADMIN_id_c96dabee_fk_myapp_sub` (`SUBADMIN_id`),
  KEY `myapp_complaintesand_VOLUNTEER_id_9582cf5e_fk_myapp_vol` (`VOLUNTEER_id`),
  CONSTRAINT `myapp_complaintesand_SUBADMIN_id_c96dabee_fk_myapp_sub` FOREIGN KEY (`SUBADMIN_id`) REFERENCES `myapp_subadmin` (`id`),
  CONSTRAINT `myapp_complaintesand_VOLUNTEER_id_9582cf5e_fk_myapp_vol` FOREIGN KEY (`VOLUNTEER_id`) REFERENCES `myapp_volunteer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `myapp_complaintesandreply` */

/*Table structure for table `myapp_donation` */

DROP TABLE IF EXISTS `myapp_donation`;

CREATE TABLE `myapp_donation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `accno` varchar(200) NOT NULL,
  `ifsc` varchar(200) NOT NULL,
  `amount` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_donation` */

insert  into `myapp_donation`(`id`,`name`,`accno`,`ifsc`,`amount`) values (1,'sdds','768','67867','6787');

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(200) NOT NULL,
  `SUBADMIN_id` bigint(20) NOT NULL,
  `VOLUNTEER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_SUBADMIN_id_51aca572_fk_myapp_subadmin_id` (`SUBADMIN_id`),
  KEY `myapp_feedback_VOLUNTEER_id_02386d28_fk_myapp_volunteer_id` (`VOLUNTEER_id`),
  CONSTRAINT `myapp_feedback_SUBADMIN_id_51aca572_fk_myapp_subadmin_id` FOREIGN KEY (`SUBADMIN_id`) REFERENCES `myapp_subadmin` (`id`),
  CONSTRAINT `myapp_feedback_VOLUNTEER_id_02386d28_fk_myapp_volunteer_id` FOREIGN KEY (`VOLUNTEER_id`) REFERENCES `myapp_volunteer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `myapp_feedback` */

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'vol','vol','volunteer'),(3,'sub','sub','subadmin'),(4,'sub2','sub3','subadmin');

/*Table structure for table `myapp_needs` */

DROP TABLE IF EXISTS `myapp_needs`;

CREATE TABLE `myapp_needs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `list` varchar(200) NOT NULL,
  `quantityt` varchar(200) NOT NULL,
  `VOLUNTEER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_needs_VOLUNTEER_id_64a22392_fk_myapp_volunteer_id` (`VOLUNTEER_id`),
  CONSTRAINT `myapp_needs_VOLUNTEER_id_64a22392_fk_myapp_volunteer_id` FOREIGN KEY (`VOLUNTEER_id`) REFERENCES `myapp_volunteer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `myapp_needs` */

/*Table structure for table `myapp_precaution` */

DROP TABLE IF EXISTS `myapp_precaution`;

CREATE TABLE `myapp_precaution` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(200) NOT NULL,
  `file` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_precaution` */

/*Table structure for table `myapp_slot` */

DROP TABLE IF EXISTS `myapp_slot`;

CREATE TABLE `myapp_slot` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `totalslot` varchar(200) NOT NULL,
  `currentslot` varchar(200) NOT NULL,
  `VOLUNTEER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_slot_VOLUNTEER_id_eb07793e_fk_myapp_volunteer_id` (`VOLUNTEER_id`),
  CONSTRAINT `myapp_slot_VOLUNTEER_id_eb07793e_fk_myapp_volunteer_id` FOREIGN KEY (`VOLUNTEER_id`) REFERENCES `myapp_volunteer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `myapp_slot` */

/*Table structure for table `myapp_subadmin` */

DROP TABLE IF EXISTS `myapp_subadmin`;

CREATE TABLE `myapp_subadmin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `place` varchar(200) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_subadmin_LOGIN_id_07d935af_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_subadmin_LOGIN_id_07d935af_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_subadmin` */

insert  into `myapp_subadmin`(`id`,`name`,`email`,`phone`,`place`,`LOGIN_id`) values (3,'dry','ru','ryu','',1),(4,'dry','ru','ryu','',4),(5,'6r','r68u','r7i7','r7i7',1),(6,'6r','r68u','r7i7','huij',1),(7,'dryryty','r68u','r7i7','hui4',1),(8,'gyi','gyi','gyi','gyi',1),(9,'gyi','gyi','gyi','gyi',1),(10,'gyi','gyi','gyi','gyisf',1),(11,'sfgdds','','','',1),(12,'xdg','','','',1),(13,'hu','','','',1),(14,'nn','','','',1);

/*Table structure for table `myapp_subemergency` */

DROP TABLE IF EXISTS `myapp_subemergency`;

CREATE TABLE `myapp_subemergency` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `myapp_subemergency` */

/*Table structure for table `myapp_userdb` */

DROP TABLE IF EXISTS `myapp_userdb`;

CREATE TABLE `myapp_userdb` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `age` varchar(200) NOT NULL,
  `adress` varchar(200) NOT NULL,
  `phno` varchar(200) NOT NULL,
  `joiningdate` varchar(200) NOT NULL,
  `dismisaldate` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `myapp_userdb` */

/*Table structure for table `myapp_volunteer` */

DROP TABLE IF EXISTS `myapp_volunteer`;

CREATE TABLE `myapp_volunteer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `Login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_volunteer_Login_id_c246e41a_fk_myapp_login_id` (`Login_id`),
  CONSTRAINT `myapp_volunteer_Login_id_c246e41a_fk_myapp_login_id` FOREIGN KEY (`Login_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_volunteer` */

insert  into `myapp_volunteer`(`id`,`name`,`email`,`phone`,`Login_id`) values (1,'safs','segseg','segesgse',2),(2,'sdgh','rgasd','areg',1),(3,'ftyu','tu6u','t78',1);

/*Table structure for table `myapp_whether` */

DROP TABLE IF EXISTS `myapp_whether`;

CREATE TABLE `myapp_whether` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `whether` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_whether` */

insert  into `myapp_whether`(`id`,`whether`) values (6,'rthdgh');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
