<div align="center">

  # Covid19 Web Scraper

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Technology](https://img.shields.io/badge/Technology-Python%20%7C%20BeautifulSoup%20%7C%20Matplotlib-blue.svg)](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)
  [![Status](https://img.shields.io/badge/Status-Completed-green.svg)](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)
  [![Developed by](https://img.shields.io/badge/Developed%20by-Amey%20Thakur-blue.svg)](https://github.com/Amey-Thakur)

  A comprehensive data scraping and visualization tool for monitoring live COVID-19 statistics in India.

  **[Source Code](Covid19_Web_Scraper.py)** • **[Google Colaboratory](Covid19_Web_Scraper.ipynb)** • **[Kaggle Notebook](https://www.kaggle.com/ameythakur20/covid19-web-scraper)**

</div>

---

<div align="center">

  [👥 Authors](#authors) &nbsp;·&nbsp; [📖 Overview](#overview) &nbsp;·&nbsp; [✨ Features](#features) &nbsp;·&nbsp; [📁 Structure](#project-structure) &nbsp;·&nbsp; [🚀 Usage](#usage) &nbsp;·&nbsp; [🖼️ Results](#visualization-results) &nbsp;·&nbsp; [📜 License](#license) &nbsp;·&nbsp; [ℹ️ About](#about-this-repository) &nbsp;·&nbsp; [🙏 Acknowledgments](#acknowledgments)

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

The **Covid19 Web Scraper** is a Python-based utility developed to provide real-time insights into the COVID-19 situation in India. It programmatically extracts live data from the **[Ministry of Health and Family Welfare (MOHFW)](https://www.mohfw.gov.in)** website and processes it into actionable visualizations.

Developed as a mini-project for the **Open Source Tech Lab (CSL405)**, this tool demonstrates the practical application of web scraping (BeautifulSoup), data manipulation (Pandas), and complex statistical visualization (Matplotlib & Seaborn).

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

### 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: BeautifulSoup4, Requests, Pandas, Matplotlib, Seaborn, PrettyTable
- **Environment**: Local Machine / Google Colab / Kaggle

---

<!-- STRUCTURE -->
## Project Structure

## Project Structure

```
COVID19-WEB-SCRAPER/
│
├── Covid19_Web_Scraper.py          # Main Python Implementation
├── Covid19_Web_Scraper.ipynb       # Jupyter Notebook for Colab/Kaggle
├── COVID19 India Bar Plot.jpg      # Visualization Output (Sample)
├── COVID19 India Donut Chart.jpg   # Visualization Output (Sample)
├── LICENSE                         # Project License
└── README.md                       # Project Documentation
```

---

<!-- USAGE -->
## Usage

### Prerequisites
Ensure you have Python 3.x installed along with the required dependencies:
```bash
pip install pandas seaborn matplotlib requests beautifulsoup4 prettytable
```

### Execution
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER.git
    cd COVID19-WEB-SCRAPER
    ```
2.  **Run the script**:
    ```bash
    python Covid19_Web_Scraper.py
    ```

---

<!-- RESULTS -->
## Visualization Results

<div align="center">

  ### Statewise Confirmed Cases (Bar Plot)
  ![COVID19 India Bar Plot](COVID19%20India%20Bar%20Plot.jpg)

  ### Nationwide Distribution (Donut Chart)
  ![COVID19 India Donut Chart](COVID19%20India%20Donut%20Chart.jpg)

</div>

---

<!-- LICENSE -->
## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**Summary**: You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original author.

**Copyright © 2020** [Amey Thakur](https://github.com/Amey-Thakur), [Hasan Rizvi](https://github.com/rizvihasan)

---

<!-- ABOUT -->
## About This Repository

**Created & Maintained by**: [Amey Thakur](https://github.com/Amey-Thakur)  
**Academic Journey**: Bachelor of Engineering in Computer Engineering (2018-2022)  
**Institution**: [Terna Engineering College](https://ternaengg.ac.in/), Navi Mumbai  
**University**: [University of Mumbai](https://mu.ac.in/)

**Connect**: [GitHub](https://github.com/Amey-Thakur) · [LinkedIn](https://www.linkedin.com/in/amey-thakur)

### Acknowledgments

Grateful acknowledgment to **[Hasan Rizvi](https://github.com/rizvihasan)** for his exceptional contribution to this project. His expertise in logical structuring and data visualization was instrumental in the success of this mini-project.

Special thanks to the faculty members of the Department of Computer Engineering at Terna Engineering College for their guidance during the course of the **Open Source Tech Lab**.

---

<!-- FOOTER -->
<div align="center">

  **[⬆ Back to Top](#covid19-web-scraper)** &nbsp;·&nbsp; [👥 Authors](#authors) &nbsp;·&nbsp; [📖 Overview](#overview) &nbsp;·&nbsp; [✨ Features](#features) &nbsp;·&nbsp; [📁 Structure](#project-structure) &nbsp;·&nbsp; [🚀 Usage](#usage) &nbsp;·&nbsp; [🖼️ Results](#visualization-results) &nbsp;·&nbsp; [📜 License](#license) &nbsp;·&nbsp; [ℹ️ About](#about-this-repository) &nbsp;·&nbsp; [🙏 Acknowledgments](#acknowledgments)

  <br>

  **[🧪 Open Source Tech Lab](https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB)** &nbsp;·&nbsp; **[💻 Project Repository](https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER)**

</div>

---

<div align="center">

  ### 🎓 [Computer Engineering Repository](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)

  **Computer Engineering (B.E.) - University of Mumbai**

  *Semester-wise curriculum, laboratories, projects, and academic notes.*

</div>
