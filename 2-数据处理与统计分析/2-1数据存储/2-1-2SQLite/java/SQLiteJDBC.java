import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * javac SQLiteJDBC.java
 * java -classpath ".;sqlite-jdbc-3.53.1.0.jar" SQLiteJDBC # in Windows
 * java -classpath ".:sqlite-jdbc-3.53.1.0.jar" SQLiteJDBC # in macOS or Linux
 */
public class SQLiteJDBC {

    public static void main(String[] args) {

        try (
                Connection connection  = DriverManager.getConnection("jdbc:sqlite:test.db");
                Statement statement = connection.createStatement();
            )
        {
            
            {
                statement.setQueryTimeout(30); // set timeout
                System.out.println("Opend database successfully...");

                String create_stmt = "CREATE TABLE IF NOT EXISTS COMPANY(" +
                "ID INTEGER PRIMARY KEY AUTOINCREMENT," + 
                "NAME TEXT NOT NULL," +
                "AGE INT NOT NULL," +
                "ADDRESS CHAR(50)," + 
                "SALARY REAL);";
                statement.executeUpdate(create_stmt);
                System.out.println("数据表创建成功...");

                String insert_stmt = "INSERT INTO COMPANY (NAME, AGE, ADDRESS, SALARY) VALUES ('Paul', 20, 'NewYork', 20000.00)";
                statement.executeUpdate(insert_stmt);
                System.out.println("数据写入成功..."); 

                String update_stmt = "UPDATE COMPANY SET SALARY = 9999.00 WHERE ID = 1";
                statement.executeUpdate(update_stmt);
                System.out.println("数据更新成功...");

                String del_stmt = "DELETE FROM COMPANY WHERE ID = 3";
                statement.executeUpdate(del_stmt);
                System.out.println("数据删除成功...");

                ResultSet ret = statement.executeQuery("SELECT * FROM COMPANY");
                while(ret.next()) {
                    System.out.println("ID = " + ret.getInt("ID"));
                    System.out.println("NAME = " + ret.getString("NAME"));
                    System.out.println("AGE = " + ret.getString("AGE"));
                    System.out.println("ADDRESS = " + ret.getString("ADDRESS"));
                    System.out.println("SALARY = " + ret.getString("SALARY"));
                }

                // connection.commit();
                statement.close();
                connection.close();
            }
           
        } catch ( SQLException e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
            e.printStackTrace(System.err);
            System.exit(0);
        }
    }
}
