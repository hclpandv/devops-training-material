## Understanding cron

> Cron is a UNIX, Solaris utility that allows tasks to be automatically run in the background at regular intervals by the cron daemon. These tasks are often termed as cron jobs in UNIX, Solaris. Crontab (CRON Table) is a file which contains the schedule of cron entries to be run and at specified times.

#### Restrictions

You can execute crontab if your name appears in the file /usr/lib/cron/cron.allow.

If that file does not exist, you can use crontab if your name does not appear in the file /usr/lib/cron/cron.deny.
If only cron.deny exists and is empty, all users can use crontab. 
If neither file exists, only the root user can use crontab. The allow/deny files consist of one user name per line.

#### Command

| Command             | Description                                   |
|---------------------|-----------------------------------------------|
| `export EDITOR=vi`  | To Edit the crontab in VI                     |
| `crontab -e`        | Edit crontab file, or create new              |
| `crontab -l`        | Display crontab file                          |
| `crontab -r`        | Remove crontab file                           |
| `crontab -v`        | Display the last time you edited your crontab |
