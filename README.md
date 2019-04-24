# LibreView_to_AppleHealth_converter
Converts a CSV export of blood sugar levels from [LibreView](https://libreview.com) into a format that can be imported into the Apple Health app with [Health CSV Importer](https://lionheartsw.com/software/health-csv-importer/).

## First, configure the script so it works for you
1. Set the `LV_USER` constant to your LibreView name, usually something like **FirstnameLastname**.
2. Adjust `BASE_DIR` to your liking.
   - I'm using [Pythonista 3](https://omz-software.com/pythonista/) to run the conversion script on my iPhone, but you could just as easily run it somewhere else.
   - Because the [LibreView](https://libreview.com) site sucks on mobile devices, I tend to export the data on my Mac. That's why I'm using an iCloud folder.

## Then export, convert and import your data
1. Export your blood sugar levels from LibreView, by clicking **Export Patient's Glucose Data** in the bottom right of [your measurements](https://www1.libreview.com/Dashboard/MyMeasurements), to the specified **IN** directory.
2. Run the conversion script on a device of your choice.
3. Use [Health CSV Importer](https://lionheartsw.com/software/health-csv-importer/) to import the converted data in the **OUT** folder into the Apple Health app.

## Limitations
- Exported data is expected to be in mmol/L and will be exported as such.
- The conversion script does not remember the last exported data point, and will always export the full set.
  - The importer will remind you to delete previously imported data before importing a new full set, as you'd get duplicate data in Apple Health otherwise.
