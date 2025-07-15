🏥 Clinic Inventory System

The **Clinic Inventory System** is a lightweight, standalone desktop application built with Python for tracking and managing medication stock in rural health clinics. Designed to operate without an internet connection or external database, this system provides a simple and effective solution for managing medicine inventory in low-resource settings like rural Zambia

## ✅ Features

- 🩺 **Add Medication** — Input medicine name, quantity, unit (e.g., tablets, bottles), and expiry date  
- 📋 **View Inventory** — Display a list of all medicines currently in stock  
- 💾 **Auto-Save Locally** — Data is saved automatically to a local file (`rural_inventory.json`)  
- ❌ **No Database Required** — Ideal for offline use in clinics with limited infrastructure  
- 🖥️ **User-Friendly GUI** — Built with Python’s Tkinter for easy navigation  
- 📦 **Packaged as `.exe`** — Runs on any Windows computer without Python installed 

## 💡 Use Case

This system was developed to help health workers in rural clinics manage inventory reliably and easily, without needing a stable internet connection or technical expertise.

---

## 🛠 Technologies Used

| Component        | Tool/Language     |
|------------------|-------------------|
| Programming      | Python 3.x        |
| GUI              | Tkinter           |
| Data Storage     | JSON (File-based) |
| Executable Build | PyInstaller       |

---

## 🗂 Folder Structure

ClinicInventorySystem/
├── main.py # Application entry point
├── ui/
│ └── main_window.py # GUI layout and logic
├── logic/
│ └── inventory_manager.py # Save/load functions
├── dist/
│ └── main.exe # Standalone executable
├── rural_inventory.json # Data file (created on first run)

yaml
Copy
Edit

---

## 💻 How to Use

### ▶️ Option 1: Run with Python (Development)

1. Clone the repository:
   ```bash
   git clone https://github.com/comfortlimata/ClinicInventorySystem.git
   cd ClinicInventorySystem
Run the app:

bash
Copy
Edit
python main.py
🟦 Option 2: Run the .exe Without Python
Go to the Releases

Download the latest .zip file

Extract it and open the folder

Double-click main.exe to launch the app

rural_inventory.json will be created automatically to store your inventory data

🧪 Sample Entry
Medicine Name	Quantity	Unit	Expiry Date
Paracetamol	100	Tablets	2025-08-01
Amoxicillin	50	Bottles	2024-12-10

🔐 Data Handling
Stores all medicine records in rural_inventory.json

No external database or internet required

Safe for offline, rural environments

📌 Future Enhancements
Medicine search/filter

Expiry date alerts

Printable or exportable inventory reports

Login system for staff tracking

Cloud backup integration (optional for internet-enabled clinics)

🙋 Author
Comfort Limata
Student – Information Systems and Technology
📍 Zambia
📧 Email: comfortlimata@gmail.com
🌐 GitHub: github.com/comfortlimata

📝 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software for educational and non-commercial purposes
 
