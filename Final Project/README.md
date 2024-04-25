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

  <select id="dateSelect">
    <option value="20237">20237</option>
    <option value="20238">20238</option>
    <option value="20239">20239</option>
    <option value="202310">202310</option>
    <option value="202311">202311</option>
    <option value="202312">202312</option>
    <option value="20241">20241</option>
    <option value="20242">20242</option>
    <option value="20243">20243</option>
    <option value="20244">20244</option>
  </select>

  <button onclick="generateURL()">Generate URL</button>

  <p id="generatedURL"></p>

  <script>
    function generateURL() {
      var selectedDate = document.getElementById("dateSelect").value;
      var baseURL = "https://googlecloudrun-nvrttyom5q-uc.a.run.app/get_soil_moisture_";
      var url = baseURL + selectedDate;
      document.getElementById("generatedURL").textContent = "Generated URL: " + url;
    }
  </script>



## Contributors 
- Samikshya Subedi
- Tzu-Yu Ma  

