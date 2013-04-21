# mega-client

mega-client is a sysadmin friendly command line interface to mega.co.nz api.
It's goal is to provide simple interface for other programs to run against. It
is a simple wrapper around [mega.py](https://github.com/richardasaurus/mega.py)
library.

## Usage

Sample usage:

### Help

```
mega-client -h
```

### Upload files
```
mega-client --action 'upload' --login test@example.com --password secret file1 file2 ...
```

### Download files

```
mega-client --action 'download' --login test@example.com --password secret file1 file2 ...
```

### Get list of files
```
mega-client --action 'ls' --login test@example.com --password secret
```

### Remove files
```
mega-client --action 'rm' --login test@example.com --password secret file1 file2
```
