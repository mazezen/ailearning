<?php
// 自 PHP 5.3 开始默认启用 SQLite3 扩展. 可通过 php -i 查看. 
// 可以在编译时使用 --without-sqlite3 禁用 SQLite3 扩展

// > php sqlite3.php
class SQLiteClass extends SQLite3
{
    public $db;

    // 通过 __construct 构造函数打开 SQLite3数据库文件
    // 如果数据库文件不存在,则创建
    public function  __construct()
    {
        $db = $this->open("php-test.db");
    }

    /**
     * checkDbOpen
     * 
     * 检查数据库是否打开成功
     */
    public function checkDbOpen() {
        if ($this->db) {
            echo "code: " . $db -> lastErrorCode . "msg: " . $db -> lastErrorMsg();
        } else {
            echo "Opend database successfully\n";
        }
    }

    /**
     * createTable
     * 
     * 创建数据表 COMPANY
     */
    public function createTable() {
        $create_sql =<<<EOF
CREATE TABLE IF NOT EXISTS COMPANY(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
);
EOF;

        $ret = $this->exec($create_sql);
        if (!$ret) {
            echo "创建表失败: code: " . $db -> lastErrorCode . "msg: " . $db -> lastErrorMsg();
        } else {
            echo "Create COMPANY table successfully...\n";
        }
    }

    /**
     * insertData
     * 
     * 写入数据
     */
    public function insertData()
    {
        $insert_sql =<<<EOF
INSERT INTO COMPANY(NAME, AGE, ADDRESS, SALARY) VALUES ('Paual', 20, 'Earth', 20000.00);
INSERT INTO COMPANY(NAME, AGE, ADDRESS, SALARY) VALUES ('Mark', 10, 'Earth', 10000.00);
INSERT INTO COMPANY(NAME, AGE, ADDRESS, SALARY) VALUES ('Sul', 20, 'Earth', 30000.00);
INSERT INTO COMPANY(NAME, AGE, ADDRESS, SALARY) VALUES ('Dael', 20, 'Earth', 90000.00);
EOF;
        $ret = $this->exec($insert_sql);
        if (!$ret) {
            echo "创建表失败: code: " . $db -> lastErrorCode . "msg: " . $db -> lastErrorMsg();
        } else {
            echo "Insert into COMPANY data successfully...\n";
        }
    }

    /**
     * queryData
     * 
     * 查询数据
     */
    public function queryData()
    {
        $query_sql =<<<EOF
SELECT * FROM COMPANY;
EOF;

        $ret = $this->query($query_sql);
        while($row = $ret -> fetchArray(SQLITE3_ASSOC)) {
            echo "ID = " . $row['ID'] . "\n";
            echo "NAME = " . $row['NAME'] . "\n";
            echo "AGE = " . $row['AGE'] . "\n";
            echo "ADDRESS = " . $row['ADDRESS'] . "\n";
            echo "SALARY = " . $row['SALARY'] . "\n";
        }
        echo "Query done successfully...!\n";
    }

    /**
     * updateData
     * 
     * 更新数据
     */
    public function updateData()
    {
        $modify_sql =<<<EOF
UPDATE COMPANY SET SALARY = 99999.00 WHERE ID = 1;
EOF;
        $ret = $this->exec($modify_sql);
        if (!$ret) {
            echo "更新数据失败: code: " . $db -> lastErrorCode . "msg: " . $db -> lastErrorMsg();
        } else {
            echo "更新数据成功\n";
        }
    }

    /**
     * delData
     * 
     * 删除数据
     */
    public function delData() 
    {
        $del_sql = "DELETE FROM COMPANY WHERE ID = 12";
        $ret = $this->exec($del_sql);
        if (!$ret) {
            echo "删除数据失败: code: " . $db -> lastErrorCode . "msg: " . $db -> lastErrorMsg();
        } else {
            echo "删除数据成功\n";
        }
    }


    /**
     * __destruct 析构函数, 程序结束时调用.关闭 db connection 释放资源
     */
    public function __destruct()
    {
        echo "释放资源\n";
        $this->close();
    }

}

$sqlite_class = new SQLiteClass();
$sqlite_class->checkDbOpen();
$sqlite_class->createTable();
$sqlite_class->insertData();
$sqlite_class->updateData();
$sqlite_class->delData();
$sqlite_class->queryData();
?>
