<div align="center">

  # COVID19-WEB-SCRAPER

  [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
  ![Status](https://img.shields.io/badge/Status-Completed-success)
  [![Platform](https://img.shields.io/badge/Platform-Python%20%7C%20Linux%20%7C%20Windows-blueviolet)](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)
  [![Technology](https://img.shields.io/badge/Technology-Python%20%7C%20BeautifulSoup-orange)](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)
  [![Developed by](https://img.shields.io/badge/Developed%20by-Amey%20Thakur%20%26%20Hasan%20Rizvi-blue)](https://github.com/Amey-Thakur)

  A comprehensive data scraping and visualization tool for monitoring live COVID-19 statistics in India.

  **[Source Code](Source%20Code/)** &nbsp;&middot;&nbsp; **[Technical Specification](docs/SPECIFICATION.md)**

</div>

---

<div align="center">

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Visualization](#visualization-results) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

</div>

---

<!-- AUTHORS -->
<div align="center">

  ## Authors

  **Terna Engineering College | Computer Engineering | Batch of 2022**

  <table>
  <tr>
  <td align="center">
  <a href="https://github.com/Amey-Thakur">
  <img src="https://github.com/Amey-Thakur.png" width="150px;" alt="Amey Thakur"/><br />
  <sub><b>Amey Thakur</b></sub>
  </a>
  </td>
  <td align="center">
  <a href="https://github.com/rizvihasan">
  <img src="https://github.com/rizvihasan.png" width="150px;" alt="Hasan Rizvi"/><br />
  <sub><b>Hasan Rizvi</b></sub>
  </a>
  </td>
  </tr>
  </table>

  *Special thanks to [Hasan Rizvi](https://github.com/rizvihasan) for his meaningful contributions, guidance, and support that helped shape this work.*

</div>

---

<!-- OVERVIEW -->
## Overview

The **COVID19-WEB-SCRAPER** is a Python-based utility developed to provide real-time insights into the COVID-19 situation in India. It programmatically extracts live data from the **[Ministry of Health and Family Welfare (MOHFW)](https://www.mohfw.gov.in)** website and processes it into actionable visualizations.

Developed as a mini-project for the **Open Source Tech Lab**, this tool demonstrates the practical application of web scraping (BeautifulSoup), data manipulation (Pandas), and complex statistical visualization (Matplotlib & Seaborn).

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

```
COVID19-WEB-SCRAPER/
│
├── Source Code/                     # Main Python Implementation
│   ├── Covid19_Web_Scraper.py       # Core scraping logic
│   └── Covid19_Web_Scraper.ipynb    # Jupyter Notebook for Colab/Kaggle
│
├── Mini Project/                    # Visualization & Reports
│   └── Outputs/                     # Generated data visualizations
│       ├── COVID19 India Bar Plot.jpg
│       └── COVID19 India Donut Chart.jpg
│
├── docs/                            # Project Documentation
│   └── SPECIFICATION.md             # Formal Technical Specification
│
├── LICENSE                          # MIT License
├── CITATION.cff                     # Citation Metadata
├── SECURITY.md                      # Security Policy & Posture
├── codemeta.json                    # Project Metadata (JSON-LD)
└── README.md                        # Project Documentation
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
  ![Bar Plot](Mini%20Project/Outputs/COVID19%20India%20Bar%20Plot.jpg)

  ### Nationwide Distribution (Donut Chart)
  ![Donut Chart](Mini%20Project/Outputs/COVID19%20India%20Donut%20Chart.jpg)

</div>

---

<!-- LICENSE -->
## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**Summary**: You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original author.

**Copyright &copy; 2020** [Amey Thakur](https://github.com/Amey-Thakur), [Hasan Rizvi](https://github.com/rizvihasan)

---

<!-- ABOUT -->
## About This Repository

**Created & Maintained by**: [Amey Thakur](https://github.com/Amey-Thakur)  
**Academic Journey**: Bachelor of Engineering in Computer Engineering (2018-2022)  
**Institution**: [Terna Engineering College](https://ternaengg.ac.in/), Navi Mumbai  
**University**: [University of Mumbai](https://mu.ac.in/)

This project features the COVID19-WEB-SCRAPER, a terminal-based data analysis utility developed as a 4th-semester mini-project for the Open Source Tech Lab course. It showcases the practical application of web scraping logic, high-precision data normalization, and comparative statistical visualization.

**Connect**: [GitHub](https://github.com/Amey-Thakur) · [LinkedIn](https://www.linkedin.com/in/amey-thakur)

### Acknowledgments

Grateful acknowledgment to **[Hasan Rizvi](https://github.com/rizvihasan)** for his pivotal role and collaborative excellence during the development of this project. His expertise in logical structuring and data visualization was instrumental in the success of this project. This technical record serves as a testament to his scholarly partnership and significant impact on the final implementation.

Special thanks to the faculty members of the Department of Computer Engineering at Terna Engineering College for their guidance during the course of this project. Gratitude is also extended to the mentors and peers who supported this learning endeavor.

---

<!-- FOOTER -->
<div align="center">

  [↑ Back to Top](#covid19-web-scraper)

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Visualization](#visualization-results) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

  <br>

  🔬 **[Open Source Tech Lab](https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB)** &nbsp;·&nbsp; 🖥️ **[COVID19-WEB-SCRAPER](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)**

</div>

---

<div align="center">

  ### Presented as part of the 4th Semester Mini-Project @ Terna Engineering College

  ### 🎓 [Computer Engineering Repository](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)

  **Computer Engineering (B.E.) - University of Mumbai**

  *Semester-wise curriculum, laboratories, projects, and academic notes.*

</div>
