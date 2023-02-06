/*
 Navicat Premium Data Transfer

 Source Server         : lqq
 Source Server Type    : MySQL
 Source Server Version : 80030
 Source Host           : localhost:3306
 Source Schema         : hotel

 Target Server Type    : MySQL
 Target Server Version : 80030
 File Encoding         : 65001

 Date: 07/01/2023 23:59:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `account_unique_admin`(`account` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'imboss', '123456');
INSERT INTO `admin` VALUES (2, 'immanager', '123456');

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sex` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ID_card` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone_number` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `cust_idcard_unique`(`ID_card` ASC) USING BTREE,
  CONSTRAINT `cust_check_sex` CHECK ((`sex` = _utf8mb4'男') or (`sex` = _utf8mb4'女'))
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES (1, '刘比替', '男', '440101', '13788888888');
INSERT INTO `customer` VALUES (2, '刘比水', '女', '44558', '444888');
INSERT INTO `customer` VALUES (3, '符文静', '女', '44526', '4488822');
INSERT INTO `customer` VALUES (4, '吴除山', '男', '48958', '77895565');

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `state` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `room_id` int NOT NULL,
  `cust_id` int NOT NULL,
  `staff_id` int NOT NULL,
  `start_time` date NOT NULL,
  `end_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_custid`(`cust_id` ASC) USING BTREE,
  INDEX `fk_roomnum`(`room_id` ASC) USING BTREE,
  INDEX `fk_stfid`(`staff_id` ASC) USING BTREE,
  CONSTRAINT `fk_custid` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_roomnum` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_number`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_stfid` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `od_check_state` CHECK ((`state` = _utf8mb4'进行中') or (`state` = _utf8mb4'已结束'))
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES (1, '已结束', 1908, 3, 1, '2023-01-02', '2023-01-07');
INSERT INTO `order` VALUES (2, '已结束', 1306, 1, 1, '2023-01-02', '2023-01-03');
INSERT INTO `order` VALUES (3, '已结束', 1408, 2, 1, '2023-01-04', '2023-01-04');
INSERT INTO `order` VALUES (4, '进行中', 1306, 2, 1, '2023-01-04', NULL);
INSERT INTO `order` VALUES (5, '进行中', 1307, 1, 1, '2023-01-05', NULL);
INSERT INTO `order` VALUES (6, '进行中', 1808, 4, 1, '2023-01-06', NULL);

-- ----------------------------
-- Table structure for room
-- ----------------------------
DROP TABLE IF EXISTS `room`;
CREATE TABLE `room`  (
  `room_number` int NOT NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  `state` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`room_number`) USING BTREE,
  CONSTRAINT `rm_check_state` CHECK ((`state` = _utf8mb4'待清洁') or (`state` = _utf8mb4'可入住') or (`state` = _utf8mb4'使用中')),
  CONSTRAINT `rm_check_type` CHECK ((`type` = _utf8mb4'标准单人房') or (`type` = _utf8mb4'标准双人房') or (`type` = _utf8mb4'豪华大床房') or (`type` = _utf8mb4'顶级总统套房'))
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of room
-- ----------------------------
INSERT INTO `room` VALUES (1304, '标准单人房', 200.00, '可入住');
INSERT INTO `room` VALUES (1305, '标准单人房', 200.00, '可入住');
INSERT INTO `room` VALUES (1306, '标准单人房', 200.00, '使用中');
INSERT INTO `room` VALUES (1307, '标准单人房', 200.00, '使用中');
INSERT INTO `room` VALUES (1407, '标准双人房', 400.00, '可入住');
INSERT INTO `room` VALUES (1408, '标准双人房', 400.00, '待清洁');
INSERT INTO `room` VALUES (1808, '豪华大床房', 800.00, '使用中');
INSERT INTO `room` VALUES (1908, '顶级总统套房', 1500.00, '待清洁');

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '姓名',
  `account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '员工类型',
  `phone_number` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `sex` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `account_unique`(`account` ASC) USING BTREE,
  CONSTRAINT `stf_check_sex` CHECK ((`sex` = _utf8mb4'男') or (`sex` = _utf8mb4'女')),
  CONSTRAINT `stf_check_type` CHECK ((`type` = _utf8mb4'前台') or (`type` = _utf8mb4'清洁'))
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES (1, '黎鸣', 'lm', '123456', '前台', '52228', '男');
INSERT INTO `staff` VALUES (2, '张薛有', 'zxy', '123456', '清洁', '68889', '女');

-- ----------------------------
-- Triggers structure for table order
-- ----------------------------
DROP TRIGGER IF EXISTS `check_in`;
delimiter ;;
CREATE TRIGGER `check_in` AFTER INSERT ON `order` FOR EACH ROW UPDATE room set state='使用中' where room_number=new.room_id
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table order
-- ----------------------------
DROP TRIGGER IF EXISTS `check_out`;
delimiter ;;
CREATE TRIGGER `check_out` AFTER UPDATE ON `order` FOR EACH ROW IF
	new.state = "已结束" THEN
		UPDATE room 
		SET state = '待清洁' 
	WHERE
		room_number = new.room_id;

END IF
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
