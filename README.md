# MCP Learning Journey 🚀

Hands-on repository for learning **Model Context Protocol (MCP)** while following the Udemy course:

> [MCP Bootcamp: Build, Deploy & Secure Model Context Protocol](https://www.udemy.com/course/learn-mcp-model-context-protocol-course-and-a2a-bootcamphands-hands-on/)

We build everything from scratch and grow this repo step-by-step with every lecture.

---

## 📁 Project Structure

```
mcp-learning-journey/
├── python-server/          # Python MCP server, client, and chatbot host
├── typescript-server/      # TypeScript / Node.js MCP servers
├── docs/                   # Notes, architecture diagrams, resources
├── notes/                  # Personal learning notes from each lecture
├── .gitignore
└── README.md
```

---

## 🛠️ Prerequisites

- **Python 3.10+** (recommended 3.11 or 3.12)
- **Node.js 20+**
- **uv** (Python package manager) → `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Git**
- Claude Desktop / Cursor / VS Code (for testing MCP servers)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/suryansh74/mcp-learning-journey.git
cd mcp-learning-journey
```

### 2. Python Server Setup (recommended starting point)
```bash
cd python-server
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
uv sync
```

### 3. Run the client demo
```bash
uv run python client.py
```

`client.py` starts `hello_world.py` as a separate process and calls its tools over stdio. It does not import the server functions.

### 4. TypeScript Server Setup (later)
```bash
cd typescript-server
npm init -y
npm install @modelcontextprotocol/sdk zod
```

---

## 📚 Learning Path (we will fill this as we progress)

| # | Topic | Status | Folder |
|---|-------|--------|--------|
| 1 | Environment Setup & First Hello World Server | ✅ Done | `python-server/` |
| 2 | Tools | ✅ Done | `python-server/hello_world.py` |
| 3 | Resources | ✅ Done | `python-server/hello_world.py` |
| 4 | Prompts | ✅ Done | `python-server/hello_world.py` |
| 5 | Transports (stdio vs Streamable HTTP) | 🟡 stdio only | `python-server/client.py` |
| 6 | Clients | ✅ Done | `python-server/client.py` |
| 7 | Debugging with MCP Inspector | ⬜ Pending | |
| 8 | Security & OAuth | ⬜ Pending | |
| 9 | Deployment (Docker / Cloudflare / AWS) | ⬜ Pending | |
| 10 | A2A (Agent-to-Agent) | ⬜ Pending | |

---

## 🔗 Useful Official Links

- [Official MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)

---

## 📝 How we will work

1. You watch the lecture
2. We implement / improve the code together
3. You push the changes
4. We review and move to the next concept

Let's build real understanding, not just copy-paste.

Happy learning! 🔥
