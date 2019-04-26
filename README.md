# LibreView_to_AppleHealth_converter
Converts a CSV export of blood sugar levels from [LibreView](https://libreview.com) into a format that can be imported into the Apple Health app with [Health CSV Importer](https://lionheartsw.com/software/health-csv-importer/).

## Recommended general settings / assumptions
1. In the [LibreView account settings preferences](https://www1.libreview.com/Accounts/PatientUserSettings) set the following:
   - **Blood Glucose Units** to **mmol/L**
     - You could use **mg/dL** for import and export, by setting the relevant header name to **Blood Glucose (mg/dL)** in the [conversion script](./convert_LV_export.py)
   - **Date Format** to **Day-Month-Year**
   - **Time Format** to **24-hour**
   - **Language for UI** to **English** (this affects the decimal point of the exported CSV)
2. The CSV file is expected to have been exported today (thus have today's date within its name, in `MM-DD-YYYY` format).

## Specifics when running on iOS
1. `INPUT_DIR`: The CSV to convert is expected to be in the iCloud drive, within the **Pythonista 3** folder.
2. You need to set `LIBRE_VIEW_USER` to your LibreView name within the [conversion script](./convert_LV_export.py). It's usually of the form **FirstnameLastname**.
   - Or make sure your LibreView name expands to **mobile** (by [setting](https://www1.libreview.com/Accounts/PatientUserSettings) _First Name_ to **mob** and _Last Name_ to **ile** for example).
3. `OUTPUT_DIR`: This will also be the **Pythonista 3** folder within your iCloud drive by default (it'd be a bit of a PITA to use local folders).

## Specifics when running on macOS
1. `INPUT_DIR`: The CSV to convert is expected to in the `Downloads` folder in your home directory.
2. `OUTPUT_DIR`: This will be the **Pythonista 3** folder within your iCloud drive by default. Set to something else if you like.

## Then export, convert and import your data
1. Export your blood sugar levels from LibreView, by clicking **Export Patient's Glucose Data** in the bottom right of [your measurements](https://www1.libreview.com/Dashboard/MyMeasurements), to the `INPUT_DIR` as per above.
2. Run the conversion script [`convert_LV_export.py`](./convert_LV_export.py) on a device of your choice.
   - You could use [Pythonista 3](https://omz-software.com/pythonista/) to run the conversion script on your iPhone.
   - To run it on a Mac, `cd` to the script's directory and run it with `./convert_LV_export`
     - You may need to install `python3`, for example with [Homebrew](https://brew.sh).
3. Use [Health CSV Importer](https://lionheartsw.com/software/health-csv-importer/) on your iPhone to import the converted CSV (named `YYYY-MM-DD_blood_glucose.csv` in the `OUTPUT_DIR` of your choice) into the Apple Health app.

## Limitations
- The conversion script does not remember the last exported data point, and will always convert the full set.
  - The importer will remind you to delete previously imported data before importing a new full set, as you'd get duplicate data in Apple Health otherwise.
