-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2024 at 11:56 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendance_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendancemaster`
--

CREATE TABLE `attendancemaster` (
  `id` bigint(20) NOT NULL,
  `Slno` int(11) DEFAULT NULL,
  `login_datetime` datetime(6) DEFAULT NULL,
  `logout_datetime` datetime(6) DEFAULT NULL,
  `login_ipaddress` varchar(1000) DEFAULT NULL,
  `logout_ipaddress` varchar(1000) DEFAULT NULL,
  `company_id` bigint(20) DEFAULT NULL,
  `employee_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendancemaster`
--

INSERT INTO `attendancemaster` (`id`, `Slno`, `login_datetime`, `logout_datetime`, `login_ipaddress`, `logout_ipaddress`, `company_id`, `employee_id`) VALUES
(1, NULL, '2024-06-04 10:46:47.748500', '2024-06-04 10:47:02.558746', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1),
(2, NULL, '2024-06-04 11:44:40.902658', '2024-06-04 11:45:29.555283', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1),
(3, NULL, '2024-06-04 12:19:02.139035', '2024-06-04 12:19:25.909816', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1),
(4, NULL, '2024-06-04 12:19:48.594905', '2024-06-04 12:20:23.417523', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1),
(5, NULL, '2024-06-04 12:21:11.552837', '2024-06-04 12:21:30.528035', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1),
(6, NULL, '2024-06-04 12:21:43.292276', NULL, 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', NULL, 1, 1),
(7, NULL, '2024-06-04 12:21:51.301737', '2024-06-04 12:22:11.897638', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1),
(8, NULL, '2024-06-04 12:23:23.442558', '2024-06-04 12:24:02.212311', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1),
(9, NULL, '2024-06-04 14:50:41.697597', '2024-06-04 14:50:54.264635', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1),
(10, NULL, '2024-06-04 15:21:50.314068', '2024-06-04 15:21:56.158507', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 'Kakkanad, Ernakulam, Kanayannur, Ernakulam District, Kerala, 682030, India', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add nation', 6, 'add_nation'),
(22, 'Can change nation', 6, 'change_nation'),
(23, 'Can delete nation', 6, 'delete_nation'),
(24, 'Can view nation', 6, 'view_nation'),
(25, 'Can add user type', 7, 'add_usertype'),
(26, 'Can change user type', 7, 'change_usertype'),
(27, 'Can delete user type', 7, 'delete_usertype'),
(28, 'Can view user type', 7, 'view_usertype'),
(29, 'Can add state', 8, 'add_state'),
(30, 'Can change state', 8, 'change_state'),
(31, 'Can delete state', 8, 'delete_state'),
(32, 'Can view state', 8, 'view_state'),
(33, 'Can add city', 9, 'add_city'),
(34, 'Can change city', 9, 'change_city'),
(35, 'Can delete city', 9, 'delete_city'),
(36, 'Can view city', 9, 'view_city'),
(37, 'Can add user', 10, 'add_user'),
(38, 'Can change user', 10, 'change_user'),
(39, 'Can delete user', 10, 'delete_user'),
(40, 'Can view user', 10, 'view_user'),
(41, 'Can add nation master', 11, 'add_nationmaster'),
(42, 'Can change nation master', 11, 'change_nationmaster'),
(43, 'Can delete nation master', 11, 'delete_nationmaster'),
(44, 'Can view nation master', 11, 'view_nationmaster'),
(45, 'Can add state master', 12, 'add_statemaster'),
(46, 'Can change state master', 12, 'change_statemaster'),
(47, 'Can delete state master', 12, 'delete_statemaster'),
(48, 'Can view state master', 12, 'view_statemaster'),
(49, 'Can add city master', 13, 'add_citymaster'),
(50, 'Can change city master', 13, 'change_citymaster'),
(51, 'Can delete city master', 13, 'delete_citymaster'),
(52, 'Can view city master', 13, 'view_citymaster'),
(53, 'Can add company details', 14, 'add_companydetails'),
(54, 'Can change company details', 14, 'change_companydetails'),
(55, 'Can delete company details', 14, 'delete_companydetails'),
(56, 'Can view company details', 14, 'view_companydetails'),
(57, 'Can add department master', 15, 'add_departmentmaster'),
(58, 'Can change department master', 15, 'change_departmentmaster'),
(59, 'Can delete department master', 15, 'delete_departmentmaster'),
(60, 'Can view department master', 15, 'view_departmentmaster'),
(61, 'Can add designation master', 16, 'add_designationmaster'),
(62, 'Can change designation master', 16, 'change_designationmaster'),
(63, 'Can delete designation master', 16, 'delete_designationmaster'),
(64, 'Can view designation master', 16, 'view_designationmaster'),
(65, 'Can add employee master', 17, 'add_employeemaster'),
(66, 'Can change employee master', 17, 'change_employeemaster'),
(67, 'Can delete employee master', 17, 'delete_employeemaster'),
(68, 'Can view employee master', 17, 'view_employeemaster'),
(69, 'Can add company details', 18, 'add_companydetails'),
(70, 'Can change company details', 18, 'change_companydetails'),
(71, 'Can delete company details', 18, 'delete_companydetails'),
(72, 'Can view company details', 18, 'view_companydetails'),
(73, 'Can add employee department', 19, 'add_employeedepartment'),
(74, 'Can change employee department', 19, 'change_employeedepartment'),
(75, 'Can delete employee department', 19, 'delete_employeedepartment'),
(76, 'Can view employee department', 19, 'view_employeedepartment'),
(77, 'Can add employee designation', 20, 'add_employeedesignation'),
(78, 'Can change employee designation', 20, 'change_employeedesignation'),
(79, 'Can delete employee designation', 20, 'delete_employeedesignation'),
(80, 'Can view employee designation', 20, 'view_employeedesignation'),
(81, 'Can add employee image', 21, 'add_employeeimage'),
(82, 'Can change employee image', 21, 'change_employeeimage'),
(83, 'Can delete employee image', 21, 'delete_employeeimage'),
(84, 'Can view employee image', 21, 'view_employeeimage'),
(85, 'Can add employee join master', 22, 'add_employeejoinmaster'),
(86, 'Can change employee join master', 22, 'change_employeejoinmaster'),
(87, 'Can delete employee join master', 22, 'delete_employeejoinmaster'),
(88, 'Can view employee join master', 22, 'view_employeejoinmaster'),
(89, 'Can add attendance master', 23, 'add_attendancemaster'),
(90, 'Can change attendance master', 23, 'change_attendancemaster'),
(91, 'Can delete attendance master', 23, 'delete_attendancemaster'),
(92, 'Can view attendance master', 23, 'view_attendancemaster'),
(93, 'Can add role master', 24, 'add_rolemaster'),
(94, 'Can change role master', 24, 'change_rolemaster'),
(95, 'Can delete role master', 24, 'delete_rolemaster'),
(96, 'Can view role master', 24, 'view_rolemaster'),
(97, 'Can add working time', 25, 'add_workingtime'),
(98, 'Can change working time', 25, 'change_workingtime'),
(99, 'Can delete working time', 25, 'delete_workingtime'),
(100, 'Can view working time', 25, 'view_workingtime'),
(101, 'Can add time break master', 26, 'add_timebreakmaster'),
(102, 'Can change time break master', 26, 'change_timebreakmaster'),
(103, 'Can delete time break master', 26, 'delete_timebreakmaster'),
(104, 'Can view time break master', 26, 'view_timebreakmaster');

-- --------------------------------------------------------

--
-- Table structure for table `citymaster`
--

CREATE TABLE `citymaster` (
  `id` bigint(20) NOT NULL,
  `city` varchar(250) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `state_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `citymaster`
