# 🐍 Python + Flask — Day 04

> *"You're not just running a server anymore — you're building roads."* 🛣️

Today is all about **Routing** — how Flask listens to different URLs and knows exactly what to do with each one.

---

## 🗺️ All Routes at a Glance

```mermaid
flowchart TD
    Browser([🧑 Browser Request]) --> Router{Flask Router}

    Router -->|GET /| A["index()\n→ 'Welcome to Flask!'"]
    Router -->|GET or POST /about| B["about()\n→ 'Welcome to About'"]
    Router -->|GET /user/john| C["user(name='john')\n→ 'Hi john'"]
    Router -->|GET /post/42| D["post(number=42)\n→ 'The value you input is 42'"]
    Router -->|GET /step4| E["step4()\n→ redirect → /about"]
    Router -->|anything else| F["❌ 404 Not Found"]

    E --> B

    style Browser fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style Router fill:#1e1e2e,stroke:#f9e2af,color:#cdd6f4
    style A fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style B fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style C fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style D fill:#1e1e2e,stroke:#fab387,color:#cdd6f4
    style E fill:#1e1e2e,stroke:#f9e2af,color:#cdd6f4
    style F fill:#1e1e2e,stroke:#f38ba8,color:#f38ba8
```

---

## 📖 The 4 Steps — Broken Down

### ✅ Step 1 — Multiple Routes

One app, many routes. Each `@app.route()` is a separate door into your app.

```python
@app.route("/about", methods=["GET", "POST"])
def about():
    return "Welcome to About"
```

```mermaid
flowchart LR
    A([Visit /about]) --> B["Flask matches @app.route('/about')"]
    B --> C["Calls about()"]
    C --> D(["Returns: 'Welcome to About'"])

    style A fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style B fill:#1e1e2e,stroke:#f9e2af,color:#cdd6f4
    style C fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style D fill:#1e1e2e,stroke:#a6e3a1,color:#a6e3a1
```

---

### ✅ Step 2 — Dynamic String Route `<name>`

The URL itself carries the data. No need to hardcode names.

```python
@app.route("/user/<name>")
def user(name):
    return f"Hi {name}"
```

```mermaid
flowchart LR
    A(["/user/maria"]) --> B["Flask extracts 'maria'\nfrom the URL"]
    B --> C["Passes it as name='maria'\nto user()"]
    C --> D(["Returns: 'Hi maria'"])

    style A fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style B fill:#1e1e2e,stroke:#f9e2af,color:#cdd6f4
    style C fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style D fill:#1e1e2e,stroke:#a6e3a1,color:#a6e3a1
```

> 💡 Try visiting `/user/yourname` — it works for *any* name!

---

### ✅ Step 3 — Int Converter `<int:number>`

Same idea as Step 2, but Flask enforces the type. Visiting `/post/hello` gives a **404** — Flask protects you automatically.

```python
@app.route("/post/<int:number>")
def post(number):
    return f"The value you input is {number}"
```

```mermaid
flowchart TD
    A([Visit /post/...]) --> B{Is the value\na whole number?}
    B -->|Yes e.g. /post/42| C["Flask passes number=42\nto post()"]
    B -->|No e.g. /post/hello| D["❌ 404 — Flask rejects it\nbefore your function even runs"]
    C --> E(["Returns: 'The value you input is 42'"])

    style A fill:#1e1e2e,stroke:#fab387,color:#cdd6f4
    style B fill:#1e1e2e,stroke:#f9e2af,color:#cdd6f4
    style C fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style D fill:#1e1e2e,stroke:#f38ba8,color:#f38ba8
    style E fill:#1e1e2e,stroke:#a6e3a1,color:#a6e3a1
```

---

### ✅ Step 4 — `url_for` + `redirect`

Instead of hardcoding `/about`, you ask Flask to *generate* the URL for you. Then `redirect` sends the user there.

```python
@app.route("/step4")
def step4():
    return redirect(url_for("about"))
```

```mermaid
sequenceDiagram
    actor User
    participant Flask
    participant step4
    participant about

    User->>Flask: GET /step4
    Flask->>step4: calls step4()
    step4->>step4: url_for("about") → "/about"
    step4->>User: 302 Redirect → /about
    User->>Flask: GET /about
    Flask->>about: calls about()
    about->>User: "Welcome to About"
```

> 🔑 **Key difference:**
> - `url_for("about")` → produces the string `"/about"`
> - `redirect(...)` → sends the browser *to* that URL

---

## 🧠 URL Converters Cheat Sheet

| Converter | Syntax | Accepts | Example URL |
|---|---|---|---|
| *(default)* | `<name>` | Any text | `/user/john` |
| int | `<int:number>` | Whole numbers only | `/post/42` |
| float | `<float:value>` | Decimal numbers | `/price/9.99` |
| path | `<path:subpath>` | Text including `/` | `/files/a/b/c` |

---

## 🔄 GET vs POST — What's the Difference?

```mermaid
flowchart LR
    subgraph GET["📬 GET"]
        G1["Fetching data\nfrom the server"]
        G2["URL carries the info\ne.g. /search?q=flask"]
        G3["Safe to refresh\nthe page"]
    end

    subgraph POST["📮 POST"]
        P1["Sending data\nto the server"]
        P2["Data goes in\nthe request body"]
        P3["Used for forms,\nlogins, submissions"]
    end

    style GET fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style POST fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
```

Your `/about` route accepts **both** — that's what `methods=["GET", "POST"]` means.

---

## 🚀 Getting Started

```bash
# Install Flask (if not done already)
pip install flask

# Run the app
python app.py

# Then visit any of these:
# http://localhost:5000/
# http://localhost:5000/about
# http://localhost:5000/user/yourname
# http://localhost:5000/post/42
# http://localhost:5000/step4
```

---

## 📂 Project Structure

```
day-04/
│
├── app.py        ← All routes live here
└── README.md     ← You are here 👋
```

---

## ✅ Day 04 Checklist

- [x] Added a second route `/about`
- [x] Used `methods=["GET", "POST"]`
- [x] Created a dynamic string route `/user/<name>`
- [x] Used the `<int:number>` converter
- [x] Used `url_for` to generate URLs
- [x] Used `redirect` to send users to another route
- [ ] Try `<float:value>` converter
- [ ] Make `/user/<name>` return HTML instead of plain text
- [ ] Build a route that uses `url_for` to link to `/user/<name>`

---

## 🗓️ The Learning Journey

```mermaid
timeline
    title Python + Flask Learning Path
    Day 01 : Python fundamentals ✅
           : functions, module ✅
    Day 02 : OOP & Data Structures ✅
           : classes & lists ✅
    Day 03 : Flask install ✅
           : First web app ✅
           : flask install & debug mode ✅
    Day 04 : Routing & URL Rules ✅
           : url_for, converters,method ✅
    Day 05 : Jinja2 Templates
    Day 06 : Static Files & HTML Forms
    Day 07 : SQL & SQLite Basics
```

---

<div align="center">

*Built with curiosity on Day 04 of learning Python + Flask* 🐍

</div>