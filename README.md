
# POTA GeoJSON Converter

This script converts a Parks on the Air (POTA) dataset from JSON format into a GeoJSON `FeatureCollection` format compatible with mapping applications (e.g., Leaflet, Mapbox).

It also supports filtering the parks based on U.S. state location codes (e.g., `US-GA` for Georgia) and saves the results to a file named with the corresponding filter suffix.

## 📁 Input

The script expects a file named `pota_in.json` in the same directory, structured like this:

```json
[
  {
    "reference": "US-0001",
    "name": "Acadia National Park",
    "latitude": 44.31,
    "longitude": -68.2034,
    "locationDesc": "US-ME"
  },
  ...
]
```

## ✅ Output

The script outputs a GeoJSON file with each park as a `Feature`. For example:

```json
{
  "type": "Feature",
  "properties": {
    "reference": "US-0001 - US-ME",
    "name": "Acadia National Park"
  },
  "geometry": {
    "type": "Point",
    "coordinates": [-68.2034, 44.31]
  }
}
```

Output is saved to:
- `parks_ALL.json` if no filter is specified
- `parks_US-GA.json` if filtered by `US-GA`

## 🚀 Usage

### Run without a filter (convert all parks):

```bash
python POTA_Conv.py
```

### Run with a state/location filter:

```bash
python POTA_Conv.py US-GA
```

This will output a file named `parks_US-GA.json` with only parks where `locationDesc` contains `US-GA`.

## 🛠 Requirements

- Python 3.x

## 📄 License

MIT License
