# 🐍 Python + Flask — Day 05

> *"HTML alone is static. Jinja2 makes it alive."* ⚡

Today Flask stopped returning plain strings — and started returning **real HTML pages**, powered by **Jinja2 templates**.

---

## 🗺️ The Big Picture — How It All Connects

```mermaid
flowchart TD
    Browser([🧑 Browser visits /klein]) --> Flask

    Flask["Flask app.py\n@app.route('/<name>')"] --> RT["render_template('index.html')\npasses: hello, name, items"]

    RT --> Jinja["⚙️ Jinja2 Engine\nProcesses the template"]

    Jinja --> Base["base.html\nProvides the layout shell\nnav + footer + block slots"]
    Jinja --> Index["index.html\n{% extends base.html %}\nFills in the block slots"]

    Base --> Merge(["🔀 Merged into\none final HTML page"])
    Index --> Merge

    Merge --> Browser2(["🌐 Browser renders\nthe full page"])

    style Browser fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style Flask fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style RT fill:#1e1e2e,stroke:#f9e2af,color:#cdd6f4
    style Jinja fill:#1e1e2e,stroke:#fab387,color:#cdd6f4
    style Base fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style Index fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style Merge fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style Browser2 fill:#1e1e2e,stroke:#a6e3a1,color:#a6e3a1
```

---

## 📁 Folder Structure

Flask expects your HTML files in a specific folder — always.

```
day-05/
│
├── app.py
└── templates/          ← Flask looks HERE for HTML files
    ├── base.html       ← The parent layout (nav, footer, slots)
    └── index.html      ← The child page (fills the slots)
```

> ⚠️ If the folder isn't named `templates`, Flask won't find your HTML and will throw an error.

---

## 🧩 Concept 1 — `render_template`

Instead of `return "some string"`, you return a full HTML file — and pass Python variables into it.

```python
return render_template("index.html", hello=hello, name=name, items=items)
```

```mermaid
flowchart LR
    A["Python variables\nhello, name, items"] -->|passed into| B["render_template()"]
    B -->|loads| C["templates/index.html"]
    C -->|Jinja2 fills in\nthe placeholders| D(["Final HTML sent\nto the browser"])

    style A fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style B fill:#1e1e2e,stroke:#f9e2af,color:#cdd6f4
    style C fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style D fill:#1e1e2e,stroke:#a6e3a1,color:#a6e3a1
```

---

## 🧩 Concept 2 — `{{ }}` Placeholders

The double curly braces are Jinja2's way of saying *"put a Python value here."*

| In Python | In HTML Template | Result in Browser |
|---|---|---|
| `hello = "Welcome to Flask!"` | `{{ hello }}` | Welcome to Flask! |
| `name = "klein"` | `{{ name }}` | klein |
| `"flask"` + filter | `{{ item \| upper }}` | FLASK |

---

## 🧩 Concept 3 — Loops in Jinja2

You have a Python list — Jinja2 lets you loop through it **inside HTML**.

```python
# Python
items = ["Flask", "Jinja2", "Rendering Templates"]
```

```html
<!-- HTML Template -->
{% for item in items %}
    {{ item | upper }}
{% endfor %}
```

```mermaid
flowchart TD
    A(["items = Flask, Jinja2, Rendering Templates"]) --> B["{% for item in items %}"]
    B --> C["Iteration 1: item = 'Flask'\n{{ item | upper }} → FLASK"]
    B --> D["Iteration 2: item = 'Jinja2'\n{{ item | upper }} → JINJA2"]
    B --> E["Iteration 3: item = 'Rendering Templates'\n{{ item | upper }} → RENDERING TEMPLATES"]
    C --> F["{% endfor %}"]
    D --> F
    E --> F

    style A fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style B fill:#1e1e2e,stroke:#f9e2af,color:#cdd6f4
    style C fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style D fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style E fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style F fill:#1e1e2e,stroke:#fab387,color:#cdd6f4
```

---

## 🧩 Concept 4 — Filters `|`

Filters modify a value using the pipe `|` symbol — no Python code needed inside HTML.

