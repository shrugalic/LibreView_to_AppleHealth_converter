# LibreView_to_AppleHealth_converter
Converts a CSV export of blood sugar levels from [LibreView](https://libreview.com) into a format that can be imported into the Apple Health app with [Health CSV Importer](https://lionheartsw.com/software/health-csv-importer/).

## First, configure the script so it works for you
1. Set the `LV_USER` constant to your LibreView name, usually of the form **FirstnameLastname**.
2. Adjust `BASE_DIR` to your liking.
   - Because the [LibreView](https://libreview.com) site sucks on mobile devices, I tend to export the data on my Mac. That's why I'm using an iCloud folder.
3. `ICLOUD_DIR` is configured to work on an iPhone.
   - To run it on a Mac, uncomment the appropriate `ICLOUD_DIR`.
4. Imported data is expected to be in **mmol/L** and will be exported as such.
   - If you'd prefer to use **mg/dL** for import and export, just set the relevant header name to **Blood Glucose (mg/dL)**.

## Then export, convert and import your data
1. Export your blood sugar levels from LibreView, by clicking **Export Patient's Glucose Data** in the bottom right of [your measurements](https://www1.libreview.com/Dashboard/MyMeasurements), to the specified **IN** directory.
2. Run the conversion script [`convert_LV_export.py`](./convert_LV_export.py) on a device of your choice.
   - I'm using [Pythonista 3](https://omz-software.com/pythonista/) to run the conversion script on my iPhone.
   - To run it on a Mac instead, `cd` to the script's directory and run it with `./convert_LV_export`
     - You may need to install `python3`, for example with [Homebrew](https://brew.sh).
3. Use [Health CSV Importer](https://lionheartsw.com/software/health-csv-importer/) to import the converted data in the **OUT** folder into the Apple Health app.

## Limitations
- The conversion script does not remember the last exported data point, and will always convert the full set.
  - The importer will remind you to delete previously imported data before importing a new full set, as you'd get duplicate data in Apple Health otherwise.
