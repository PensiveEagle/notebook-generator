<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PensiveEagle">
    <img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/pensiveeagle-logo.svg" alt="Pensive Eagle Logo" width="200" height="auto">
  </a>

<h3 align="center">PDF Notebook Generator</h3>

  <p align="center">
    A simple python project that generates a work notebook .pdf based on the contents of a .csv
    <br />
  <!--  <a href="https://github.com/PensiveEagle/notebook-generator"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
  <!--  <a href="https://github.com/PensiveEagle/notebook-generator">View Demo</a>
    &middot;
    <a href="https://github.com/PensiveEagle/notebook-generator/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/PensiveEagle/notebook-generator/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a practice project that takes .csv data containing a list of topics and the number of pages each topic should have and produces a .pdf file of a notebook with headers and footer for the topics on each relevant page.

<img src="https://github.com/PensiveEagle/repo-assets/blob/main/readme_assets/notebook-generator-assets/notebook_screenshot.png?raw=true" alt="CLI Screenshot" width="100%" height="auto">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][python-shield]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* python 3.14

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/PensiveEagle/notebook-generator.git
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin PensiveEagle/notebook-generator
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project create a templated notebook based on the contents of the topics.csv

To create your own custom notebooks with your own topics:

1. Setup the csv to contain the topics you want and the number of pages for each topic
2. Run the programme
   ```sh
   python.exe main.py
   ```
3. Your .pdf notebook will be output to the project folder

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python Mega Course: Build 20 Real-World Apps and AI Agents - Ardit Sulce](https://www.udemy.com/course/the-python-mega-course/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center"><img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/makers_mark_circle.svg" width="50"></div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PensiveEagle/notebook-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/PensiveEagle/notebook-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PensiveEagle/notebook-generator.svg?style=for-the-badge
[forks-url]: https://github.com/PensiveEagle/notebook-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/PensiveEagle/notebook-generator.svg?style=for-the-badge
[stars-url]: https://github.com/PensiveEagle/notebook-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/PensiveEagle/notebook-generator.svg?style=for-the-badge
[issues-url]: https://github.com/PensiveEagle/notebook-generator/issues
[license-shield]: https://img.shields.io/github/license/PensiveEagle/notebook-generator.svg?style=for-the-badge
[license-url]: https://github.com/PensiveEagle/notebook-generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[python-shield]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/

