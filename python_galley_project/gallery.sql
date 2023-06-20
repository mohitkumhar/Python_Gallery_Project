-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2023 at 02:36 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_album_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `gallery`
--

CREATE TABLE `gallery` (
  `sno` int(255) NOT NULL,
  `memories` text NOT NULL,
  `slug` varchar(50) NOT NULL,
  `img_file` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gallery`
--

INSERT INTO `gallery` (`sno`, `memories`, `slug`, `img_file`, `date`) VALUES
(2, 'second one', 'second-photo', '1.jpg', '2023-06-19 22:36:58'),
(3, 'third', 'third-photo', '2.jpg', '2023-06-19 22:35:43'),
(4, 'fourth', 'fourth-post', '4.png', '2023-06-19 14:26:12'),
(5, 'fifth', 'fifth-post', '5.jpg', '2023-06-19 22:10:54'),
(6, 'sixth', 'sixth-post', '6.jpg', '2023-06-19 22:14:26'),
(7, 'seventh', 'seventh-post', '7.png', '2023-06-19 16:31:46'),
(8, 'eighth', 'eight-post', '8.png', '2023-06-19 16:31:48'),
(9, 'ninth', 'ninth-post', '9.png', '2023-06-19 16:31:51'),
(10, 'tenth', 'tenth-post', '10.png', '2023-06-19 20:25:41'),
(11, 'eleventh', 'eleventh-post', '11.png', '2023-06-19 20:26:45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gallery`
--
ALTER TABLE `gallery`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gallery`
--
ALTER TABLE `gallery`
  MODIFY `sno` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
