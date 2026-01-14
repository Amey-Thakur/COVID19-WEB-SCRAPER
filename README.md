
<div align="center">

  # COVID19-WEB-SCRAPER

  [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
  ![Status](https://img.shields.io/badge/Status-Completed-success)
  [![Platform](https://img.shields.io/badge/Platform-Python%20%7C%20Linux%20%7C%20Windows-blueviolet)](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)
  [![Technology](https://img.shields.io/badge/Technology-Python%20%7C%20BeautifulSoup-orange)](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)
  [![Developed by](https://img.shields.io/badge/Developed%20by-Amey%20Thakur%20%26%20Hasan%20Rizvi-blue)](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)

  A robust data scraping and visualization tool for monitoring live COVID-19 statistics in India, implemented using Python, Beautiful Soup, and Seaborn for scholarly analysis.

  **[Source Code](Source%20Code/)** &nbsp;·&nbsp; **[Technical Specification](docs/SPECIFICATION.md)** &nbsp;·&nbsp; **[Kaggle Notebook](https://www.kaggle.com/code/ameythakur20/covid19-web-scraper)**

</div>

---

<div align="center">

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Visualization](#visualization-results) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

</div>

---

<!-- AUTHORS -->
<div align="center">

  ## Authors

  **Terna Engineering College | Computer Engineering | Batch of 2022**

| <a href="https://github.com/Amey-Thakur"><img src="https://github.com/Amey-Thakur.png" width="150" height="150" alt="Amey Thakur"></a><br>[**Amey Thakur**](https://github.com/Amey-Thakur)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-green.svg)](https://orcid.org/0000-0001-5644-1575) | <a href="https://github.com/rizvihasan"><img src="https://github.com/rizvihasan.png" width="150" height="150" alt="Hasan Rizvi"></a><br>[**Hasan Rizvi**](https://github.com/rizvihasan)<br><br>[![GitHub](https://img.shields.io/badge/GitHub-rizvihasan-181717?style=flat&logo=github&logoColor=white)](https://github.com/rizvihasan) |
| :---: | :---: |

</div>

> [!IMPORTANT]
> ### 🤝🏻 Special Acknowledgement
> *Special thanks to **[Hasan Rizvi](https://github.com/rizvihasan)** for his meaningful contributions, guidance, and support that helped shape this work.*

---

<!-- OVERVIEW -->
## Overview

The **COVID19-WEB-SCRAPER** is a Python-based utility developed to provide real-time insights into the COVID-19 situation in India. It programmatically extracts live data from the **[Ministry of Health and Family Welfare (MOHFW)](https://www.mohfw.gov.in)** website and processes it into actionable visualizations.

Developed as a mini-project for the **Open Source Tech Lab**, this tool demonstrates the practical application of web scraping (BeautifulSoup), data manipulation (Pandas), and complex statistical visualization (Matplotlib & Seaborn).

> [!NOTE]
> **Research Impact**: The logic and architectural overview of this project are part of a curated Computer Engineering collection on ResearchGate.
> - [ResearchGate Profile](https://www.researchgate.net/profile/Amey-Thakur)

### Resources

| # | Resource | Description |
|---|---|---|
| 1 | [Kaggle Notebook](https://www.kaggle.com/code/ameythakur20/covid19-web-scraper) | Interactive Jupyter Notebook environment |
| 2 | [Technical Specification](docs/SPECIFICATION.md) | Technical architecture and logic specification |
| 3 | [Source Code](Source%20Code/) | Core Python implementation files |
| 4 | [OST Laboratory](https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB) | Academic repository for Open Source Tech |


> [!TIP]
> **Scraping Efficiency**
>
> For Large-scale data extraction or automated monitoring, the scraping logic can be optimized by implementing headless browser sessions or introducing random sleep intervals between requests. This minimizes load on the target server and reduces the risk of rate-limiting or IP blocking.

---

<!-- FEATURES -->
## Features

| Feature | Description |
|---------|-------------|
| **Live Scraping** | Real-time data extraction from official MOHFW sources |
| **Tabular Reports** | Clean, formatted console representation using `PrettyTable` |
| **Data Processing** | Automated parsing and integer conversion via `Pandas` |
| **Bar Plots** | Comparative analysis of confirmed cases across different States/UTs |
| **Donut Charts** | Proportional distribution of Nationwide Confirmed, Recovered, and Deceased cases |

### Tech Stack
- **Language**: Python 3.x
- **Libraries**: BeautifulSoup4, Requests, Pandas, Matplotlib, Seaborn, PrettyTable
- **Environment**: Local Machine / Google Colab / Kaggle

---

<!-- STRUCTURE -->
## Project Structure

```python
COVID19-WEB-SCRAPER/
│
├── docs/                                    # Formal Documentation
│   └── SPECIFICATION.md                     # Technical Architecture & Specification
│
├── Mini-Project/                            # Academic Reports
│   └── Outputs/                             # Generated Data Visualizations
│       ├── Statewise_Confirmed_Cases.jpg    # Statistical Bar Chart
│       └── Nationwide_Distribution.jpg      # Statistical Donut Chart
│
├── Source Code/                             # Core Implementation
│   ├── Scraper_Notebook.ipynb               # Jupyter Implementation
│   ├── Main_Scraper.py                      # Standalone Script
│   └── requirements.txt                     # Execution Dependencies
│
├── .gitattributes                           # Git Configuration
├── .gitignore                               # Git Ignore Rules
├── CITATION.cff                             # Citation Metadata
├── codemeta.json                            # Project Metadata (JSON-LD)
├── LICENSE                                  # MIT License
├── README.md                                # Main Documentation
└── SECURITY.md                              # Security Policy & Posture
```

---

<!-- USAGE -->
## Quick Start

### Prerequisites
- **Python 3.x**: Ensure the core interpreter is installed on your local environment.
- **Terminal**: Access to a Bash shell or command prompt for manual execution.
- **Dependencies**: Install the required analytical libraries using pip:
```bash
pip install pandas seaborn matplotlib requests beautifulsoup4 prettytable
```

> [!WARNING]
> **Technical Posture & Ethics**
>
> This tool is designed for educational purposes. Web scraping is highly dependent on the target website's DOM structure; any modifications to the MOHFW portal may require iterative updates to the scraping logic. Always adhere to the target site's `robots.txt` and ethical data collection standards.

### Installation & Deployment

1. **Clone the Collection**  
   Retrieve the localized repository using the following Git command:
   ```bash
   git clone https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER.git
   cd COVID19-WEB-SCRAPER
   ```

2. **Environment Configuration**  
   Navigate to the source directory and verify that all dependencies are resolved.

3. **Execution**  
   Execute the scraping utility directly from the terminal:
   ```bash
   python "Source Code/Covid19_Web_Scraper.py"
   ```

---

<!-- RESULTS -->
## Visualization Results

<div align="center">

  ### Statewise Confirmed Cases (Bar Plot)
  ![Bar Plot](Mini-Project/Outputs/COVID19%20India%20Bar%20Plot.jpg)

  ### Nationwide Distribution (Donut Chart)
  ![Donut Chart](Mini-Project/Outputs/COVID19%20India%20Donut%20Chart.jpg)

</div>

---

<!-- =========================================================================================
                                     USAGE SECTION
     ========================================================================================= -->
## Usage Guidelines

This repository is openly shared to support learning and knowledge exchange across the academic community.

**For Students**  
Use this mini-project as a reference for understanding web scraping logic, high-precision data normalization, and comparative statistical visualization using Python. The source code is documented to support self-paced learning and exploration of real-world data science challenges.

**For Educators**  
This project may serve as a practical example or supplementary teaching resource for Open Source Tech Lab courses (`CSL405`). Attribution is appreciated when utilizing content.

**For Researchers**  
The documentation and organization provide insights into academic project curation and educational software structuring.

---

<!-- LICENSE -->
## License

This repository and all linked academic content are made available under the **MIT License**. See the [LICENSE](LICENSE) file for complete terms.

> [!NOTE]
> **Summary**: You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original author.

Copyright © 2020 Amey Thakur, Hasan Rizvi

---

<!-- ABOUT -->
## About This Repository

**Created & Maintained by**: [Amey Thakur](https://github.com/Amey-Thakur) & [Hasan Rizvi](https://github.com/rizvihasan)  
**Academic Journey**: Bachelor of Engineering in Computer Engineering (2018-2022)  
**Institution**: [Terna Engineering College](https://ternaengg.ac.in/), Navi Mumbai  
**University**: [University of Mumbai](https://mu.ac.in/)

This project features the COVID19-WEB-SCRAPER, a terminal-based data analysis utility developed as a 4th-semester mini-project for the Open Source Tech Lab course. It showcases the practical application of web scraping logic, high-precision data normalization, and comparative statistical visualization.

**Connect:** [GitHub](https://github.com/Amey-Thakur) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/amey-thakur) &nbsp;·&nbsp; [Kaggle](https://www.kaggle.com/ameythakur20) &nbsp;·&nbsp; [ORCID](https://orcid.org/0000-0001-5644-1575)

### Acknowledgments

Grateful acknowledgment to [**Hasan Rizvi**](https://github.com/rizvihasan) for his exceptional collaboration and innovative contributions during the development of this project. His technical expertise in logical structuring, high-precision data normalization, and commitment to software quality were instrumental in building this robust web scraper. Learning alongside him was a transformative experience; his thoughtful approach to problem-solving and steady encouragement turned complex challenges into meaningful learning moments. This work reflects the growth and insights gained from our side-by-side academic journey. Thank you, Hasan, for everything you shared and taught along the way.

Grateful acknowledgment to the faculty members of the Department of Computer Engineering at Terna Engineering College for their guidance and instruction in Open Source Technology. Their expertise in collaborative development and Unix-like environments helped shape the technical foundation of this project.

Special thanks to the mentors and peers whose encouragement, discussions, and support contributed meaningfully to this learning endeavor.

---

<!-- FOOTER -->
<div align="center">

  [↑ Back to Top](#covid19-web-scraper)

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Visualization](#visualization-results) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

  <br>

  🔬 **[Open Source Tech Lab](https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB)** &nbsp;·&nbsp; 🖥️ **[COVID19-WEB-SCRAPER](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)**

</div>

---

<div align="center">

  #### Presented as part of the 4th Semester Mini-Project @ Terna Engineering College

  ---

  ### 🎓 [Computer Engineering Repository](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)

  **Computer Engineering (B.E.) - University of Mumbai**

  *Semester-wise curriculum, laboratories, projects, and academic notes.*

</div>
