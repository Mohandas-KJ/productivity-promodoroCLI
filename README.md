# **🚀 Pomodoro CLI**
A Micro-Task–Driven Productivity Timer for Focused Execution

## Overview
Pomodoro CLI is a modular, command-line productivity tool designed to execute work in micro-task blocks using timed focus sessions.
Inspired by high-performance work principles (including time-boxing and micro-execution strategies), this tool helps users break work into small, executable units and complete them sequentially with discipline.

Unlike traditional Pomodoro timers, Pomodoro emphasizes:

- Task execution over time tracking
- Micro-task scheduling
- Sequential focus
- Minimal distractions
- CLI-first workflow

## ✨ Features
- ⏱️ Micro-Task Timer
    - Assign a fixed time per task
    - Tasks execute one after another automatically
- 🔄 Sequential Task Execution
    - Tasks are processed in order
    - Optional delay between tasks
- 🌀 Live Spinner Timer
    - Animated spinner with real-time countdown
    - Single-line terminal updates (no clutter)
- 🔔 Audio Alerts
    - Start & end alerts for each task
    - Cross-platform fallback support
- 📊 Time Tracking
    - Calculates total focus time
    - Human-readable output (hours/minutes)
- 🧱 Modular Architecture
    - Clear separation of responsibilities
    - Easy to extend or modify

## 🧠 Design Philosophy
- Execution beats planning
- Small tasks reduce resistance
- Timers enforce discipline
- CLI keeps focus sharp
- Learning by building > learning by reading

## My Learning
I create projects that makes one programming concept fit in a Big Picture. Like that, In this project I learned the following:
1. Modular Programming
2. Threading in Python
3. Terminal Control (CLI)
4. About Timers in Python

**This project may not be large in scope, but it focuses on understanding how individual libraries and concepts fit into a larger system.**

## 📁 Project Structure
``` 
productivity-promodoroCLI/
├── .gitignore
├── README.md
├── run.py
├── pyenv.cfg
│
├── src/
│   ├── __init__.py
│   ├── pomodoro.py
│   │
│   └── productivity/
│       ├── __init__.py
│       │
│       ├── commons/
│       │   ├── __init__.py
│       │   ├── spinner_timer.py
│       │   └── time_sheet.py
│       │
│       └── time_blocking/
│           ├── __init__.py
│           ├── micro_tasker.py
│           └── mt_timer.py
│
└── test/
```

- `run.py` -> entry point (recommended way to run)
- `pomodoro.py` -> This is the main python script where the flow starts
- `productivity` -> This is the package where core modules live

## ▶️ How to Run
### 1️⃣ Clone the repository
```bash
git clone https://github.com/Mohandas-KJ/productivity-pomodoroCLI.git
cd productivity-promodoroCLI
```

### 2️⃣ Run the application
```bash
python run.py
```

That’s it. No setup. No environment variables. No package installation.

## 🧠 Why `run.py` Exists
The project uses a src/ layout.
To keep execution simple for users, run.py delegates execution to the main program inside src.

This avoids:
- PYTHONPATH issues
- confusing python -m commands
- platform-specific import errors

You can still run the core file if needed:
```bash
python src/promodoro.py
```

## 🛠️ Current Features
- Micro Time Blocking (Elon Musk–style scheduling)
- Interactive CLI menu
- Cross-platform terminal support

More techniques will be added incrementally.

## 📚 Learning Notes (Planned)
This repository will include a future folder documenting:
- Workflow design decisions
- Algorithms used
- Concepts learned during development
- Personal notes on threading, scheduling, and CLI UX
- Mistakes, fixes, and insights
- Learning is documented in my own words, not copied explanations.

## 💡 Philosophy
**Productivity tools should reduce friction, not create it.**
This project prioritizes clarity, portability, and learning over unnecessary abstractions.

## 🛠️ Tech Stack
- Language: Python
- Interface: Command Line (CLI)
- Core Concepts:
    - Threading
    - Timers
    - State management
    - Modular design

## 🤝 Contribution
This is currently a personal productivity project, but suggestions and improvements are welcome.

If you find an idea, optimization, or improvement — feel free to open an issue or fork.

## ❤️ Final Note
This project is a reflection of learning by building.
It is not about perfection — it is about progress, execution, and discipline.
