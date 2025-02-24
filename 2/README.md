# Log Archiver

## Description
This script archives logs by compressing them into a `.tar.gz` file and storing them in a specified directory. It helps maintain a clean system by managing old logs efficiently.

## Features
- Accepts a log directory as an argument.
- Compresses logs into a `tar.gz` file.
- Saves the archive with a timestamp.
- Logs the archive process with date and time.

## Usage
Run the script from the command line with the following command:

```bash
log-archive <log-directory>
```

## Example
```bash
log-archive /var/log
```
This will create an archive file named similar to `logs_archive_20240816_100648.tar.gz`.

## Repository
[GitHub Repository](https://github.com/jordimg/server-performance-stats)

## Future Improvements
- Email notifications upon successful archiving.
- Uploading archives to remote storage or cloud services.

https://roadmap.sh/projects/log-archive-tool
