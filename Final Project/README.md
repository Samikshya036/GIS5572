# Minnesota Corn Growers App
![GitHub last commit](https://img.shields.io/github/last-commit/TzuYuMa/Corn?style=for-the-badge)

## Overview  
This app aims to provide Minnesota corn growers with updated information on growing degree days (AGDD), soil moisture, and reference evapotranspiration (ET). Selecting the desire area to download data with CSV or PDF file, or you can find the [Data URLs for GeoJson](#data-urls-for-geojson) Utilizing GeoJSON format from APIs. This supports agricultural decision-making in Minnesota by facilitating the comparison of various models for accurate analysis.

## Objectives  
- Develop a system to calculate and map AGDD, ET, and soil moisture for Minnesota Corn Growers.
- Utilize local and cloud computing to automate data processing from collection through spatial visualization via ArcOnline.
- Ensure data accuracy and seamless integration of varied datasets within a PostgreSQL database.
- Maintain user-friendly access and support real-time updates.

## Data Sources 
- **IEM**: Daily Min/Max temperature data, Minnesota.
- **NASA SMAP**: Soil Moisture, Minnesota.
- **TerraClimate**: Actual Evapotranspiration, Global.

## Data URLs for GeoJson
- AGDD: [AGDD Data URL](https://googlecloudrun-nvrttyom5q-uc.a.run.app/get_agdd_idw)
- ET: [ET Data URL]
- Soil Moisture:
  ```python
  https://googlecloudrun-nvrttyom5q-uc.a.run.app/get_soil_moisture_<date>

  Please manually replace `<date>` with the desired year and month in your browser's address bar

  Available date range: 20237-20244

  For example:
  
  ```plaintext
  https://googlecloudrun-nvrttyom5q-uc.a.run.app/get_soil_moisture_20237

## Contributors 
- Samikshya Subedi
- Tzu-Yu Ma  

