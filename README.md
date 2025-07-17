# ClinicInventorySystem

A simple desktop application for managing clinic medicine inventory, built with Python and Tkinter.

## Features
- Add new medicines with details (name, category, quantity, unit, expiry date)
- View all medicines in a searchable, sortable table
- SQLite database backend for persistent storage
- Simple, user-friendly interface
- Search by medicine name or expiry date
- Expiring drugs calendar with visual alerts

## Screenshots & Demo

**Add Medicine Form – Enter new medicine details including name, quantity, unit, and expiry date.**

*Screenshot: Add Medicine Form*

**Inventory Table – View and search all medicines currently in stock.**

*Screenshot: Inventory Table*

**Expiring Drugs Calendar – See upcoming expiring medicines highlighted on a calendar.**

*Screenshot: Expiring Drugs Calendar*

**System Demo Video – Walkthrough of adding, searching, and tracking medicines in the Clinic Inventory System.**

*Demo video available upon request*

## Requirements
- Python 3.7+
- Tkinter (usually included with Python)
- SQLite3 (included with Python)
- tkcalendar (install with `pip install tkcalendar`)

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Comfortlimata/ClinicInventorySystem.git
   cd ClinicInventorySystem
   ```

2. **(Optional) Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install tkcalendar
   ```

4. **Initialize the database and run the app:**
   ```sh
   python main.py
   ```

## Usage
- **Add Medicine:** Fill in the form and click "Add" to save a new medicine to the inventory.
- **View Inventory:** Click "View Inventory" to see all medicines in a searchable table.
- **Search:** Use the search bar in the inventory window to filter medicines by name or expiry date (YYYY-MM-DD).
- **Expiring Drugs:** Click the "Expiring Drugs button to open a window showing:
  - A calendar with all expiring dates in the next 30 days marked.
  - An advice label showing the next expiring medicine and date.
  - A table listing medicines expiring on the selected date.

## Project Structure
```
ClinicInventorySystem/
├── logic/
│   └── inventory_manager.py      # Database logic for medicines
├── ui/
│   ├── main_window.py           # Main Tkinter UI
│   └── database_setup.py        # Database setup and connection
├── main.py                      # Entry point
├── rural_inventory.db           # SQLite database file (created at runtime)
├── setup_database.py            # (Legacy) Database setup script
├── media/                       # Screenshots and demo videos
└── README.md                    # Project documentation
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is open source and available under the [MIT License](LICENSE).
