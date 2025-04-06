# Tables

The tables Apps and Logtypes will be filled with the necissary information automatically. Using the setup script they can be filled with initialized with values. Alternatively you can set them up manually. Beware, that the 'name' fields must be identical to the corrosponding names of the application in the name of the logfile and the error code.

The application will modify the database as needed with new versions. Old Logs values will be migrated. Updates regarding the data model will always be backwards compatible even when implementing new features to ensure, that all data can be migrated safely.

## Apps

```SQL
create table apps (
    appID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name char(50) Not Null,
    description char(100),
    state char(4)
)
```

For more information in the reporting the fields **description** and **state** can be used. This is **optional** and will only be used in the reporting and alerting.

### States

- TEST: Applications used for testing reasons
- PROD: Application used in production

## Logtypes

```SQL
create table logtypes (
    typeID int Primary Key Not Null AUTO_INCREMENT,
    typeName char(10) Not Null,
    typeDescription char(100)
)
```

The field **typeDescription** is **optional** and is only used in the reporting and alerting.

## Logs

```SQL
create table logs (
    logtime timestamp Not Null,
    appID int Not Null,
    typeID int Not Null,
    message varchar(255),
    PRIMARY KEY (logtime, appID),
    FOREIGN KEY (appID) REFERENCES apps(appID),
    FOREIGN KEY (typeID) REFERENCES logtypes(typeID))
```

# User Setup

A user mus be setup with the correct privileges to operate the database. This will set up a user with the least amount of priviliges necessary to run this application. You can also use a User with more privileges. It is generally recommended to give out only necessary grants to users for security porpuses.

Create Role Logmanager to avoid user specific privileges. This way the privileges can be shared through this role.

```SQL
CREATE ROLE 'logmanager'
```

Create the User used by the logmanager. Store the password savely. Further configurations like TLS or password expiration can be added.

```SQL
CREATE USER logman IDENTIFIED BY <password> DEFAULT ROLE logmanager
```

Grant the necissary privileges to the **Role** not the user. To ensure, that these privileges can be shared to multiple users.

```SQL
GRANT create, drop, select, insert, update, delete ON logtest TO logmanager
```
