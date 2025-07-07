# 🧠 AutoPilot HR

A powerful, AI-driven HR automation platform built to streamline resume screening, candidate evaluation, and decision support for recruiters — all with minimal manual intervention.

---

## 🚀 Features

- ✅ **Resume Parsing** – Extract structured data from PDFs, Word docs, and raw text resumes.  
- 🤖 **LLM-Powered Evaluation** – Use GPT-based models to rank, screen, and match candidates.  
- 🔍 **Job-Candidate Matching** – Score and filter applicants based on custom job descriptions.  
- 🗂️ **Batch Processing** – Automate bulk resume analysis and export structured results.  
- 📊 **Insights & Summarization** – Generate summaries and red flags for hiring managers.  
- 📁 **PDF & XLSX Export** – Get clean output files for each candidate or the entire batch.  

---

## 🏗️ Tech Stack

| Layer         | Technologies Used                                               |
|---------------|------------------------------------------------------------------|
| **Backend**   | Python, Flask                                                   |
| **AI Models** | OpenAI GPT (3.5/4), LangChain                                   |
| **Parsing**   | `python-docx`, `pdfminer`, `PyMuPDF`, `spaCy`                  |
| **Data**      | `pandas`, `xlsxwriter`, `openpyxl`                             |
| **Orchestration** | UiPath Studio, UiPath Document Understanding Module     |
| **Deployment**| Docker (planned), GitHub Actions (CI/CD ready)                 |

---

## 🧪 Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/sujanfx/autopilot-hr.git
cd autopilot-hr
```

###2. Create and activate a virtual environment
```bash
Copy
Edit
python3 -m venv autopilot_env
source autopilot_env/bin/activate  # Mac/Linux
```

# OR

``` autopilot_env\Scripts\activate.bat  # Windows ```

### 3. Install dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```

### 4. Run the server
```bash
Copy
Edit
python main.py
```

For full automation via UiPath, refer to the UiPath-Workflows/ folder.

## 📁 Project Structure
```
graphql
Copy
Edit
AutoPilot-HR/
├── AI-Services/               # GPT-based scoring and evaluation modules
├── UiPath-Workflows/          # RPA workflows (resume download, automation, etc.)
├── Documentation/             # Screenshots, diagrams, architecture
├── project.json               # UiPath project configuration
├── Main.xaml                  # Entry-point for UiPath automation
└── ...

```

## 📄 License
MIT License © 2025 Sujan Sridhara

