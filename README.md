# Discord Library Bot

A Discord bot that manages a simple library system.  
Users can borrow and return books directly through Discord commands.  
The bot also reminds users about due dates.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/iwodud/discord-library-bot.git
cd discord-library-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the database

```bash
python3 tools/init_db.py
```

### 4. (Optional) Add example data

```bash
python3 tools/example_data.py
```

### 5. Run the bot

```bash
python3 bot/main.py
```

---

## Project Structure

```
discord-library-bot/
├── bot/                    # Bot logic: commands, reminders, main entry point
│   ├── bot_commands.py         # Command handlers for interacting with users
│   ├── reminders.py        # Logic for sending return reminders
│   └── main.py             # Entry point to run the bot
│
├── database/               # Database access logic (functions used by the bot)
│   └── db.py               # Functions to interact with the SQLite database
│
├── tools/                  # One-time scripts: schema, database init, test data
│   ├── schema.sql          # SQL script defining the database schema
│   ├── init_db.py          # Script to initialize database structure
│   └── example_data.py     # Optional script to insert example records
│
├── library.db              # Local SQLite database (gitignored)
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (e.g., Discord bot token)
└── README.md               # Project documentation (this file)

```

---

## Technologies Used

- Python 3.x
- discord.py
- SQLite (as a local development database)

---

## Features (in progress)

- [x] SQLite database structure
- [x] Database initialization script
- [x] Script for adding example data
- [x] SQL: add_book
- [ ] command: add_book (admin)
- [x] Command: show_all_books
- [ ] Command: delete a book (admin)
- [ ] Command: borrow a book (user)
- [ ] Command: return a book (user)
- [ ] Reminder system for due dates

---

## Notes

- `library.db` is not committed to the repository. Each developer creates their own local version using tools/init_db.py.
- In the future, the project may migrate to a production-grade database like MySQL.
- Scripts in tools/ are meant to be run manually once during development and should not be part of normal bot execution.
