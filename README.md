# Address Book

A modern, feature-rich desktop address book application built with Python and PySide6. Manage your contacts with an intuitive and beautiful interface.

![Address Book](https://img.shields.io/badge/Version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **📝 Contact Management** - Add, edit, and delete contacts with ease
- **🔍 Quick Access** - Clickable contact cards for instant access
- **📊 Organized Layout** - Clean form-based interface with contact list sidebar
- **💾 Persistent Storage** - SQLite database for reliable data storage
- **🎨 Modern UI** - Beautiful purple-themed interface with smooth animations
- **✅ Data Validation** - Comprehensive input validation with helpful error messages
- **📱 Responsive Design** - Adapts to different screen sizes

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/address-book.git
   cd address-book
   ```

2. **Install the application**
   ```bash
   pip install -e .
   ```

3. **Run the application**
   ```bash
   address-book
   ```
   Or alternatively:
   ```bash
   python main.py
   ```

### Development Installation

For contributing to the project:

```bash
git clone https://github.com/yourusername/address-book.git
cd address-book
pip install -e ".[dev]"
```

## 📖 Usage

### Adding a Contact

1. Fill in the contact form on the left side
2. **Required fields:**
   - First Name
   - At least one phone number (Cell or Home)
3. **Optional fields:**
   - Last Name, Email, Birthday, Address details
4. Click "Save" to store the contact

### Editing a Contact

1. Click on any contact card in the right sidebar
2. The form will populate with the contact's information
3. Make your changes
4. Click "Update" to save changes

### Deleting a Contact

1. Select a contact by clicking on its card
2. Click the "Delete" button
3. Confirm the deletion

### Form Validation

The application includes comprehensive validation:

- **First Name**: Required field
- **Phone Numbers**: At least one required (Cell or Home)
- **Email**: Valid format required if provided
- **State**: 2-letter abbreviation if provided
- **Postal Code**: 5 digits if provided

## 🗂️ Project Structure

```
address-book/
├── app/
│   ├── __init__.py
│   ├── app.py                 # Main application window
│   ├── models/
│   │   ├── __init__.py
│   │   └── contact.py         # Pydantic models for contacts
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py              # Database engine and operations
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py     # Auto-generated UI code
│   │   └── components/
│   │       ├── __init__.py
│   │       └── clickable_card.py  # Custom contact card widget
│   ├── validators/
│   │   ├── __init__.py
│   │   └── contact.py         # Contact data validation
│   ├── services/
│   │   ├── __init__.py
│   │   └── contact_service.py # Business logic layer
│   └── assets/
│       └── styles.qss         # Application styling
├── main.py                    # Application entry point
├── pyproject.toml            # Project configuration and dependencies
└── README.md
```

## 🔧 Technical Details

### Architecture

The application follows a modular architecture:

- **Models**: Data structures using Pydantic
- **Services**: Business logic layer
- **UI**: Presentation layer with PySide6
- **Database**: SQLite persistence layer
- **Validators**: Input validation logic

### Dependencies

- **PySide6**: Qt-based GUI framework
- **Pydantic**: Data validation and settings management
- **SQLite**: Built-in database engine

### Data Storage

Contacts are stored in a SQLite database located at:
```
app/data/contacts.db
```

The database is automatically created on first run.

## 🎨 Customization

### Styling

The application uses Qt Style Sheets (QSS) for styling. Modify `app/assets/styles.qss` to change the appearance:

```css
QMainWindow {
  background-color: #540863;
  /* Add your custom styles here */
}
```

### Adding New Fields

To add new contact fields:

1. Update the database schema in `app/database/db.py`
2. Modify the Pydantic models in `app/models/contact.py`
3. Add UI elements in the form
4. Update validation rules in `app/validators/contact.py`

## 🐛 Troubleshooting

### Common Issues

**Application won't start:**
- Ensure Python 3.8+ is installed
- Check all dependencies are installed: `pip install -e .`

**Database errors:**
- Delete the `app/data/` folder to reset the database
- Check file permissions in the application directory

**UI looks broken:**
- Verify the styles.qss file exists in `app/assets/`
- Check for console error messages

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run code formatter
black .

# Run linting
flake8

# Run type checking
mypy .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [PySide6](https://www.qt.io/qt-for-python) - Qt for Python
- Icons and design inspired by modern desktop applications
- Thanks to all contributors who help improve this project

## 📞 Support

If you encounter any problems or have questions:

1. Check the [Issues](https://github.com/yourusername/address-book/issues) page
2. Create a new issue with detailed information
3. Provide steps to reproduce any bugs

---

**Enjoy organizing your contacts with Address Book!** 📇✨