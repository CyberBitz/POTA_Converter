import json
import sys

def run_conversion(filter_state=None):
    # Load the input JSON
    with open("sd.json", "r") as f:
        data = json.load(f)

    # Create GeoJSON structure
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for park in data:
        if filter_state and filter_state not in park["locationDesc"]:
            continue

        feature = {
            "type": "Feature",
            "properties": {
                "reference": f"{park['reference']} - {park['locationDesc']}",
                "name": park["name"]
            },
            "geometry": {
                "type": "Point",
                "coordinates": [park["longitude"], park["latitude"]]
            }
        }
        geojson["features"].append(feature)

    # Determine output filename
    suffix = f"_{filter_state}" if filter_state else "_ALL"
    output_path = f"parks_out{suffix}.json"

    # Write the GeoJSON to file
    with open(output_path, "w") as f:
        json.dump(geojson, f, indent=2)

    print(f"Saved to {output_path}")

if __name__ == "__main__":
    filter_arg = sys.argv[1] if len(sys.argv) > 1 else None
    run_conversion(filter_arg)
