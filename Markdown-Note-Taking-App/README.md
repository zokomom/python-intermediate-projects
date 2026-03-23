# 📝 Markdown Notes API

A backend API to create, store, and render Markdown notes with basic grammar checking and secure HTML output.

---

## 🚀 What it does

* Create and store notes in Markdown
* Render Markdown → HTML
* Upload `.md` files as notes
* Check spelling mistakes in notes
* List notes with pagination

---

## ⚙️ API Endpoints

### ➤ Create Note

`POST /notes`

```json
{
  "title": "Sample Note",
  "markdown_content": "# Hello\n\nThis is a note"
}
```

---

### ➤ Get Notes

`GET /notes?skip=0&limit=10`

---

### ➤ Render HTML

`GET /notes/{note_id}/html`

Returns sanitized HTML.

---

### ➤ Upload Markdown File

`POST /notes/upload-markdown`

Upload a `.md` file → saved as a note.

---

### ➤ Grammar Check

`POST /grammar-check`

```json
{
  "title": "Test",
  "markdown_content": "Ths is wrng text"
}
```

---

## 🧠 Tech Used

* FastAPI
* PostgreSQL
* SQLAlchemy
* Markdown
* Bleach
* PySpellChecker

---

## ⚠️ Notes

* HTML output is sanitized to prevent XSS
* Only `.md` files are accepted for upload
* Grammar check is basic (spell-based)

---

## 💡 Why this project

Built to practice:

* REST API design
* File handling
* Markdown processing
* Backend security basics

---

## Acknowledgements
[https://roadmap.sh/projects/markdown-note-taking-app]