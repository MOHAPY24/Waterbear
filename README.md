

# Waterbear

A lightweight, secure JSON-based database client with password protection and snapshot capabilities.

## Overview

Waterbear is a simple yet powerful Python database library that stores data in JSON format with built-in security features. It's designed for applications that need persistent storage with basic access control and data recovery options.

## Features

- 🔐 **Password Protection** - Secure your database with integer passwords
- 💾 **JSON-Based Storage** - Human-readable data format
- 📸 **Auto-Snapshotting** - Automatic backup before modifications
- 🔄 **Data Recovery** - Restore from snapshots if needed
- 🛡️ **Safe Deletion** - Multiple deletion modes with confirmation
- ⚡ **Lightweight** - Minimal dependencies and overhead

## Installation

```bash
# Clone the repository
git clone https://github.com/MOHAPY24/Waterbear.git
cd Waterbear

# No additional dependencies required beyond Python standard library
```

## Quick Start

```python
import db

# Initialize database with password
database = db.Waterbear(1234, "my_database.json", autosnapshot=True)

# Store data
database.Update_Key("username", "john_doe", 1234)
database.Update_Key("email", "john@example.com", 1234)

# Retrieve data
print(database.Get_Value("username"))  # Output: john_doe

# Get all data
print(database.Get_All())

# Close and save database
database.Close(1234)
```

## API Reference

### Initialization
```python
Waterbear(dbpassword, dbfilename="waterbear_db1.json", autosnapshot=True)
```

### Core Methods
- `Get_Value(key)` - Retrieve value by key
- `Update_Key(key, value, dbpass)` - Update or create key-value pair
- `Delete_Key(key, dbpass)` - Remove specific key
- `Get_All()` - Get all data as dictionary
- `Close(dbpass)` - Save and close database

### Security & Maintenance
- `Reset_Db_Password(old_pass, new_pass)` - Change database password
- `Snapshot()` - Manual snapshot creation
- `PushSnapshot(dbpass)` - Restore from snapshot
- `Delete(dbpass)` - Clear database (preserves snapshot)
- `DeleteNoPreserve(dbpass)` - Clear database and snapshot

## File Structure

```
waterbear/
├── db.py          # Main database class
├── errors.py      # Custom exceptions
├── wb.py          # Example usage
└── README.md      # This file
```

## Security Notes

- Passwords are simple integers (not suitable for high-security applications)
- Snapshots provide basic versioning and recovery
- All modifications require password verification
- Data is persisted only when explicitly saved or closed

## Error Handling

Waterbear raises custom exceptions:
```python
try:
    database.Update_Key("key", "value", wrong_password)
except errors.PasswordInvalid:
    print("Access denied - invalid password")
```

## Example Use Cases

- Configuration storage
- Small-scale application data
- Prototype development
- Educational projects
- IoT device configuration

## Limitations

- Integer-only passwords
- Single-file storage (not suitable for large datasets)
- Basic concurrency handling
- No advanced query capabilities

## License

BSD 3 Clause

---

Waterbear is perfect for small to medium projects that need simple, secure JSON storage without complex database setup.
