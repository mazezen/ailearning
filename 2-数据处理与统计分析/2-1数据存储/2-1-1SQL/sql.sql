-- 本系列 SQL 在 MySQL 中测试通过 
-- MySQL 版本 8.0.34
-- SQL (Structed Query Language: 结构化查询语言) 用于管理关系型数据库管理系统 RDBMS.
-- 以下数据 来源于 https://www.runoob.com/sql

SELECT @@version;

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `websites`
-- ----------------------------
DROP TABLE IF EXISTS `websites`;
CREATE TABLE `websites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL DEFAULT '' COMMENT '站点名称',
  `url` varchar(255) NOT NULL DEFAULT '',
  `alexa` int(11) NOT NULL DEFAULT '0' COMMENT 'Alexa 排名',
  `country` char(10) NOT NULL DEFAULT '' COMMENT '国家',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `websites`
-- ----------------------------
BEGIN;
INSERT INTO `websites` VALUES ('1', 'Google', 'https://www.google.cm/', '1', 'USA'), ('2', '淘宝', 'https://www.taobao.com/', '13', 'CN'), ('3', '菜鸟教程', 'http://www.runoob.com/', '4689', 'CN'), ('4', '微博', 'http://weibo.com/', '20', 'CN'), ('5', 'Facebook', 'https://www.facebook.com/', '3', 'USA');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;



SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `apps`
-- ----------------------------
DROP TABLE IF EXISTS `apps`;
CREATE TABLE `apps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` char(20) NOT NULL DEFAULT '' COMMENT '站点名称',
  `url` varchar(255) NOT NULL DEFAULT '',
  `country` char(10) NOT NULL DEFAULT '' COMMENT '国家',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `apps`
-- ----------------------------
BEGIN;
INSERT INTO `apps` VALUES ('1', 'QQ APP', 'http://im.qq.com/', 'CN'), ('2', '微博 APP', 'http://weibo.com/', 'CN'), ('3', '淘宝 APP', 'https://www.taobao.com/', 'CN');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;



SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `access_log`
-- ----------------------------
DROP TABLE IF EXISTS `access_log`;
CREATE TABLE `access_log` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) NOT NULL DEFAULT '0' COMMENT '网站id',
  `count` int(11) NOT NULL DEFAULT '0' COMMENT '访问次数',
  `date` date NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `access_log`
-- ----------------------------
BEGIN;
INSERT INTO `access_log` VALUES ('1', '1', '45', '2016-05-10'), ('2', '3', '100', '2016-05-13'), ('3', '1', '230', '2016-05-14'), ('4', '2', '10', '2016-05-14'), ('5', '5', '205', '2016-05-14'), ('6', '4', '13', '2016-05-15'), ('7', '3', '220', '2016-05-15'), ('8', '5', '545', '2016-05-16'), ('9', '3', '201', '2016-05-17');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;



SHOW TABLES;



------------------------------- SELECT -------------------------------
SELECT * FROM websites;
SELECT name, country FROM websites;

-- DISTINCT 用于返回指定列的唯一值
SELECT DISTINCT country FROM websites;

-- WHERE 提取满足条件的记录
SELECT * FROM websites WHERE country = 'CN';
SELECT * FROM websites WHERE id = 1;

-- AND & OR 运算符
-- 从 "Websites" 表中选取国家为 "CN" 且alexa排名大于 "50" 的所有网站
SELECT * FROM websites WHERE country = 'CN' AND alexa > 50;

-- 从 "Websites" 表中选取国家为 "USA" 或者 "CN" 的所有客户
SELECT * FROM websites WHERE country = "USA" OR country = "CN";
SELECT * FROM websites WHERE country IN ('USA', 'CN');

-- 从 "Websites" 表中选取 alexa 排名大于 "15" 且国家为 "CN" 或 "USA" 的所有网站
SELECT * FROM websites WHERE alexa > 15 AND country IN ("CN", "USA");
SELECT * FROM websites WHERE alexa > 15 AND (country = "CN" OR country = "USA");

-- ORDER BY
-- 从 "Websites" 表中选取所有网站，并按照 "alexa" 列排序
SELECT * FROM websites ORDER BY alexa DESC; -- 按照降序排列
SELECT * FROM websites ORDER BY alexa ASC;  -- 按照升序排列

-- ORDER BY 队列时, 逗号分割字段
-- 从 "Websites" 表中选取所有网站，并按照 "country" 和 "alexa" 列排序
SELECT * FROM websites ORDER BY alexa, country DESC;


------------------------------- INSERT INTO -------------------------------
INSERT INTO websites (name, url, alexa, country) VALUES ("百度", "https://baidu.com", 4, "CN");
-- 查看最新写入的数据
SELECT * FROM websites ORDER BY id DESC LIMIT 1;

-- 指定的列写入数据
INSERT INTO websites (name, url, country) VALUES ("stackoverflow", "https://stackoverflow.com", "IND");
SELECT * FROM websites ORDER BY id DESC LIMIT 1;


------------------------------- UPDATE -------------------------------
-- 把 "菜鸟教程" 的 alexa 排名更新为 5000，country 改为 USA
SELECT * FROM websites;
UPDATE websites SET alexa = 5000, country = "USA" WHERE name = "菜鸟教程";
SELECT * FROM websites;


------------------------------- DELETE -------------------------------
SELECT count(1) from websites;
DELETE FROM websites WHERE name = "菜鸟教程";
SELECT count(1) FROM websites;
SELECT * FROM websites;

-- 删除整张表中的所有记录
-- DELETE FROM websites;


------------------------------- SELECT TOP -------------------------------
-- 返回前3行的数据
SELECT * FROM websites ORDER BY id ASC LIMIT 3;


------------------------------- LIKE -------------------------------
-- 选取 name 以字母 "G" 开始的所有客户
SELECT * FROM websites WHERE name LIKE 'G%';
-- 选取 name 第二个字母 为 t的客户
SELECT * FROM websites WHERE name LIKE '_t%';
-- 选取 name 以字母 "k" 结尾的所有客户
SELECT * FROM websites WHERE name LIKE '%k';
-- 选取 name 包含模式 "oo" 的所有客户
SELECT * FROM websites WHERE name LIKE '%oo%';
-- 选取 name 不包含模式 "oo" 的所有客户
SELECT * FROM websites WHERE name NOT LIKE '%oo%';


------------------------------- 通配符 -------------------------------
-- 选取 url 以字母 "https" 开始的所有网站
SELECT * FROM websites WHERE url LIKE 'https%';
-- url 包含模式 "oo" 的所有网站
SELECT * FROM websites WHERE url LIKE '%oo%';

-- _ 通配符
-- 选取 name 以一个任意字符开始，然后是 "oogle" 的所有客户
SELECT * FROM websites WHERE name LIKE '_oogle';
-- 选取 name 以 "G" 开始，然后是一个任意字符，然后是 "o"，然后是一个任意字符，然后是 "le" 的所有网站
SELECT * FROM websites WHERE name LIKE 'G_o_le';

-- [charlist] 通配符
-- 选取 name 以 "G"、"F" 或 "s" 开始的所有网站
SELECT * from websites WHERE name REGEXP '^[GFs]';
-- 选取 name 以 A 到 H 字母开头的网站
SELECT * FROM websites WHERE name REGEXP '^[A-H]';
-- 选取 name 不以 A 到 H 字母开头的网站
SELECT * FROM websites WHERE name NOT REGEXP '^[A-H]';
SELECT * FROM websites WHERE name REGEXP '^[^A-H]';


------------------------------- IN -------------------------------
-- 选取 name 为 "Google" 或 "菜鸟教程" 的所有网站
SELECT * FROM websites WHERE name IN ('google', 'stackoverflow');


------------------------------- BETWEEN -------------------------------
-- 选取 alexa 介于 1 和 20 之间的所有网站
SELECT * FROM websites WHERE alexa BETWEEN 1 AND 20;
SELECT * FROM websites WHERE alexa NOT BETWEEN 1 AND 20;
-- 选取 alexa 介于 1 和 20 之间但 country 不为 USA 和 IND 的所有网站
SELECT * FROM websites WHERE alexa BETWEEN 1 AND 20 AND country NOT IN ('USA', 'IND');
-- 选取 name 以介于 'A' 和 'H' 之间字母开始的所有网站
SELECT * FROM websites WHERE name REGEXP '^[A-H]';
SELECT * FROM websites WHERE name BETWEEN 'A' AND 'H';
-- 选取 name 不介于 'A' 和 'H' 之间字母开始的所有网站
SELECT * FROM websites WHERE name REGEXP '^[^A-H]';
SELECT * FROM websites WHERE name NOT BETWEEN 'A' AND 'H';

SELECT * from access_log;
-- 选取 date 介于 '2016-05-10' 和 '2016-05-14' 之间的所有访问记录
SELECT * FROM access_log WHERE `date` BETWEEN '2016-05-10' AND '2016-05-14';


------------------------------- ALIAS NAME -------------------------------
-- 指定了两个别名，一个是 name 列的别名，一个是 country 列的别名。提示：如果列名称包含空格，要求使用双引号或方括号
SELECT name as 名称, country as 国家 FROM websites;

-- 把三个列（url、alexa 和 country）结合在一起，并创建一个名为 "site_info" 的别名
SELECT name, CONCAT(url, ', ', alexa, ', ', country) as site_info FROM websites;

-- 表的别名
SELECT w.name, w.url, a.count, a.date FROM websites as w, access_log as a WHERE w.id = a.aid AND w.name = "Google";
SELECT w.name, CONCAT(w.url, ', ', w.alexa, ', ', w.country) as site_info, a.date FROM websites as w, access_log as a WHERE w.id = a.aid AND w.alexa > 1;

------------------------------- JOIN -------------------------------
SELECT w.id, w.name, l.count, l.date FROM websites as w INNER JOIN access_log as l ON w.id = l.site_id;

SELECT w.id, w.name, l.count, l.date FROM websites as w LEFT JOIN access_log as l ON w.id = l.site_id ORDER BY l.count DESC;

INSERT INTO `access_log` (`aid`, `site_id`, `count`, `date`) VALUES ('11', '12', '111', '2016-03-09');
SELECT * from access_log;
SELECT * from websites;
SELECT w.id, w.name, l.site_id, l.count, l.date FROM websites as w RIGHT JOIN access_log as l ON w.id = l.site_id ORDER BY l.count DESC;

SELECT country FROM websites UNION SELECT country FROM apps ORDER BY country;
SELECT country FROM websites UNION ALL SELECT country FROM apps ORDER BY country;
SELECT country, name FROM websites WHERE country = 'CN' UNION ALL SELECT country, app_name FROM apps WHERE country = 'CN' ORDER BY country;

------------------------------- SELECT INTO -------------------------------
-- mysql 不支持 SELECT INTO ,但是支持 INSERT INTO ... SELECT
-- 也可以使用 
-- CREATE TABLE 新表
-- AS
-- SELECT * FROM 旧表
-- MYSQL 和 PostgreSQL
CREATE TABLE websites_backup AS SELECT * FROM websites;
SHOW TABLES;
SELECT * FROM websites_backup;

INSERT INTO websites (name, country) SELECT app_name, country FROM apps;
SELECT * FROM websites;


------------------------------- CONSTRAINT -------------------------------
-- NOT NULL
CREATE TABLE students (
    StudentID INT NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50),
    Age INT
);

-- UNIQUE
CREATE TABLE employees (
    EmployeeID INT NOT NULL UNIQUE,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50),
    Email VARCHAR(100) NOT NULL
);
CREATE INDEX idx_lastname ON employees (LastName);

CREATE TABLE orders (
    ID BIGINT PRIMARY KEY AUTO_INCREMENT,
    OrderNumber VARCHAR(50) NOT NULL,
    OrderDate DATE NOT NULL
);

CREATE TABLE orders (
    OrderID INT NOT NULL PRIMARY KEY,
    OrderNumber INT NOT NULL,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Customers (
    CustomerID INT NOT NULL PRIMARY KEY,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50),
    JoinDate DATE DEFAULT GETDATE()
);

-- NOT NULL
CREATE TABLE perons (
    ID INT NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    Age INT
);
-- 在一个已存在的表 person中为Age字段添加 NOT NULL 约束
ALTER TABLE perons MODIFY Age INT NOT NULL;
-- 在一个已存在的表 person中为Age字段删除 NOT NULL 约束
ALTER TABLE perons MODIFY Age INT NULL;


-- UNIQUE
ALTER TABLE perons ADD UNIQUE (ID);
ALTER TABLE perons ADD CONSTRAINT uc_personID UNIQUE (ID, LastName);

ALTER TABLE perons DROP INDEX uc_personID;

-- PRIMARY KEY
ALTER TABLE perons ADD PRIMARY KEY (ID);
ALTER TABLE perons ADD CONSTRAINT pk_peronsID PRIMARY KEY (ID, LastName);
ALTER TABLE perons DROP PRIMARY KEY;
ALTER TABLE perons DROP CONSTRAINT pl_peronsID;

-- CHECK
CREATE TABLE persons (
    P_Id INT NOT NULL,
    LastName varchar(50) NOT NULL,
    FirstName varchar(50),
    Address VARCHAR(255),
    City VARCHAR(255),
    CONSTRAINT chk_Person CHECK  (P_Id > 0 AND City = 'Sandnes')
);
ALTER TABLE perons ADD CHECK (P_Id>0);
ALTER TABLE perons ADD CONSTRAINT chk_Person CHECK (P_Id > 0 AND City = 'Sandnes');
ALTER TABLE perons DROP CHECK chk_Person;

-- DEFAULT
SELECT CURRENT_TIMESTAMP; -- 查询当前日期和时间
CREATE TABLE employees (
    ID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    HireDate DATE DEFAULT CURRENT_TIMESTAMP, -- 默认当前日期
    Salary DECIMAL(10, 2) DEFAULT 0.00 -- 默认值为 0.00
);

-- 在现有表中的字段添加默认值
ALTER TABLE employees ALTER COLUMN Salary SET DEFAULT 1.00;
-- 删除默认值
ALTER TABLE employees ALTER COLUMN Salary DROP DEFAULT;

------------------------------- VIEWS -------------------------------
-- 1. 视图隐藏了底层数据结构, 简化了数据访问操作, 客户端不再需要知道底层表的结构及其之间的关系.
-- 2. 视图提供了一个统一访问数据的接口.(允许用户可以通过视图访问数据的安全机制, 而不授予用户直接访问底层表的权限.)
-- 3. 加强了安全性. 使用户只能看到视图显示的数据.
-- 4. 视图还可以嵌套. 一个视图可以嵌套另一个视图
SELECT * FROM websites;
-- CREATE
CREATE VIEW websites_cn AS
SELECT id, name, url, alexa, country
FROM websites
WHERE country = 'CN';

INSERT INTO websites (id, name, url, alexa, country) VALUES (11, "blue sky", "https://bsky.app", 1000, 'CN');

SELECT * FROM websites_cn;

-- UPDATE
-- 无法直接更新视图, 视图是基于原有表创建的虚拟表. 如要更新视图,需更新原有表中的数据, 视图将自动反应这些变化


-- 删除视图
DROP VIEW IF EXISTS websites_cn;


------------------------------- 日期 -------------------------------
SELECT NOW(); -- 返回当前的日期和时间
SELECT CURDATE(); -- 返回当前的日子
SELECT CURTIME(); -- 返回当前的时间
SELECT DATE(date) from access_log; -- 提取日期
SELECT EXTRACT(YEAR FROM date) as DateYear FROM access_log;

------------------------------- 函数 -------------------------------
-- AVG
SELECT * FROM access_log;
SELECT AVG(count) as avg_count FROM access_log;
SELECT * FROM access_log WHERE count > (SELECT AVG(count) FROM access_log);

-- COUNT
SELECT COUNT(1) AS nums FROM access_log;
SELECT COUNT(DISTINCT site_id) as nums FROM access_log;

-- FIRST
SELECT name as FirstSite FROM websites LIMIT 1;
-- LAST
SELECT name as LastSite FROM websites ORDER BY name DESC LIMIT 1;

-- MAX
SELECT MAX(count) as max_count FROM access_log;
SELECT MIN(count) as min_count FROM access_log;

-- SUM
SELECT sum(count) as sum_count FROM access_log;

-- GROUP BY
SELECT site_id, sum(access_log.count) as nums FROM access_log GROUP BY site_id;
SELECT websites.name, count(access_log.aid) as nums FROM access_log LEFT JOIN websites ON access_log.site_id = websites.id GROUP BY websites.name;


-- HAVING
SELECT websites.name, websites.url, SUM(access_log.count) AS nums FROM (access_log
INNER JOIN Websites
ON access_log.site_id=websites.id)
GROUP BY websites.name
HAVING SUM(access_log.count) > 200;


-- EXISTS
SELECT websites.name, websites.url
FROM websites
WHERE EXISTS (SELECT count FROM access_log WHERE websites.id = access_log.site_id AND count > 200);

SELECT websites.name, websites.url
FROM websites
WHERE NOT EXISTS (SELECT count FROM access_log WHERE websites.id = access_log.site_id AND count > 200);

-- UCASE
SELECT UCASE(name) as site_title, url FROM websites;

-- LCASE
SELECT LCASE(name) as site_title, url FROM websites;

-- MID
SELECT MID(name, 1, 4) site_title FROM websites;

-- LEN
SELECT LENGTH(name) as len_name FROM websites;
SELECT LENGTH(url) as len_url FROM websites;

-- ROUND
SELECT ROUND(-1.23);
SELECT ROUND(-1.58);
SELECT ROUND(1.2998, 1);

-- NOW
SELECT NOW();
SELECT name, url, NOW() as date_time FROM websites;

-- FORMAT
SELECT name, url, DATE_FORMAT(NOW(), '%Y-%m-%d') as date FROM websites;
