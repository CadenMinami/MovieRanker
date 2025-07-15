#  Movie Ranker CLI App

A command-line application that lets you build and manage your personal ranked list of favorite movies. When a new movie is added, it gets inserted into the correct spot based on its ranking — and all existing rankings shift accordingly.

---

##  Features

- Add a new movie with a rank (1 being best)
- Automatically shifts lower-ranked movies down
- Prevents duplicate movie entries
- View the full ranked movie list
- Delete movies from the list
- Persistent storage using JSON
- File safety with the `os` module

---

##  Concepts Practiced

- Python data structures (`list`, `dict`)
- File storage using `json` for persistence
- Path and file safety with `os.path.exists()`
- Data validation and rank ordering


---

## 🛠 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/movie-ranker-cli.git
   cd movie-ranker-cli
