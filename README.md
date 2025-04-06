# 🛠️Setup

1. clone the repository
2. setup venv
3. install required pip libraries
4. setup mysql DB as described in [DBSetup](DBSetup.md)
5. set Environment Variables
6. Make sure main.py is started every 24hrs

# ⚙️Configuration

**📑Environment variables:**

- **LOGPATH**: Path to Logfolder

  -> All Logfiles should be in the base folder and not ordered in subfolders

- **DBHOST**: Hostname of the mysql database
- **DBUSER**: Username for the mysql DB User

  -> This user needs select, insert, update, delete privileges as well as the ability to create tables

- **DBPASSWD**: Password for the mysql user
- **DBNAME**: Name of the database

**Logfiles**

```
[<Date(YYYY-mm-dd)|Time(HHMMSS)] [<ERR|WARN|INF>] <Message>
```

**One line of the logfile should be considered one entry**. Entries should not span over multiple lines in the logfile.

The file should always end in **.log**!

The logfile should be named as follows:

\<name of the application\>\_\<YYYYmmddHHMMSS\>.log

Example:

researchtool12_20000720071520.log

```
[2000-07-20|071520] [ERR] Connection timeout
```

# 🍪How the cookie is made

This tool reads all logfiles from the given logpath at the start of every hour. It will extract all entries from the logs and insert them into a mysql database.

From there it will monitor the logs and create reports.

As configured the reports can be created daily, weekly or monthly. Each report will generate a pdf file with a overview of the generated logs in the corrosponding timeframe.

These Reports will be sent through a telegram bot and placed in a configured folder on the system.

If configured, beginning at a specific loglevel alerts can be created and send through a telegram Bot.
