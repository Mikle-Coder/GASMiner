# GASMiner

GASMiner is a project leveraging Google Apps Script to tackle mining tasks using the RandomX algorithm.

## Overview

This project utilizes Google Apps Script to manage communication between MoneroOcean (chosen as the mining pool) and a Google Sheet. Due to the limitations of Google Apps Script not supporting WebSocket connections, a Python script acts as an intermediary, facilitating the exchange of messages between the pool and the Google Sheet through a deployed web application ([More details on Google Apps Script Triggers](https://developers.google.com/apps-script/guides/triggers?hl=en#dogete_and_doposte)).

## Project Structure

- **Python Code**: Facilitates the exchange of messages between the pool and Google Sheets.
- **Google Sheet**: Serves as a temporary storage for tasks and results. Additionally, this project employs a computational spreadsheet system that enhances computational power by utilizing multiple Google accounts.
- **Computational Spreadsheet System**: This system merges computational spreadsheets from multiple Google accounts to enhance computational power.

## Getting Started with Mining

Install the required libraries using the provided requirements.txt file:
```
pip install -r requirements.txt
```
Run the miner.py script to begin mining:
```
python miner.py
```

## Adding Computational Power

1. **Google Account Setup**:
   - Open the [Google Sheet](https://docs.google.com/spreadsheets/d/1lk87CkAqxpGPVCNnv_MaAZDYEFwkAd-1r60-d1raqU8) on your Google account.
   - Click on `SetupThreads` to trigger a script that copies necessary sheets to your Google Drive for computations.
   - This action will create a folder named 'Threads' on your Google Drive, containing 10 sheets titled 'Thread...' and one sheet named 'Task'.

2. **Setting Up Threads**:
   - Access each sheet with 'Thread' in its name and click on `RunThread`.
   - This will execute a script that creates 20 time-based triggers (every minute) to initiate the computational script.

This setup will increase the overall computational capacity by 200 solutions per minute.
