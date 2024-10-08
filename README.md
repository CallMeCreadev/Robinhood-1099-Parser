New Feature: September 9th 2024 (CallMeCreadev)
Allow users to run an executable that creates a drag and drop interface to convert their PDF into CSV.  No longer required to have python installed. 

# 🍃 Robinhood 1099 Parser

[![Build](https://github.com/kevinpark1217/Robinhood-1099-Parser/actions/workflows/build.yaml/badge.svg)](https://github.com/kevinpark1217/Robinhood-1099-Parser/actions/workflows/build.yaml)

> This project converts Robinhood Securities 1099 tax document from PDF to CSV file. This tool will be helpful for those who need every transaction in a spreadsheet format for tax reporting purposes.


### Original Work

Copyright (c) 2021 Keun Park (kevin.park1217@gmail.com)

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate?business=P3M77TR7L8LBA&item_name=Thanks+for+supporting+my+work%21&currency_code=USD)


## 🚀 Running Locally

### Prerequisites

Make sure you have the following installed on your computer.
- Latest [Python 3](https://www.python.org/downloads/)  
  Must be version 3.8 or higher
- [**Windows Only**] [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)  
  In the installer, select
  - C++ build tools
  - the *Windows 10 SDK*
  - the latest version of *MSVC v142 x64/x86 build tools*.


### Installing
```bash
python -m pip install wheel
python -m pip install --upgrade rh_1099
```
**Note**: If commands above fail, try replacing `python` with `python3`

### Running
```bash
➜ rh_1099
usage: rh_1099 [-h] --pdf FILE [--csv FILE] [--silent] [--check]
```

### Example and Checking

Enable `--check` flag to print out total values for some columns. Make sure these values match with the PDF!

```bash
➜ rh_1099 --pdf rh_1099.pdf --check
Pages: 100%|██████████████████████████████████████████████████████████████| 40/40 [00:03<00:00, 10.41it/s]
>>> Calculated Totals:
    Make sure the values matches with the PDF totals!
    proceeds: 77521.03, cost: 80902.05, wash_sales_loss: 3733.41, gain_loss: 352.39
>>> Saved to output.csv
```

## 🐞 Issues and Bugs
If you have any issues with the tool, please open a GitHub Issue with as much as detail as you can provide.