```html
{{ item | upper }}        → FLASK
{{ item | lower }}        → flask
{{ item | capitalize }}   → Flask
{{ item | reverse }}      → ksalF
{{ name | length }}       → 5
```

> 💡 You can even chain them: `{{ name | upper | reverse }}`

---

## 🧩 Concept 5 — Template Inheritance (`extends`)

The most powerful idea today. One `base.html` holds the shared layout. Child pages just fill in the gaps.

```mermaid
flowchart TD
    subgraph BASE["🏗️ base.html — The Parent"]
        B1["&lt;nav&gt; Home | About &lt;/nav&gt;"]
        B2["{% block content %}\n--- EMPTY SLOT ---\n{% endblock %}"]
        B3["&lt;footer&gt;© 2026&lt;/footer&gt;"]
    end

    subgraph CHILD["📄 index.html — The Child"]
        C1["{% extends 'base.html' %}"]
        C2["{% block content %}\n&lt;h1&gt;{{hello}} {{name}}&lt;/h1&gt;\n{% endblock %}"]
    end

    C1 -->|inherits from| BASE
    C2 -->|fills the slot in| B2

    style BASE fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style CHILD fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
```

**Without inheritance** → you copy-paste `<nav>` and `<footer>` on every page. Change nav once? Update 10 files. 😭

**With inheritance** → change `base.html` once. Every page updates automatically. 🎉

---

## 🔄 Full Request Flow — Step by Step

```mermaid
sequenceDiagram
    actor User
    participant Flask as Flask (app.py)
    participant Jinja as Jinja2 Engine
    participant Base as base.html
    participant Index as index.html

    User->>Flask: GET /klein
    Flask->>Flask: home(name="klein") is called
    Flask->>Flask: builds: hello, name, items
    Flask->>Jinja: render_template("index.html", ...)
    Jinja->>Index: loads index.html
    Index->>Base: {% extends "base.html" %}
    Jinja->>Base: loads base.html shell
    Jinja->>Jinja: merges block content into base slot
    Jinja->>Jinja: fills {{ hello }}, {{ name }}, loops items
    Jinja->>Flask: returns complete HTML string
    Flask->>User: sends final HTML to browser
```

---

## 🧠 Jinja2 Syntax Cheat Sheet

| Syntax | Purpose | Example |
|---|---|---|
| `{{ }}` | Output a value | `{{ name }}` |
| `{% %}` | Logic / statements | `{% for %}` `{% if %}` |
| `{# #}` | Comments (hidden from browser) | `{# TODO: fix this #}` |
| `\|` | Apply a filter | `{{ name \| upper }}` |
| `{% extends %}` | Inherit a parent template | `{% extends "base.html" %}` |
| `{% block %}` | Define a fillable slot | `{% block content %}` |
| `{% endblock %}` | Close a block | `{% endblock %}` |
| `{% for %}` | Start a loop | `{% for item in items %}` |
| `{% endfor %}` | End a loop | `{% endfor %}` |

---

## 🚀 Getting Started

```bash
# Make sure your folder structure is right first!
# day-05/
# ├── app.py
# └── templates/
#     ├── base.html
#     └── index.html

python app.py

# Then visit:
# http://localhost:5000/yourname   → renders index.html with your name
# http://localhost:5000/about      → redirects to /klein
```

---

## ✅ Day 05 Checklist

- [x] Used `render_template` instead of returning plain strings
- [x] Passed Python variables into HTML with `{{ }}`
- [x] Used `{% for %}` loop inside a Jinja2 template
- [x] Applied a filter with `| upper`
- [x] Created `base.html` as a parent layout
- [x] Used `{% extends %}` and `{% block %}` for template inheritance
- [ ] Try an `{% if %}` statement inside a template
- [ ] Add a `{% block title %}` to give each page a unique browser tab title
- [ ] Create a second child page that also extends `base.html`

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
           : url_for, converters, method ✅
    Day 05 : Jinja2 Templates ✅
           : render_template, loops, filters, extends ✅
    Day 06 : Static Files & HTML Forms
    Day 07 : SQL & SQLite Basics
```

---

<div align="center">

*Built with curiosity on Day 05 of learning Python + Flask* 🐍

</div>