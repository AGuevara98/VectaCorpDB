# VectaCorpDB

Streamlit CRUD application for managing VectaCorp help desk employees backed by a SQLite database.

## How to run

```powershell
cd "...\VectaCorpDB\src"
& "...\VectaCorpDB\.venv\Scripts\python.exe" -m streamlit run app_visualize.py
```

Then open http://localhost:8501 in your browser.

## Features

The app supports all four CRUD operations on the employees table via a dropdown menu:

- **View** – displays all employees in a table with role names resolved from the roles table.
- **Add** – form to create a new employee (name, email, role, username, password).
- **Delete** – two-step flow: look up an employee by ID to preview their info, then confirm deletion.
- **Update** – two-step flow: look up an employee by ID to pre-populate an edit form, then save changes.

## Changes made

### `src/app_visualize.py` — completed CRUD UI

- **Delete section**: replaced a two-submit-button form (which doesn't work in Streamlit) with a plain button that stores the fetched employee in `st.session_state`, followed by a separate confirm-delete button. This preserves employee data across rerenders.
- **Update section**: same `st.session_state` pattern so the edit form is pre-populated with the employee's current data when shown. Previously the fields always rendered empty.
- **`update_employee_db` function**: fixed a bug where the body referenced `roleid` (an undeclared variable) instead of the `role` parameter. The function now calls `db.get_roleid_from_role(role)` to resolve the role name, matching the same pattern used in `add_employee`.
- Added success messages after Add, Delete, and Update operations.

### `src/db.py` — SQLite threading fix

- Added `check_same_thread=False` to `sqlite3.connect(...)`. Streamlit reruns the script across different threads, which caused a `sqlite3.ProgrammingError` when any DB operation was triggered after the initial page load.
