learning Python ....

```xml
<?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<mycat:schema xmlns:mycat="http://org.opencloudb/">

        <schema name="VDB" checkSQLschema="false" sqlMaxLimit="100" dataNode="dn1">
        </schema>

        <dataNode name="dn1" dataHost="localhost1" database="zabbix" />

        <dataHost name="localhost1" maxCon="1000" minCon="10" balance="1"
                writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">

                <heartbeat>select user()</heartbeat>
                <!-- can have multi write hosts -->
                <writeHost host="node1" url="node1:3306" user="relay"  password="xxxxx">
                        <!-- can have multi read hosts -->
                        <readHost host="node2" url="node2:3306" user="relay" password="xxxxx" />
                </writeHost>
        </dataHost>

</mycat:schema>

```
