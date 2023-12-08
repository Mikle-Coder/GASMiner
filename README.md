





















# GASMiner

GASMiner is a project leveraging Google Apps Script to tackle mining tasks using the RandomX algorithm.

## Overview

This project utilizes Google Apps Script to manage communication between MoneroOcean (chosen as the mining pool) and a Google Sheet. Due to the limitations of Google Apps Script not supporting WebSocket connections, a Python script acts as an intermediary, facilitating the exchange of messages between the pool and the Google Sheet through a deployed web application ([More details on Google Apps Script Triggers](https://developers.google.com/apps-script/guides/triggers?hl=en#dogete_and_doposte)).

## Project Structure

- **Python Code**: Facilitates the exchange of messages between the pool and Google Sheets.
- **Google Sheet**: Serves as a temporary storage for tasks and results. Additionally, this project employs a computational spreadsheet system that enhances computational power by utilizing multiple Google accounts.

### Computational Spreadsheet System

The computational spreadsheet system optimizes mining tasks by leveraging multiple Google accounts. Upon clicking `SetupThreads` on the main Google Sheet, the system generates a folder named 'Threads' in the user's Google Drive. This folder contains several sheets titled 'Thread...' and one sheet named 'Task'.

Each 'Thread...' sheet corresponds to a specific Google account. By clicking `RunThread` on these sheets, users initiate the creation of time-based triggers (every minute) within each sheet. These triggers execute the computational script, significantly boosting the overall computational capacity by 200 solutions per minute per sheet.

This setup allows for the distribution of mining tasks across multiple Google accounts, thereby enhancing the mining process's efficiency.

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

2. **Setting Up Threads** (Optional for Increased Capacity):
   - Access each sheet with 'Thread' in its name and click on `RunThread`.
   - This will execute a script that creates 20 time-based triggers (every minute) to initiate the computational script.
   - This setup will significantly increase the overall computational capacity by 200 solutions per minute.

**Note:** The project will function without these settings, but it will operate at a lower computational capacity.

## Additional Notes

- Ensure Python and necessary libraries are installed.
- Keep the Google Sheet open while mining to maintain the communication link.

## Note

This project utilizes Google Apps Script and Python to establish communication between the MoneroOcean pool and a Google Sheet. Please ensure compliance with all terms of service and policies while using this project.

Feel free to reach out for any questions or troubleshooting!


































# GASMiner

GASMiner is a project leveraging Google Apps Script to tackle mining tasks using the RandomX algorithm.

## Overview

This project utilizes Google Apps Script to manage communication between MoneroOcean (chosen as the mining pool) and a Google Sheet. Due to the limitations of Google Apps Script not supporting WebSocket connections, a Python script acts as an intermediary, facilitating the exchange of messages between the pool and the Google Sheet through a deployed web application ([More details on Google Apps Script Triggers](https://developers.google.com/apps-script/guides/triggers?hl=en#dogete_and_doposte)).

## Project Structure

- **Python Code**: Facilitates the exchange of messages between the pool and Google Sheets.
- **Google Sheet**: Serves as a temporary storage for tasks and results. The computational spreadsheet system automatically records the outcomes into this sheet.


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

2. **Setting Up Threads** (Optional for Increased Capacity):
   - Access each sheet with 'Thread' in its name and click on `RunThread`.
   - This will execute a script that creates 20 time-based triggers (every minute) to initiate the computational script.
   - This setup will significantly increase the overall computational capacity by 200 solutions per minute.

**Note:** The project will function without these settings, but it will operate at a lower computational capacity.

## Additional Notes

- Ensure Python and necessary libraries are installed.
- Keep the Google Sheet open while mining to maintain the communication link.

## Note

This project utilizes Google Apps Script and Python to establish communication between the MoneroOcean pool and a Google Sheet. Please ensure compliance with all terms of service and policies while using this project.

Feel free to reach out for any questions or troubleshooting!
