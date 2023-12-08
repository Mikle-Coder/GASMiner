# GASMiner

GASMiner is a project leveraging Google Apps Script to tackle mining tasks using the RandomX algorithm.

## Overview

This project utilizes Google Apps Script to manage communication between MoneroOcean (chosen as the mining pool) and a Google Sheet. Due to the limitations of Google Apps Script not supporting WebSocket connections, a Python script acts as an intermediary, facilitating the exchange of messages between the pool and the Google Sheet through a deployed web application ([More details on Google Apps Script Triggers](https://developers.google.com/apps-script/guides/triggers?hl=en#dogete_and_doposte)).

## Project Structure

- **Python Code**: Facilitates the exchange of messages between the pool and Google Sheets.
- **Google Sheet**: Serves as a temporary storage for tasks and results. Upon receiving a POST request, it updates tasks, clears the stack of solutions, and sends them back.


## Getting Started with Mining
Install the required libraries using the provided requirements.txt file:
```bash
pip install -r requirements.txt
```
Run the miner.py script to begin mining:
```bash
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