--

INSERT INTO `citymaster` (`id`, `city`, `pincode`, `state_id`) VALUES
(1, 'Bangalore', '560001', 1),
(2, 'Mumbai', '400001', 2),
(3, 'Los Angeles', '90001', 3),
(4, 'Houston', '77001', 4),
(5, 'Toronto', 'M5H 2N2', 5),
(6, 'Montreal', 'H2Y 1C6', 6),
(7, 'Tirupur', '641607', 7),
(8, 'Ernakulam', '682011', 8);

-- --------------------------------------------------------

--
-- Table structure for table `companydetails`
--

CREATE TABLE `companydetails` (
  `id` bigint(20) NOT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `reg_no` varchar(100) DEFAULT NULL,
  `company_icon` varchar(100) DEFAULT NULL,
  `company_logo` varchar(100) DEFAULT NULL,
  `city_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `companydetails`
--

INSERT INTO `companydetails` (`id`, `company_name`, `address`, `reg_no`, `company_icon`, `company_logo`, `city_id`, `user_id`) VALUES
(1, 'AKM', 'Kakkanad, Cochin', 'AK1010', 'company_images/1715068421813.jpg', 'company_images/lg.jpg', 8, 1),
(2, 'Buzcatch', 'Kinfra Hi-Tech Park ,Kalamaserry, Cochin', 'BUZ102', 'company_images/buzlogo_wFMeA5H.png', 'company_images/buzlogo_ZLsKGYz.png', 8, 3);

-- --------------------------------------------------------

--
-- Table structure for table `departmentmaster`
--

CREATE TABLE `departmentmaster` (
  `id` bigint(20) NOT NULL,
  `department` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departmentmaster`
--

INSERT INTO `departmentmaster` (`id`, `department`) VALUES
(1, 'IT Department'),
(2, 'Software Department'),
(3, 'HR Department'),
(4, 'Marketing Department');

-- --------------------------------------------------------

--
-- Table structure for table `designationmaster`
--

CREATE TABLE `designationmaster` (
  `id` bigint(20) NOT NULL,
  `designation` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `designationmaster`
--

INSERT INTO `designationmaster` (`id`, `designation`) VALUES
(1, 'Python Developer'),
(2, 'PHP Developer'),
(3, 'FrontEnd Developer'),
(4, 'Designer'),
(5, 'Digital Marketing'),
(6, 'Business Developer');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(9, 'attendance_app', 'city'),
(14, 'attendance_app', 'companydetails'),
(6, 'attendance_app', 'nation'),
(8, 'attendance_app', 'state'),
(10, 'attendance_app', 'user'),
(7, 'attendance_app', 'usertype'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(23, 'master', 'attendancemaster'),
(13, 'master', 'citymaster'),
(18, 'master', 'companydetails'),
(15, 'master', 'departmentmaster'),
(16, 'master', 'designationmaster'),
(19, 'master', 'employeedepartment'),
(20, 'master', 'employeedesignation'),
(21, 'master', 'employeeimage'),
(22, 'master', 'employeejoinmaster'),
(17, 'master', 'employeemaster'),
(11, 'master', 'nationmaster'),
(24, 'master', 'rolemaster'),
(12, 'master', 'statemaster'),
(26, 'master', 'timebreakmaster'),
(25, 'master', 'workingtime'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-24 05:23:52.052799'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-05-24 05:23:54.775508'),
(3, 'auth', '0001_initial', '2024-05-24 05:24:23.881282'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-05-24 05:25:54.643681'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-05-24 05:25:54.928966'),
(6, 'auth', '0004_alter_user_username_opts', '2024-05-24 05:25:55.214205'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-05-24 05:25:55.414349'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-05-24 05:25:55.615018'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-05-24 05:25:55.793492'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-05-24 05:25:55.930772'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-05-24 05:25:56.093595'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-05-24 05:25:56.648160'),
(13, 'auth', '0011_update_proxy_permissions', '2024-05-24 05:25:56.832738'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-05-24 05:25:56.995527'),
(15, 'attendance_app', '0001_initial', '2024-05-24 05:26:37.188377'),
(16, 'admin', '0001_initial', '2024-05-24 05:26:49.765242'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-05-24 05:26:49.981501'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-24 05:26:50.135230'),
(19, 'sessions', '0001_initial', '2024-05-24 05:26:51.940682'),
(20, 'attendance_app', '0002_alter_user_contact_no_alter_user_usertype', '2024-05-24 05:44:42.094798'),
(21, 'attendance_app', '0003_alter_user_usertype', '2024-05-24 06:31:50.621571'),
(22, 'attendance_app', '0004_remove_state_nation_delete_city_delete_nation_and_more', '2024-05-24 14:18:44.202019'),
(23, 'master', '0001_initial', '2024-05-24 14:29:03.959704'),
(24, 'master', '0002_statemaster', '2024-05-24 15:31:18.083628'),
(25, 'master', '0003_citymaster', '2024-05-24 15:37:06.086903'),
(26, 'master', '0004_departmentmaster_designationmaster', '2024-05-24 16:45:08.495901'),
(27, 'attendance_app', '0005_companydetails', '2024-05-24 16:45:15.728490'),
(28, 'master', '0005_employeemaster', '2024-05-24 16:49:00.336273'),
(29, 'attendance_app', '0006_delete_companydetails', '2024-05-24 17:38:54.386051'),
(30, 'master', '0006_companydetails', '2024-05-24 17:38:56.177501'),
(31, 'master', '0007_employeedepartment_employeedesignation_employeeimage_and_more', '2024-05-24 17:40:24.771433'),
(32, 'master', '0008_rename_deprtment_employeedepartment_department', '2024-05-25 06:36:14.613921'),
(33, 'master', '0009_alter_employeemaster_user', '2024-05-27 04:44:09.844558'),
(34, 'master', '0010_attendancemaster', '2024-05-27 05:19:57.567846'),
(35, 'master', '0011_alter_employeeimage_employee_image', '2024-05-27 08:36:21.721717'),
(36, 'master', '0012_alter_employeeimage_employee_image', '2024-05-27 09:36:50.157270'),
(37, 'master', '0013_rename_employee_id_employeemaster_employee_code', '2024-05-27 09:44:08.503632'),
(38, 'attendance_app', '0007_alter_user_options_alter_usertype_options', '2024-05-27 16:08:16.353888'),
(39, 'master', '0014_alter_attendancemaster_options_and_more', '2024-05-27 16:08:16.503587'),
(40, 'attendance_app', '0008_alter_user_options_alter_usertype_options_and_more', '2024-05-27 16:14:49.492603'),
(41, 'master', '0015_alter_attendancemaster_options_and_more', '2024-05-27 16:14:53.645436'),
(42, 'master', '0016_rolemaster', '2024-05-28 06:51:10.969301'),
(43, 'master', '0017_alter_rolemaster_table', '2024-05-28 07:00:49.523260'),
(44, 'master', '0018_delete_rolemaster', '2024-05-28 07:04:19.532839'),
(45, 'master', '0019_rolemaster', '2024-05-28 07:05:59.625852'),
(46, 'master', '0020_employeejoinmaster_role', '2024-05-28 07:15:17.978589'),
(47, 'master', '0021_alter_employeejoinmaster_join_date', '2024-05-28 08:32:24.584070'),
(48, 'master', '0022_alter_employeeimage_employee', '2024-05-28 09:21:31.932825'),
(49, 'master', '0023_companydetails_usertype_and_more', '2024-05-29 05:25:26.090180'),
(50, 'master', '0024_alter_companydetails_usertype', '2024-05-29 05:41:49.399503'),
(51, 'master', '0025_rename_usertype_companydetails_user', '2024-05-29 05:43:01.086109'),
(52, 'attendance_app', '0009_user_company', '2024-05-29 10:29:04.649855'),
(53, 'attendance_app', '0010_remove_user_company', '2024-05-29 10:53:01.792146'),
(54, 'master', '0026_workingtime', '2024-05-31 04:25:26.985318'),
(55, 'master', '0027_timebreakmaster_alter_workingtime_table', '2024-06-03 06:21:10.772759');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('12aipr5hm8g7qm82ak5vmc4b2xidmjsc', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXz:oounHgwhfgIfRzP_V_SjxGvMBY3VgRDD6KbMYvSv_v4', '2024-06-18 09:33:39.845175'),
('22h1ki0m1wscqb0i9xn89ydgdyk5v6x0', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQSA:QeOHWc1uXneNIeuAFzjLMXRv0EeT3AxtYfXriq0QBG8', '2024-06-18 09:27:38.947543'),
('aik6sapsbg2z2atgj66iv70h7q1reul9', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXt:FepNhDSuUu8jOYrHiYApLA7-isU34d-gaiS0z-ztEsw', '2024-06-18 09:33:33.680274'),
('azhmocfwu786qycqmk6tmszkubfbptph', '.eJxVi0EKwjAQRe-StZSM1U7iUvAc4c9kJEUtxaQr8e5W6EJ3n__ee7mEpZW0VHumMbuTI7f7_QR6s-kL0No6MKklzHO3gdpdHhjv5037awtqWcOgkW3QIzhczXIPOTBMKIgy-yxxHwMoQmlQ8t4oe8pM0vchwrO69wfdzzaX:1sCFsh:JMfMu38jVvd_lkQ8bF6g17uLT9I6ez1GJ2wA021R3yg', '2024-06-12 09:46:03.194929'),
('d8ct0y55gs0zuf0d6fbr0zpwuze3qvc0', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXz:oounHgwhfgIfRzP_V_SjxGvMBY3VgRDD6KbMYvSv_v4', '2024-06-18 09:33:39.825138'),
('dzjf9zammpm8hpf0yj481qs20zpyxkkl', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXt:FepNhDSuUu8jOYrHiYApLA7-isU34d-gaiS0z-ztEsw', '2024-06-18 09:33:33.846560'),
('et5xi3gqbwdsjzkxhhd8fz3mvt608gxz', '.eJxVi0EOwiAQRe_C2jRQYKAuTTwHmRmG0KhNI3RlvLs26UJ3P_-991IJt17T1uSZ5qzOyqrT70fIN1l2gL1_By4sCdd1OEAbrg-c75dD-2srtrqHoAFMMIxknLHBgXifsTCNObqReBKEGKxhH9hPsQBJKGwpi7YarHp_ALT5Njw:1sCyUU:cTlla0YDHGTfh3ExYjh5oO8LuDcB2IgwXe9fYBdVxQQ', '2024-06-14 09:24:02.732019'),
('h32s0toqlosd7aqq5eep89vc83q6o9gx', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXz:oounHgwhfgIfRzP_V_SjxGvMBY3VgRDD6KbMYvSv_v4', '2024-06-18 09:33:39.823133'),
('hbi8b6ig30v0ey13nflb82m4i4oow971', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQY7:Gj8lmM5ZLvfnMDqcCkX5boJyGuHy-Fo2Aq7z_4GE_SI', '2024-06-18 09:33:47.154385'),
('hcepemov8f9fqxjqokn2mctu5ocovnr2', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQY0:bmgwv5CkepPZkL7Li6N_lf5tcyqQ2OjPKNd_ZwaIs4g', '2024-06-18 09:33:40.958276'),
('hzuqacrza932yh1u271681qmnzl1k1je', '.eJxVi0EOwiAQRe_C2jQDLQO4NPEcZAaG0KhNI3RlvLs16UJ3P_-991KRtl7j1uQZ56zOalKn348p3WT5Aup9H7QkibSuwwHacH3QfL8c2l9bqdU9dOzEcpYEEEij1qIFMCRyAiwaJswFiw-2AFmPyGYcR284u2ysIVbvD8aJNjM:1sDHek:h7TVxcG4AlAYwABqgxjhn78v7vSG3MTbEXlrAQJ-kRQ', '2024-06-15 05:51:54.820696'),
('j6aaer98mwhy4z418ahgjbnwbih8mnt0', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQY6:q7e7W-_kcnMqmIfqKjEn3EHGQz4XZjqyoY8T1u1fJ0w', '2024-06-18 09:33:46.702325'),
('jim6aivfce7x6jtxvntdknhwaeuw6zv9', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sE2DU:wh1qnfREPM2_8tqN5Tmawn4vB0X6Kye6Owfn_zKPSYc', '2024-06-17 07:34:52.816487'),
('oc9lyxgn98k4r7eqabxgs5rvlwe52nay', '.eJxVi0EOwiAURO_C2jRf-B_EpYnnIAOloVGbRujKeHcx6UJ3L_PmvVTA1krYan6GeVRnJerwu0WkW16-Aq11wJJywLoOu6jD9YH5ftlvf21BLT2kGB2ZbI0bjYfxlkm0JJYk5Ch7Zp2oE8V0cgY8TQzNzjILIo6jen8AigA1Bg:1sDIir:tbCATOhJjibGy4I_Iu0DA78t6H1Qt8Rmp8M1V77A9UY', '2024-06-15 07:00:13.076866'),
('okemvjztysptrarkxy0v1ms1qa3lng40', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXt:FepNhDSuUu8jOYrHiYApLA7-isU34d-gaiS0z-ztEsw', '2024-06-18 09:33:33.644766'),
('onqzfzyipn8jy9j1hc4dkn9d80nf891w', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQY6:q7e7W-_kcnMqmIfqKjEn3EHGQz4XZjqyoY8T1u1fJ0w', '2024-06-18 09:33:46.195836'),
('ovebmbigswgtb3tca5lcfqtiby6n1leg', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sE2xi:XlvQykC22spMW4rLUbatu6neXeNmcE3-VbUpYYus5jY', '2024-06-17 08:22:38.775394'),
('qpfc81qboy15e83qkl5zzms1i6kbodxu', '.eJxVi0EOwiAURO_C2jS0Hwq4NPEcZID_Q6M2jbQr4921SRe6m8x776UitrXGrfEzTkWdlVOn3y8h33jeAdb1OzBnjliW7gCtuz4w3S-H9tdWtLqHjB5j8T6TNjrTSCIIViQZ9uyEBrBNwRjbw8GRZ53CACrBOzEi6v0B3CY24w:1sBXD9:GkYg9ZJHi19szBsAz1i8sfUHY9j3GD7CXJtiJfRZN68', '2024-06-10 10:04:11.116673'),
('qyceal3bpa1efvvzmf3xozbuzx117oy4', '.eJxVi0EKwjAQRe-StZSM1U7iUvAc4c9kJEUtxaQr8e5W6EJ3n__ee7mEpZW0VHumMbuTI7f7_QR6s-kL0No6MKklzHO3gdpdHhjv5037awtqWcOgkW3QIzhczXIPOTBMKIgy-yxxHwMoQmlQ8t4oe8pM0vchwrO69wfdzzaX:1sEMFb:mZhss6DEgX25pMdXER4HF1EIFjPAtUL1mT8jmUT-l70', '2024-06-18 04:58:23.366765'),
('twhznc25zewinu95xlw1ac2zmckplplf', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXz:oounHgwhfgIfRzP_V_SjxGvMBY3VgRDD6KbMYvSv_v4', '2024-06-18 09:33:39.823133'),
('w1rmc32tn3j5sautcn0sd3cofv2rdlej', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sCHMd:dPmUtqUj7bQj4I5B8EruqffSHp5aH-CWNy-IzFWevfE', '2024-06-12 11:21:03.895913'),
('x07ki7tjxn8b01gtgyg63zw92hnn0nvo', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sE22I:xdSLmGg-W6wC-ALk_F9IvTqQ9mIz-XHjZJ3xBq2ypKU', '2024-06-17 07:23:18.714691'),
('x9vhg3qmf9s1yzz8cww25dgpy8o8jz8f', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sE2CU:D5W-Ifq_72T8FPwzeI7jFPRCoJqr_gMy07H9aEWkjoM', '2024-06-17 07:33:50.707645'),
('xul3m2h5doxra6ju2pb8bu0mydgm2jr8', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXt:FepNhDSuUu8jOYrHiYApLA7-isU34d-gaiS0z-ztEsw', '2024-06-18 09:33:33.699767'),
('y06oow3k0m4vnn8rudu1in9k573mpgaf', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQY4:tTwfbV96_GGYbHlLUuD2-3iqAMi6x8UVLp30Idhbjjk', '2024-06-18 09:33:44.182832'),
('yns6rrhfyvvx4ijggv2fck5nn2ai84bo', '.eJxVi8sKwjAQRf8laylpM5OHS8HvCDNJhhS1FJOuxH-3Qhe6u9xzzktF2nqNWyvPOGd1VpM6_X5M6VaWL6De90FLKpHWdThAG64Pmu-XQ_trK7W6h9kSa5OcztpSmACDHcUj5KBHRGAuxgNYU9wYkgCiy2K8aBbnOBhR7w-fBzWU:1sEQXu:bCb_j2rjYMoNgNz-SJBXr4rxEIxr8K3oaabg0Ti1q0M', '2024-06-18 09:33:34.970062');

-- --------------------------------------------------------

--
-- Table structure for table `employeedepartment`
--

CREATE TABLE `employeedepartment` (
  `id` bigint(20) NOT NULL,
  `company_id` bigint(20) DEFAULT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `employee_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employeedepartment`
--

INSERT INTO `employeedepartment` (`id`, `company_id`, `department_id`, `employee_id`) VALUES
(1, NULL, 2, 1),
(2, NULL, 2, 2),
(3, NULL, 4, 3);

-- --------------------------------------------------------

--
-- Table structure for table `employeedesignation`
--

CREATE TABLE `employeedesignation` (
  `id` bigint(20) NOT NULL,
  `company_id` bigint(20) DEFAULT NULL,
  `designation_id` bigint(20) DEFAULT NULL,
  `employee_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employeedesignation`
--

INSERT INTO `employeedesignation` (`id`, `company_id`, `designation_id`, `employee_id`) VALUES
(1, NULL, 3, 1),
(2, NULL, 2, 2),
(3, NULL, 5, 3);

-- --------------------------------------------------------

--
-- Table structure for table `employeeimage`
--

CREATE TABLE `employeeimage` (
  `id` bigint(20) NOT NULL,
  `employee_image` varchar(100) DEFAULT NULL,
  `employee_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employeeimage`
--

INSERT INTO `employeeimage` (`id`, `employee_image`, `employee_id`) VALUES
(1, 'employee_images/SAVE_20230601_083804-min_YkukafA_KBPaS8f.jpg', 1),
(2, 'employee_images/t1.jpg', 2),
(3, 'employee_images/t1_ZSW30vN.jpg', 3);

-- --------------------------------------------------------

--
-- Table structure for table `employeejoinmaster`
--

CREATE TABLE `employeejoinmaster` (
  `id` bigint(20) NOT NULL,
  `join_date` date DEFAULT NULL,
  `company_id` bigint(20) DEFAULT NULL,
  `employee_id` bigint(20) DEFAULT NULL,
  `role_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employeejoinmaster`
--

INSERT INTO `employeejoinmaster` (`id`, `join_date`, `company_id`, `employee_id`, `role_id`) VALUES
(7, '2024-05-01', 1, 1, 2),
(8, '2024-04-15', 2, 2, 2),
(9, '2024-05-21', 2, 3, 2);

-- --------------------------------------------------------

--
-- Table structure for table `employeemaster`
--

CREATE TABLE `employeemaster` (
  `id` bigint(20) NOT NULL,
  `employee_code` varchar(50) DEFAULT NULL,
  `employee_name` varchar(250) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `city_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employeemaster`
--

INSERT INTO `employeemaster` (`id`, `employee_code`, `employee_name`, `address`, `city_id`, `user_id`) VALUES
(1, 'BZ1020', 'Arun Kumar M', 'Parapalayam', 7, 2),
(2, 'BZ1016', 'Anandhu Biju', 'Kakkanad', 8, 4),
(3, 'BZ1018', 'Thanseer S', 'Aluva, Cochin', 8, 5);

-- --------------------------------------------------------

--
-- Table structure for table `nationmaster`
--

CREATE TABLE `nationmaster` (
  `id` bigint(20) NOT NULL,
  `nation` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nationmaster`
--

INSERT INTO `nationmaster` (`id`, `nation`) VALUES
(1, 'India'),
(2, 'USA'),
(3, 'Canada');

-- --------------------------------------------------------

--
-- Table structure for table `rolemaster`
--

CREATE TABLE `rolemaster` (
  `id` bigint(20) NOT NULL,
  `role` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rolemaster`
--

INSERT INTO `rolemaster` (`id`, `role`) VALUES
(1, 'Admin'),
(2, 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `statemaster`
--

CREATE TABLE `statemaster` (
  `id` bigint(20) NOT NULL,
  `state` varchar(250) DEFAULT NULL,
  `nation_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `statemaster`
--

INSERT INTO `statemaster` (`id`, `state`, `nation_id`) VALUES
(1, 'Karnataka', 1),
(2, 'Maharashtra', 1),
(3, 'California', 2),
(4, 'Texas', 2),
(5, 'Ontario', 3),
(6, 'Quebec', 3),
(7, 'TamilNadu', 1),
(8, 'Kerala', 1);

-- --------------------------------------------------------

--
-- Table structure for table `timebreakmaster`
--

CREATE TABLE `timebreakmaster` (
  `id` bigint(20) NOT NULL,
  `tbreak` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usermaster`
--

CREATE TABLE `usermaster` (
  `id` bigint(20) NOT NULL,
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
  `contact_no` varchar(15) DEFAULT NULL,
  `usertype_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usermaster`
--

INSERT INTO `usermaster` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `contact_no`, `usertype_id`) VALUES
(1, 'pbkdf2_sha256$720000$I2onMYrPMASy0uvDxtKqz4$OabhfG5LMjN2Df2ELeSO6QkqDEFYHGb0/Gii2zUO5H0=', '2024-06-04 06:19:25.675823', 0, 'Ajithkumar', 'Ajith', 'Kumar', 'ajith123@gmail.com', 0, 1, '2024-05-29 09:45:28.228160', '8778445806', 1),
(2, 'pbkdf2_sha256$720000$7KGoopGxojwO7RpaY8gHbW$eWiWzHUrAd8TSYdi3CmvOTnl+Vwo9xmzvbwVwSafwVE=', '2024-06-04 09:54:30.008101', 0, 'Arunkumar', 'Arun', 'Kumar M', 'arun123@gmail.com', 0, 1, '2024-05-29 11:04:15.768107', '8778445807', 2),
(3, 'pbkdf2_sha256$720000$a7bVW9uKKNFNKCCu5XTKua$jm0KBbx/RQJUn/29pn+YBYzoEpkQaH5yJcCzPPcazfI=', '2024-05-31 09:24:02.573497', 0, 'abhijith', 'Abhijith', 'M', 'abhijith@buzcatch.com', 0, 1, '2024-05-30 05:08:26.511341', '7894561230', 1),
(4, 'pbkdf2_sha256$720000$q3SrcEmsGl3b4ISf6SKQx5$tP4EvXkpoYx32Uy87WTTDobvP+cgWCDhIVKz2OF6WH8=', '2024-06-01 05:51:53.977883', 0, 'Anandhu', 'Anandhu', 'Biju', 'anandhu@buzcatch.com', 0, 1, '2024-05-30 06:33:33.637073', '8956231470', 2),
(5, 'pbkdf2_sha256$720000$Am8RCuapl5fSpebmAexMIZ$l3wW2U65ws3t8lVjrm+DgRgn8bx9Zl2Hhz928Bo2HoA=', '2024-06-01 07:00:12.930299', 0, 'Thanseer', 'Thanseer', 'S', 'thanseer@buzcatch.com', 0, 1, '2024-06-01 06:57:01.132316', '9874563214', 2);

-- --------------------------------------------------------

--
-- Table structure for table `usermaster_groups`
--

CREATE TABLE `usermaster_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usermaster_user_permissions`
--

CREATE TABLE `usermaster_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usertype`
--

CREATE TABLE `usertype` (
  `id` bigint(20) NOT NULL,
  `usertype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usertype`
--

INSERT INTO `usertype` (`id`, `usertype`) VALUES
(1, 'Admin'),
(2, 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `workingtime`
--

CREATE TABLE `workingtime` (
  `id` bigint(20) NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `company_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `workingtime`
--

INSERT INTO `workingtime` (`id`, `start_time`, `end_time`, `company_id`, `user_id`) VALUES
(1, '09:30:00.000000', '17:30:00.000000', 1, 2),
(2, '09:00:00.000000', '17:00:00.000000', 2, 4),
(3, '09:30:00.000000', '17:30:00.000000', 2, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendancemaster`
--
ALTER TABLE `attendancemaster`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_attendancemas_company_id_80aea258_fk_master_co` (`company_id`),
  ADD KEY `master_attendancemas_employee_id_e235b711_fk_master_em` (`employee_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `citymaster`
--
ALTER TABLE `citymaster`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_citymaster_state_id_d06e2654_fk_master_statemaster_id` (`state_id`);

--
-- Indexes for table `companydetails`
--
ALTER TABLE `companydetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_companydetails_city_id_e35efba9_fk_master_citymaster_id` (`city_id`),
  ADD KEY `CompanyDetails_user_id_0df29d7b_fk_UserMaster_id` (`user_id`);

--
-- Indexes for table `departmentmaster`
--
ALTER TABLE `departmentmaster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `designationmaster`
--
ALTER TABLE `designationmaster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_attendance_app_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `employeedepartment`
--
ALTER TABLE `employeedepartment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_employeedepar_company_id_f4d23a38_fk_master_co` (`company_id`),
  ADD KEY `master_employeedepar_employee_id_cae62fa7_fk_master_em` (`employee_id`),
  ADD KEY `master_employeedepar_department_id_df418dcb_fk_master_de` (`department_id`);

--
-- Indexes for table `employeedesignation`
--
ALTER TABLE `employeedesignation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_employeedesig_company_id_0f8c3281_fk_master_co` (`company_id`),
  ADD KEY `master_employeedesig_designation_id_c8baa6a4_fk_master_de` (`designation_id`),
  ADD KEY `master_employeedesig_employee_id_ed549126_fk_master_em` (`employee_id`);

--
-- Indexes for table `employeeimage`
--
ALTER TABLE `employeeimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_employeeimage_employee_id_816be7a5_fk_master_em` (`employee_id`);

--
-- Indexes for table `employeejoinmaster`
--
ALTER TABLE `employeejoinmaster`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_employeejoinm_company_id_537cca38_fk_master_co` (`company_id`),
  ADD KEY `master_employeejoinm_employee_id_5fa66dab_fk_master_em` (`employee_id`),
  ADD KEY `EmployeeJoinMaster_role_id_95df2cf2_fk_RoleMaster_id` (`role_id`);

--
-- Indexes for table `employeemaster`
--
ALTER TABLE `employeemaster`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_employeemaster_city_id_903897b7_fk_master_citymaster_id` (`city_id`),
  ADD KEY `master_employeemaster_user_id_97a8692f_fk_attendance_app_user_id` (`user_id`);

--
-- Indexes for table `nationmaster`
--
ALTER TABLE `nationmaster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rolemaster`
--
ALTER TABLE `rolemaster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `statemaster`
--
ALTER TABLE `statemaster`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_statemaster_nation_id_eed7f7a9_fk_master_nationmaster_id` (`nation_id`);

--
-- Indexes for table `timebreakmaster`
--
ALTER TABLE `timebreakmaster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usermaster`
--
ALTER TABLE `usermaster`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `attendance_app_user_usertype_id_e9ced303_fk_attendanc` (`usertype_id`);

--
-- Indexes for table `usermaster_groups`
--
ALTER TABLE `usermaster_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `attendance_app_user_groups_user_id_group_id_35e2e3a6_uniq` (`user_id`,`group_id`),
  ADD KEY `attendance_app_user_groups_group_id_43966013_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `usermaster_user_permissions`
--
ALTER TABLE `usermaster_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `attendance_app_user_user_user_id_permission_id_818966e0_uniq` (`user_id`,`permission_id`),
  ADD KEY `attendance_app_user__permission_id_5e70fc82_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `usertype`
--
ALTER TABLE `usertype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `workingtime`
--
ALTER TABLE `workingtime`
  ADD PRIMARY KEY (`id`),
  ADD KEY `master_workingtime_company_id_c9a978ee_fk_CompanyDetails_id` (`company_id`),
  ADD KEY `master_workingtime_user_id_9a688704_fk_UserMaster_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendancemaster`
--
ALTER TABLE `attendancemaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `citymaster`
--
ALTER TABLE `citymaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `companydetails`
--
ALTER TABLE `companydetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `departmentmaster`
--
ALTER TABLE `departmentmaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `designationmaster`
--
ALTER TABLE `designationmaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `employeedepartment`
--
ALTER TABLE `employeedepartment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `employeedesignation`
--
ALTER TABLE `employeedesignation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `employeeimage`
--
ALTER TABLE `employeeimage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `employeejoinmaster`
--
ALTER TABLE `employeejoinmaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `employeemaster`
--
ALTER TABLE `employeemaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `nationmaster`
--
ALTER TABLE `nationmaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `rolemaster`
--
ALTER TABLE `rolemaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `statemaster`
--
ALTER TABLE `statemaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `timebreakmaster`
--
ALTER TABLE `timebreakmaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usermaster`
--
ALTER TABLE `usermaster`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `usermaster_groups`
--
ALTER TABLE `usermaster_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usermaster_user_permissions`
--
ALTER TABLE `usermaster_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usertype`
--
ALTER TABLE `usertype`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `workingtime`
--
ALTER TABLE `workingtime`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendancemaster`
--
ALTER TABLE `attendancemaster`
  ADD CONSTRAINT `master_attendancemas_company_id_80aea258_fk_master_co` FOREIGN KEY (`company_id`) REFERENCES `companydetails` (`id`),
  ADD CONSTRAINT `master_attendancemas_employee_id_e235b711_fk_master_em` FOREIGN KEY (`employee_id`) REFERENCES `employeemaster` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `citymaster`
--
ALTER TABLE `citymaster`
  ADD CONSTRAINT `master_citymaster_state_id_d06e2654_fk_master_statemaster_id` FOREIGN KEY (`state_id`) REFERENCES `statemaster` (`id`);

--
-- Constraints for table `companydetails`
--
ALTER TABLE `companydetails`
  ADD CONSTRAINT `CompanyDetails_user_id_0df29d7b_fk_UserMaster_id` FOREIGN KEY (`user_id`) REFERENCES `usermaster` (`id`),
  ADD CONSTRAINT `master_companydetails_city_id_e35efba9_fk_master_citymaster_id` FOREIGN KEY (`city_id`) REFERENCES `citymaster` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_attendance_app_user_id` FOREIGN KEY (`user_id`) REFERENCES `usermaster` (`id`);

--
-- Constraints for table `employeedepartment`
--
ALTER TABLE `employeedepartment`
  ADD CONSTRAINT `master_employeedepar_company_id_f4d23a38_fk_master_co` FOREIGN KEY (`company_id`) REFERENCES `companydetails` (`id`),
  ADD CONSTRAINT `master_employeedepar_department_id_df418dcb_fk_master_de` FOREIGN KEY (`department_id`) REFERENCES `departmentmaster` (`id`),
  ADD CONSTRAINT `master_employeedepar_employee_id_cae62fa7_fk_master_em` FOREIGN KEY (`employee_id`) REFERENCES `employeemaster` (`id`);

--
-- Constraints for table `employeedesignation`
--
ALTER TABLE `employeedesignation`
  ADD CONSTRAINT `master_employeedesig_company_id_0f8c3281_fk_master_co` FOREIGN KEY (`company_id`) REFERENCES `companydetails` (`id`),
  ADD CONSTRAINT `master_employeedesig_designation_id_c8baa6a4_fk_master_de` FOREIGN KEY (`designation_id`) REFERENCES `designationmaster` (`id`),
  ADD CONSTRAINT `master_employeedesig_employee_id_ed549126_fk_master_em` FOREIGN KEY (`employee_id`) REFERENCES `employeemaster` (`id`);

--
-- Constraints for table `employeeimage`
--
ALTER TABLE `employeeimage`
  ADD CONSTRAINT `master_employeeimage_employee_id_816be7a5_fk_master_em` FOREIGN KEY (`employee_id`) REFERENCES `employeemaster` (`id`);

--
-- Constraints for table `employeejoinmaster`
--
ALTER TABLE `employeejoinmaster`
  ADD CONSTRAINT `EmployeeJoinMaster_role_id_95df2cf2_fk_RoleMaster_id` FOREIGN KEY (`role_id`) REFERENCES `rolemaster` (`id`),
  ADD CONSTRAINT `master_employeejoinm_company_id_537cca38_fk_master_co` FOREIGN KEY (`company_id`) REFERENCES `companydetails` (`id`),
  ADD CONSTRAINT `master_employeejoinm_employee_id_5fa66dab_fk_master_em` FOREIGN KEY (`employee_id`) REFERENCES `employeemaster` (`id`);

--
-- Constraints for table `employeemaster`
--
ALTER TABLE `employeemaster`
  ADD CONSTRAINT `master_employeemaster_city_id_903897b7_fk_master_citymaster_id` FOREIGN KEY (`city_id`) REFERENCES `citymaster` (`id`),
  ADD CONSTRAINT `master_employeemaster_user_id_97a8692f_fk_attendance_app_user_id` FOREIGN KEY (`user_id`) REFERENCES `usermaster` (`id`);

--
-- Constraints for table `statemaster`
--
ALTER TABLE `statemaster`
  ADD CONSTRAINT `master_statemaster_nation_id_eed7f7a9_fk_master_nationmaster_id` FOREIGN KEY (`nation_id`) REFERENCES `nationmaster` (`id`);

--
-- Constraints for table `usermaster`
--
ALTER TABLE `usermaster`
  ADD CONSTRAINT `attendance_app_user_usertype_id_e9ced303_fk_attendanc` FOREIGN KEY (`usertype_id`) REFERENCES `usertype` (`id`);

--
-- Constraints for table `usermaster_groups`
--
ALTER TABLE `usermaster_groups`
  ADD CONSTRAINT `attendance_app_user__user_id_8dcb29ce_fk_attendanc` FOREIGN KEY (`user_id`) REFERENCES `usermaster` (`id`),
  ADD CONSTRAINT `attendance_app_user_groups_group_id_43966013_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `usermaster_user_permissions`
--
ALTER TABLE `usermaster_user_permissions`
  ADD CONSTRAINT `attendance_app_user__permission_id_5e70fc82_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `attendance_app_user__user_id_59204b73_fk_attendanc` FOREIGN KEY (`user_id`) REFERENCES `usermaster` (`id`);

--
-- Constraints for table `workingtime`
--
ALTER TABLE `workingtime`
  ADD CONSTRAINT `master_workingtime_company_id_c9a978ee_fk_CompanyDetails_id` FOREIGN KEY (`company_id`) REFERENCES `companydetails` (`id`),
  ADD CONSTRAINT `master_workingtime_user_id_9a688704_fk_UserMaster_id` FOREIGN KEY (`user_id`) REFERENCES `usermaster` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
