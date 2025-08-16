# 🚗📄 RTO Document Automation

Automated Python tool to scrape, process, and structure RTO (Regional
Transport Office) data for compliance, validation, and analysis.\
This project helps in automating RTO workflows by downloading,
extracting, and organizing vehicle or license-related documents.

------------------------------------------------------------------------

## ⚡ Features

-   🔍 Automated fetching of RTO data using RapidAPI\
-   📂 Structured dataset creation (CSV / JSON outputs)\
-   🧾 Document parsing and text extraction\
-   🛠️ Easy integration with ML/DL models for classification or
    detection\
-   📊 Useful for compliance checks, audits, and analytics

------------------------------------------------------------------------

## 🖥️ Installation

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/Jagadeeshwaran-J/RTO_Vehicle_DATA_Fetcher.git
cd RTO_Vehicle_DATA_Fetcher
```

### 2️⃣ Create and activate a virtual environment

``` bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🚀 Usage

Run the main script with:

``` bash
python rto_automation.py
```

The processed results will be saved in the `output/` folder as
**CSV/JSON**.\
Additionally, the **vehicle information JSON** will be stored as
`vehicle_info.json`.

------------------------------------------------------------------------

## 🔑 API Setup

This project uses the **[RTO Vehicle Information
API](https://rapidapi.com/eccentricslabs/api/rto-vehicle-information-india/)**
from **RapidAPI**.

### Steps to get API Key:

1.  Go to [RapidAPI Website](https://rapidapi.com/).\
2.  Sign up for a free account.\
3.  Search for **RTO Vehicle Information India** API.\
4.  Subscribe to the API (free/paid plan).\
5.  Copy your **API Key** from the RapidAPI Dashboard.

### Update Code with Your API Key:

In `rto_automation.py`, replace:

``` python
"x-rapidapi-key": "YOUR_API_KEY_HERE",
```

with your actual API Key.

------------------------------------------------------------------------

## 📂 Project Structure

    rto-automation/
    │── rto_automation.py   # Main script
    │── requirements.txt    # Dependencies
    │── output/             # Processed datasets
    │── README.md           # Documentation

------------------------------------------------------------------------
