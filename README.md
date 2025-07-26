# 🤖 AI Agent MVP - Autonomous Software Development

> **Self-Improving AI Agent for Automatic Software Project Generation**

An intelligent AI-powered system that automatically analyzes, designs, codes, tests, and documents complete software projects using state-of-the-art language models via OpenRouter.ai.

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-FF6B6B?style=for-the-badge&logo=openai&logoColor=white)](https://openrouter.ai/)

---

## 🎯 **What Does It Do?**

The AI Agent MVP takes a simple project description and automatically generates:

1. **📊 Project Analysis** - Requirements, user stories, technical specifications
2. **🏗️ Software Architecture** - System design, database schema, API structure  
3. **💻 Complete Source Code** - Ready-to-run project files and folders
4. **🧪 Testing Strategy** - Test cases, automation setup, quality gates
5. **📚 Documentation** - User guides, API docs, deployment instructions
6. **🔧 Real Project Files** - Actual working directories with proper file structure

**Input:** `"Build a todo app with React frontend and Node.js backend"`  
**Output:** Complete working project with all files, documentation, and deployment ready!

---

## ✨ **Key Features**

- 🚀 **End-to-End Automation** - From idea to working code
- 🤖 **Multi-Model Support** - Works with various AI models via OpenRouter
- 📁 **Real File Generation** - Creates actual project directories and files
- 🐳 **Docker Ready** - Containerized for easy deployment
- 🔄 **Sequential Pipeline** - 6-phase structured development process
- 📊 **Comprehensive Logging** - Track every step of the generation process
- 🎯 **Production Ready** - Clean, documented, and maintainable code output

---

## 🛠️ **Tech Stack**

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.12 + FastAPI |
| **AI Integration** | OpenRouter.ai API |
| **Current Model** | Qwen 3 Coder (Free) |
| **Container** | Docker + Docker Compose |
| **Environment** | python-dotenv |
| **HTTP Client** | requests |

---

## 🚀 **Quick Start**

### Prerequisites

- Docker and Docker Compose
- OpenRouter.ai API key ([Get yours here](https://openrouter.ai/keys))

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mvp-ai-agent.git
cd mvp-ai-agent
```

### 2. Configure Environment

```bash
# Add your OpenRouter API key to .env
echo "OPENROUTER_API_KEY=your_actual_api_key_here" >> .env
```

### 3. Build and Run

```bash
# Build the Docker image
docker build -t mvp-ai-agent .

# Run with volume mapping for real-time file access
docker run -d -p 8000:8000 -v $(pwd)/outputs:/app/outputs mvp-ai-agent
```

### 4. Test the API

```bash
# Check if the service is running
curl http://localhost:8000/health

# Generate your first project
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"description": "Build a simple todo app with React frontend and Express.js backend"}'
```

### 5. Check Generated Files

```bash
# View generated project structure
ls -la outputs/
tree outputs/source_code/  # If tree is installed

# Generated files will be in:
# outputs/source_code/frontend/
# outputs/source_code/backend/
```

---

## 📚 **API Documentation**

### Interactive API Docs

Once running, visit: **http://localhost:8000/docs**

### Main Endpoints

#### `POST /generate`
Generate a complete software project from description.

**Request:**
```json
{
  "description": "Your project description here"
}
```

**Response:**
```json
{
  "success": true,
  "message": "AI agent pipeline completed successfully",
  "execution_time": 45.2,
  "outputs": {
    "analysis": "outputs/analysis.md",
    "design": "outputs/design.md",
    "source_code": "outputs/source_code/implementation.md",
    "testing": "outputs/tests.md",
    "documentation": "outputs/documentation.md"
  },
  "project_generation": {
    "success": true,
    "created_files": ["frontend/App.jsx", "backend/server.js"],
    "created_directories": ["frontend", "backend"],
    "total_files": 8,
    "total_directories": 3
  }
}
```

#### Other Endpoints
- `GET /health` - Health check
- `GET /` - Service status

---

## ⚙️ **Configuration**

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key | **Required** |
| `OPENROUTER_MODEL` | AI model to use | `qwen/qwen3-coder:free` |

### Model Switching

**Available Models:**
- `qwen/qwen3-coder:free` (Default - Free)
- `google/gemini-2.0-flash-exp:free` (Free)
- `anthropic/claude-3.5-sonnet` (Paid)
- `openai/gpt-4o` (Paid)

**Switch Models:**
```bash
# Via environment variable
export OPENROUTER_MODEL="google/gemini-2.0-flash-exp:free"

# Via Docker run
docker run -e OPENROUTER_MODEL="anthropic/claude-3.5-sonnet" mvp-ai-agent
```

---

## 📁 **Project Structure**

```
mvp-ai-agent/
├── app.py                      # FastAPI orchestrator
├── openrouter_service.py       # AI model integration
├── model_config.py            # Model configuration
├── prompts/                   # AI prompt templates
│   ├── analysis.txt
│   ├── design.txt
│   ├── coding.txt
│   ├── testing.txt
│   └── documentation.txt
├── outputs/                   # Generated content
│   ├── analysis.md           # Project analysis
│   ├── design.md             # Architecture design
│   ├── tests.md              # Testing strategy
│   ├── documentation.md      # Final documentation
│   └── source_code/          # Real project files
│       ├── frontend/         # Frontend application
│       ├── backend/          # Backend application
│       └── database/         # Database files
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container configuration
└── .env                     # Environment variables
```

---

## 🎯 **Example Use Cases**

### Web Applications
```json
{
  "description": "Create a blog platform with user authentication, post creation, comments, and admin panel using Next.js and PostgreSQL"
}
```

### Mobile Backend
```json
{
  "description": "Build a REST API for a fitness tracking app with user profiles, workout logging, and progress analytics using FastAPI and MongoDB"
}
```

### Desktop Application
```json
{
  "description": "Develop a file organizer desktop app with drag-drop interface, automatic categorization, and cloud sync using Electron and Node.js"
}
```

---

## 🔄 **Development Workflow**

### The 6-Phase Pipeline

1. **🔍 Analysis Phase** - Requirements gathering, user stories, technical specs
2. **🏗️ Design Phase** - System architecture, database design, API specs
3. **💻 Coding Phase** - Complete source code, project structure, config files
4. **🧪 Testing Phase** - Test strategies, test cases, quality assurance
5. **📚 Documentation Phase** - User docs, API docs, deployment guides
6. **🔧 Real Project Generation** - Actual file creation, directory structure

---

## 📊 **Performance & Limitations**

| Metric | Value |
|--------|-------|
| **Average Generation Time** | Depending on the performance of the language model |
| **Supported File Types** | JavaScript, Python, HTML, CSS, JSON, Markdown |
| **Max Project Complexity** | Medium to large applications |
| **Concurrent Requests** | Limited by OpenRouter rate limits |

---

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone and setup
git clone https://github.com/yourusername/mvp-ai-agent.git
cd mvp-ai-agent

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

---

## 📄 **License**

This project is licensed under the MIT License.

---

## 🙏 **Acknowledgements**

- [OpenRouter.ai](https://openrouter.ai/) for AI model access
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Qwen Team](https://qwenlm.github.io/) for the coding-specialized model

---

## 📞 **Support**

- 🐛 **Issues:** [GitHub Issues](https://github.com/yourusername/mvp-ai-agent/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/yourusername/mvp-ai-agent/discussions)

---

**Made with ❤️ by Ömer Yasir Önal([https://github.com/yourusername](https://github.com/OmerYasirOnal))**

> *"From idea to implementation in minutes, not months."*
