# 🧠 AutoPilot HR

A powerful, AI-driven HR automation platform built to streamline resume screening, candidate evaluation, and decision support for recruiters — all with minimal manual intervention.

---

🚀 **Features**

- ✅ **Resume Parsing** – Extract structured data from PDFs, Word docs, and raw text resumes.
- 🤖 **LLM-Powered Evaluation** – Use GPT-based models to rank, screen, and match candidates.
- 🔍 **Job-Candidate Matching** – Score and filter applicants based on custom job descriptions.
- 🗂️ **Batch Processing** – Automate bulk resume analysis and export structured results.
- 📊 **Insights & Summarization** – Generate summaries and red flags for hiring managers.
- 📝 **PDF & XLSX Export** – Get clean output files for each candidate or the entire batch.

---

🏴‍☠️ **Tech Stack**

| Layer            | Technologies Used                                                      |
|------------------|-----------------------------------------------------------------------|
| **Backend**      | Python, FastAPI                                                       |
| **AI Models**    | OpenAI GPT (3.5/4), LangChain                                         |
| **Parsing**      | `python-docx`, `pdfminer`, `PyMuPDF`, `spaCy`                         |
| **Data**         | `pandas`, `xlsxwriter`, `openpyxl`                                    |
| **Orchestration**| UiPath Studio, UiPath Document Understanding Module                   |
| **Deployment**   | Docker (planned), GitHub Actions (CI/CD ready)                        |

---

## Overview
AutoPilot HR is an advanced, modular Human Resources management platform that leverages artificial intelligence, robotic process automation (RPA), and data-driven workflows to automate and optimize end-to-end HR operations. The system is designed to handle high volumes of candidate data, streamline communication, and facilitate decision-making for HR professionals.

### Key Components & Architecture
- **AI-Services Backend:**
  - Built with FastAPI, this backend provides RESTful APIs for resume parsing, candidate ranking, and job-candidate matching using machine learning models and prompt-based AI services.
  - Integrates with external AI providers and custom models for document analysis and natural language processing.
- **UiPath Workflows:**
  - A suite of RPA workflows (in `.xaml` format) automates repetitive HR tasks such as email monitoring, document processing, interview scheduling, and data entry.
  - Workflows interact with both internal data and external systems (e.g., email servers, HR databases).
- **Configuration Layer:**
  - Centralized configuration management for system settings, job profiles, and communication templates, enabling easy customization and scaling across different HR scenarios.
- **Data Management:**
  - Structured directories for input (applications, resumes, job descriptions), processed data (parsed resumes, analysis results), and output (candidate profiles, reports, communications).
  - Ensures data traceability and compliance with HR data standards.
- **Deployment & Integration:**
  - Supports deployment via Docker and cloud scripts for scalable, production-ready environments.
  - Modular design allows integration with existing HRIS, ATS, and third-party services.

### Workflow Example
1. **Resume Submission:** Candidates submit resumes via email or web portal.
2. **Automated Ingestion:** UiPath workflows monitor inboxes and extract attachments, saving them to the input directory.
3. **AI Processing:** The backend parses resumes, extracts key information, and matches candidates to job profiles using AI models.
4. **Profile Generation:** Processed candidate data is stored and formatted for HR review.
5. **Communication:** Automated emails (e.g., acknowledgments, interview invitations) are sent using configurable templates.
6. **Reporting:** The system generates analytics and reports for HR decision-makers.

This architecture enables HR teams to reduce manual workload, improve candidate experience, and make data-driven hiring decisions efficiently.

## Directory Structure
```
AutoPilot HR/
├── AI-Services/           # Backend AI services (API, models, prompts)
├── Configuration/         # System and job profile configurations, email templates
├── Data/                  # Input, output, and processed data (resumes, reports, etc.)
├── Deployment/            # Deployment scripts and cloud/docker configs
├── Documentation/         # API docs, guides, and screenshots
├── Testing/               # Integration and unit tests, test data
├── UiPath-Workflows/      # RPA workflows for HR automation
├── GlobalHandlerX.xaml    # Global workflow handler
├── Main.xaml              # Main workflow entry point
├── Project_Notebook.xlsx  # Project notes and tracking
```

## Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd "AutoPilot HR"
   ```
2. **Set up Python environment:**
   - Navigate to `AI-Services/` and activate the virtual environment:
     ```bash
     cd AI-Services
     source autopilot_env/bin/activate  # On macOS/Linux
     .\autopilot_env\Scripts\activate  # On Windows
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
3. **Configuration:**
   - Update configuration files in `Configuration/system_settings/` and `UiPath-Workflows/Main Process/Config/` as needed.

## Usage
- **AI Services:**
  - Run the FastAPI backend:
    ```bash
    uvicorn api.app:app --reload
    ```
- **UiPath Workflows:**
  - Open `.xaml` files in UiPath Studio to run or modify RPA workflows.
- **Data Processing:**
  - Place input files (resumes, job descriptions) in `Data/Input/`.
  - Processed results and reports will be available in `Data/Processed/` and `Data/Output/`.

## Testing
- Integration and unit tests are located in `Testing/`.
- To run Python tests (if using pytest):
  ```bash
  cd AI-Services
  pytest
  ```
- For UiPath workflow tests, use UiPath Studio's built-in testing tools.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes. For major changes, discuss them via an issue first.

## License
This project is licensed under the MIT License (2025). See the LICENSE file for details.
