/*
Navicat MySQL Data Transfer

Source Server         : 192.168.60.145_3306
Source Server Version : 50726
Source Host           : 192.168.60.147:3306
Source Database       : oa

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2020-02-27 10:08:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for account_user
-- ----------------------------
DROP TABLE IF EXISTS `account_user`;
CREATE TABLE `account_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `staff_id` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `iphone` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `diqu` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `username` (`username`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE,
  UNIQUE KEY `staff_id` (`staff_id`) USING BTREE,
  UNIQUE KEY `iphone` (`iphone`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of account_user
-- ----------------------------
INSERT INTO `account_user` VALUES ('1', 'pbkdf2_sha256$150000$8Ea0w4ZZ0g6g$a7YxqUcDVFj+PxAE1M9gbuZe23DB0oHojJE+/tfQiMI=', '2020-02-26 10:42:19.964106', '0', 'admin', '管理员', '1@qq.com', 'A0', '1202111110', '陕西', '1');
INSERT INTO `account_user` VALUES ('2', 'pbkdf2_sha256$150000$I6X3sfujbOQr$7CXacLm7dPwbi5/iu6fw2fuHvRNcoe2JgX82nsgPR9k=', '2020-02-26 10:30:30.382724', '0', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa', '1');
INSERT INTO `account_user` VALUES ('3', 'pbkdf2_sha256$150000$1SvjQiutKx1J$bvEOMKL+O+eUZ4n2QhFigbfbGq2G4uqD9rgzqQRpbBg=', null, '0', 'admina', '管理员', '12@qq.com', 'A1', '1202111111', '陕西', '1');

-- ----------------------------
-- Table structure for account_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `account_user_groups`;
CREATE TABLE `account_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `account_user_groups_user_id_group_id_4d09af3e_uniq` (`user_id`,`group_id`) USING BTREE,
  KEY `account_user_groups_user_id_14345e7b` (`user_id`) USING BTREE,
  KEY `account_user_groups_group_id_6c71f749` (`group_id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=FIXED;

-- ----------------------------
-- Records of account_user_groups
-- ----------------------------
INSERT INTO `account_user_groups` VALUES ('1', '1', '1');
INSERT INTO `account_user_groups` VALUES ('2', '2', '2');
INSERT INTO `account_user_groups` VALUES ('3', '3', '1');

-- ----------------------------
-- Table structure for account_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `account_user_user_permissions`;
CREATE TABLE `account_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `account_user_user_permis_user_id_permission_id_48bdd28b_uniq` (`user_id`,`permission_id`) USING BTREE,
  KEY `account_user_user_permissions_user_id_cc42d270` (`user_id`) USING BTREE,
  KEY `account_user_user_permissions_permission_id_66c44191` (`permission_id`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=FIXED;

-- ----------------------------
-- Records of account_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES ('1', '管理组');
INSERT INTO `auth_group` VALUES ('2', '项目组');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`) USING BTREE,
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=FIXED;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES ('1', '1', '24');
INSERT INTO `auth_group_permissions` VALUES ('2', '1', '21');
INSERT INTO `auth_group_permissions` VALUES ('3', '1', '22');
INSERT INTO `auth_group_permissions` VALUES ('4', '1', '23');
INSERT INTO `auth_group_permissions` VALUES ('5', '1', '25');
INSERT INTO `auth_group_permissions` VALUES ('6', '1', '26');
INSERT INTO `auth_group_permissions` VALUES ('7', '1', '27');
INSERT INTO `auth_group_permissions` VALUES ('8', '1', '28');
INSERT INTO `auth_group_permissions` VALUES ('9', '1', '32');
INSERT INTO `auth_group_permissions` VALUES ('10', '1', '30');
INSERT INTO `auth_group_permissions` VALUES ('11', '2', '32');
INSERT INTO `auth_group_permissions` VALUES ('12', '2', '29');

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add user', '6', 'add_user');
INSERT INTO `auth_permission` VALUES ('22', 'Can change user', '6', 'change_user');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete user', '6', 'delete_user');
INSERT INTO `auth_permission` VALUES ('24', 'Can view user', '6', 'view_user');
INSERT INTO `auth_permission` VALUES ('25', 'Can add tjd_staff', '7', 'add_tjd_staff');
INSERT INTO `auth_permission` VALUES ('26', 'Can change tjd_staff', '7', 'change_tjd_staff');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete tjd_staff', '7', 'delete_tjd_staff');
INSERT INTO `auth_permission` VALUES ('28', 'Can view tjd_staff', '7', 'view_tjd_staff');
INSERT INTO `auth_permission` VALUES ('29', 'Can add xmsqd', '8', 'add_xmsqd');
INSERT INTO `auth_permission` VALUES ('30', 'Can change xmsqd', '8', 'change_xmsqd');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete xmsqd', '8', 'delete_xmsqd');
INSERT INTO `auth_permission` VALUES ('32', 'Can view xmsqd', '8', 'view_xmsqd');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6` (`user_id`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('6', 'account', 'user');
INSERT INTO `django_content_type` VALUES ('7', 'manageradmin', 'tjd_staff');
INSERT INTO `django_content_type` VALUES ('8', 'manager', 'xmsqd');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2020-02-24 08:10:03.155237');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2020-02-24 08:10:03.192777');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2020-02-24 08:10:03.239808');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2020-02-24 08:10:03.352406');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2020-02-24 08:10:03.355580');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2020-02-24 08:10:03.371812');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2020-02-24 08:10:03.383460');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2020-02-24 08:10:03.387058');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2020-02-24 08:10:03.389356');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2020-02-24 08:10:03.399404');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2020-02-24 08:10:03.418104');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0010_alter_group_name_max_length', '2020-02-24 08:10:03.436164');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0011_update_proxy_permissions', '2020-02-24 08:10:03.457257');
INSERT INTO `django_migrations` VALUES ('14', 'account', '0001_initial', '2020-02-24 08:10:03.511288');
INSERT INTO `django_migrations` VALUES ('15', 'admin', '0001_initial', '2020-02-24 08:10:03.655791');
INSERT INTO `django_migrations` VALUES ('16', 'admin', '0002_logentry_remove_auto_add', '2020-02-24 08:10:03.717071');
INSERT INTO `django_migrations` VALUES ('17', 'admin', '0003_logentry_add_action_flag_choices', '2020-02-24 08:10:03.726349');
INSERT INTO `django_migrations` VALUES ('18', 'manageradmin', '0001_initial', '2020-02-24 08:10:03.766266');
INSERT INTO `django_migrations` VALUES ('19', 'manager', '0001_initial', '2020-02-24 08:10:03.833041');
INSERT INTO `django_migrations` VALUES ('20', 'sessions', '0001_initial', '2020-02-24 08:10:03.925473');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  KEY `django_session_expire_date_a5c62663` (`expire_date`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('jkcaqpr8m3niv8w85vbwpuckuh68l3nx', 'YmIwMzViNGEzZTVjYWEzZDNlNmNkYjI0ZDg4OGU1NDhjZDdiMTVkNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZWFhMzVlMjhkOWQyYmVkNzhhZDFlZjQxMDg2OTg3ZmIzNDRjN2U3IiwidXNlcl9pZCI6MSwidXNlcl9ncm91cCI6Ilx1N2JhMVx1NzQwNlx1N2VjNCJ9', '2020-02-27 10:40:34.281156');
INSERT INTO `django_session` VALUES ('2wz3szbiund6l6b5fpfg2numcb54d6za', 'YmIwMzViNGEzZTVjYWEzZDNlNmNkYjI0ZDg4OGU1NDhjZDdiMTVkNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZWFhMzVlMjhkOWQyYmVkNzhhZDFlZjQxMDg2OTg3ZmIzNDRjN2U3IiwidXNlcl9pZCI6MSwidXNlcl9ncm91cCI6Ilx1N2JhMVx1NzQwNlx1N2VjNCJ9', '2020-02-27 10:42:19.985076');
INSERT INTO `django_session` VALUES ('rfc7fdlth4ze1iub12vg10wc9xa5nenh', 'YmIwMzViNGEzZTVjYWEzZDNlNmNkYjI0ZDg4OGU1NDhjZDdiMTVkNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZWFhMzVlMjhkOWQyYmVkNzhhZDFlZjQxMDg2OTg3ZmIzNDRjN2U3IiwidXNlcl9pZCI6MSwidXNlcl9ncm91cCI6Ilx1N2JhMVx1NzQwNlx1N2VjNCJ9', '2020-02-27 06:30:28.804768');
INSERT INTO `django_session` VALUES ('3bctkftn1ii4c3urymnobxxq0wfnfc04', 'ODdlZWNkYjFlOGQwYTlkZTYxMGM3YWNkZGNlOGQ0ZjhhNzMyMTkzMzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZDU4NWRhNzg0YTc4NjI5NjY0OTIxNjNiNjk2M2VlYjg1YjE0MDA3IiwidXNlcl9pZCI6MiwidXNlcl9ncm91cCI6Ilx1OTg3OVx1NzZlZVx1N2VjNCJ9', '2020-02-27 08:26:45.534812');
INSERT INTO `django_session` VALUES ('d7eakr296fewixdxju4bp3elf739mvui', 'YmIwMzViNGEzZTVjYWEzZDNlNmNkYjI0ZDg4OGU1NDhjZDdiMTVkNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZWFhMzVlMjhkOWQyYmVkNzhhZDFlZjQxMDg2OTg3ZmIzNDRjN2U3IiwidXNlcl9pZCI6MSwidXNlcl9ncm91cCI6Ilx1N2JhMVx1NzQwNlx1N2VjNCJ9', '2020-02-27 10:16:34.349814');
INSERT INTO `django_session` VALUES ('fmqagy580g1o791qr89wcim6o2lsqmf1', 'ODdlZWNkYjFlOGQwYTlkZTYxMGM3YWNkZGNlOGQ0ZjhhNzMyMTkzMzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZDU4NWRhNzg0YTc4NjI5NjY0OTIxNjNiNjk2M2VlYjg1YjE0MDA3IiwidXNlcl9pZCI6MiwidXNlcl9ncm91cCI6Ilx1OTg3OVx1NzZlZVx1N2VjNCJ9', '2020-02-27 10:30:30.398766');
INSERT INTO `django_session` VALUES ('fctity86gqzdj7p9vtqgk98nuu9992wv', 'YmIwMzViNGEzZTVjYWEzZDNlNmNkYjI0ZDg4OGU1NDhjZDdiMTVkNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZWFhMzVlMjhkOWQyYmVkNzhhZDFlZjQxMDg2OTg3ZmIzNDRjN2U3IiwidXNlcl9pZCI6MSwidXNlcl9ncm91cCI6Ilx1N2JhMVx1NzQwNlx1N2VjNCJ9', '2020-02-27 10:27:34.352785');

-- ----------------------------
-- Table structure for manageradmin_tjd_staff
-- ----------------------------
DROP TABLE IF EXISTS `manageradmin_tjd_staff`;
CREATE TABLE `manageradmin_tjd_staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `staff_id` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `jineng` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ruzhitime` date NOT NULL,
  `fazhan` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `diqu` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `dengji` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `zhuangtai` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `staff_id` (`staff_id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of manageradmin_tjd_staff
-- ----------------------------
INSERT INTO `manageradmin_tjd_staff` VALUES ('1', 'aaa', '111', '安服基础,渗透测试,天眼分析', '2020-02-27', '安全服务', '北京', '1', '1');
INSERT INTO `manageradmin_tjd_staff` VALUES ('2', 'bbb', '222', '天眼分析', '2020-02-25', '项目管理', '上海', '2', '1');
INSERT INTO `manageradmin_tjd_staff` VALUES ('3', 'ccc', '333', '渗透测试', '2020-02-10', '安全服务', '南京', '3', '0');
INSERT INTO `manageradmin_tjd_staff` VALUES ('4', 'd', '4', '渗透测试', '2020-02-10', '安全服务', '南京', '3', '1');
INSERT INTO `manageradmin_tjd_staff` VALUES ('5', 'e', '5', '渗透测试', '2020-02-10', '安全服务', '南京', '3', '1');
INSERT INTO `manageradmin_tjd_staff` VALUES ('6', 'f', '6', '渗透测试', '2020-02-10', '安全服务', '南京', '3', '1');
INSERT INTO `manageradmin_tjd_staff` VALUES ('7', 'g', '7', '渗透测试', '2020-02-10', '安全服务', '南京', '3', '1');
INSERT INTO `manageradmin_tjd_staff` VALUES ('8', 'h', '8', '渗透测试', '2020-02-10', '安全服务', '南京', '3', '0');
INSERT INTO `manageradmin_tjd_staff` VALUES ('9', 'i', '9', '渗透测试', '2020-02-10', '安全服务', '南京', '3', '0');

-- ----------------------------
-- Table structure for manager_xmsqd
-- ----------------------------
DROP TABLE IF EXISTS `manager_xmsqd`;
CREATE TABLE `manager_xmsqd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `xqid` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `xmname` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `xmdiqu` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `xqry` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `ryjn` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `bzxx` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `kstime` date NOT NULL,
  `jstime` date NOT NULL,
  `cjtime` date NOT NULL,
  `xqcltime` date DEFAULT NULL,
  `zhuangtai` int(11) NOT NULL,
  `clbz` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `access` longtext COLLATE utf8_unicode_ci NOT NULL,
  `xmjl_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `manager_xmsqd_xmjl_id_3fa0cb42` (`xmjl_id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of manager_xmsqd
-- ----------------------------
INSERT INTO `manager_xmsqd` VALUES ('1', 'test', 'test', 'test', '4', '天眼分析', '', '2020-02-26', '2020-02-24', '2020-02-24', '2020-02-24', '3', 'abc', '{\"111\": {\"name\": \"aaa\", \"access\": \"4\"}, \"222\": {\"name\": \"bbb\", \"access\": \"3\"}}', '2');
INSERT INTO `manager_xmsqd` VALUES ('2', '1234test', '1234test', '1234test', '2', '天眼分析', '1234test', '2020-02-26', '2020-02-26', '2020-02-24', '2020-02-26', '1', '', '{\"111\": {\"name\": \"aaa\", \"access\": \"\"}, \"222\": {\"name\": \"bbb\", \"access\": \"\"}, \"4\": {\"name\": \"d\", \"access\": \"\"}, \"5\": {\"name\": \"e\", \"access\": \"\"}, \"6\": {\"name\": \"f\", \"access\": \"\"}, \"7\": {\"name\": \"g\", \"access\": \"\"}}', '2');
INSERT INTO `manager_xmsqd` VALUES ('3', 'sadfasdf', 'sadfasdf', 'sadfasdf', '1', '渗透测试', '', '2020-02-25', '2020-02-25', '2020-02-25', null, '0', '', '', '2');

-- ----------------------------
-- Table structure for manager_xmsqd_fpry
-- ----------------------------
DROP TABLE IF EXISTS `manager_xmsqd_fpry`;
CREATE TABLE `manager_xmsqd_fpry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `xmsqd_id` int(11) NOT NULL,
  `tjd_staff_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `manager_xmsqd_fpry_xmsqd_id_tjd_staff_id_6c536b7f_uniq` (`xmsqd_id`,`tjd_staff_id`) USING BTREE,
  KEY `manager_xmsqd_fpry_xmsqd_id_e970acbc` (`xmsqd_id`) USING BTREE,
  KEY `manager_xmsqd_fpry_tjd_staff_id_d7aaaf38` (`tjd_staff_id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=FIXED;

-- ----------------------------
-- Records of manager_xmsqd_fpry
-- ----------------------------
INSERT INTO `manager_xmsqd_fpry` VALUES ('1', '1', '1');
INSERT INTO `manager_xmsqd_fpry` VALUES ('2', '1', '2');
INSERT INTO `manager_xmsqd_fpry` VALUES ('3', '2', '1');
INSERT INTO `manager_xmsqd_fpry` VALUES ('4', '2', '2');
INSERT INTO `manager_xmsqd_fpry` VALUES ('5', '2', '4');
INSERT INTO `manager_xmsqd_fpry` VALUES ('6', '2', '5');
INSERT INTO `manager_xmsqd_fpry` VALUES ('7', '2', '6');
INSERT INTO `manager_xmsqd_fpry` VALUES ('8', '2', '7');
