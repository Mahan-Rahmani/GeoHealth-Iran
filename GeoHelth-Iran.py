import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patheffects 

# Part 1: Data definition
data = [
    {"province": "Tehran", "pop": 13267637, "bed_count": 32700, "bed_per_capita": 2.46, "lat": 35.68, "lon": 51.38},
    {"province": "Razavi Khorasan", "pop": 6435501, "bed_count": 12380, "bed_per_capita": 1.92, "lat": 36.29, "lon": 59.61},
    {"province": "Isfahan", "pop": 5120850, "bed_count": 9575, "bed_per_capita": 1.86, "lat": 32.65, "lon": 51.66},
    {"province": "West Azerbaijan", "pop": 3265219, "bed_count": 5189, "bed_per_capita": 1.58, "lat": 37.56, "lon": 45.00},
    {"province": "East Azerbaijan", "pop": 3909652, "bed_count": 7835, "bed_per_capita": 2.01, "lat": 38.08, "lon": 46.37},
    {"province": "Khuzestan", "pop": 4710509, "bed_count": 7695, "bed_per_capita": 1.63, "lat": 31.32, "lon": 48.30},
    {"province": "Fars", "pop": 4851274, "bed_count": 11976, "bed_per_capita": 2.46, "lat": 29.61, "lon": 52.54},
    {"province": "Gilan", "pop": 2530696, "bed_count": 5004, "bed_per_capita": 1.97, "lat": 37.20, "lon": 49.59},
    {"province": "Mazandaran", "pop": 3283582, "bed_count": 5686, "bed_per_capita": 1.73, "lat": 36.56, "lon": 53.07},
    {"province": "Kurdistan", "pop": 1603011, "bed_count": 2300, "bed_per_capita": 1.43, "lat": 35.30, "lon": 47.00},
    {"province": "Kermanshah", "pop": 1195243, "bed_count": 3454, "bed_per_capita": 2.88, "lat": 34.31, "lon": 47.09},
    {"province": "Alborz", "pop": 2712400, "bed_count": 2421, "bed_per_capita": 0.89, "lat": 35.70, "lon": 50.95},
    {"province": "Hamedan", "pop": 1738234, "bed_count": 3199, "bed_per_capita": 1.84, "lat": 34.80, "lon": 48.51},
    {"province": "Lorestan", "pop": 1760649, "bed_count": 2721, "bed_per_capita": 1.54, "lat": 33.87, "lon": 48.35},
    {"province": "Sistan and Baluchestan", "pop": 2775014, "bed_count": 2613, "bed_per_capita": 0.94, "lat": 30.47, "lon": 60.86},
    {"province": "Kerman", "pop": 3164718, "bed_count": 4641, "bed_per_capita": 1.46, "lat": 30.29, "lon": 56.31},
    {"province": "Qom", "pop": 1292283, "bed_count": 2260, "bed_per_capita": 1.74, "lat": 34.64, "lon": 50.87},
    {"province": "Zanjan", "pop": 1057461, "bed_count": 2547, "bed_per_capita": 2.40, "lat": 36.67, "lon": 48.48},
    {"province": "Yazd", "pop": 1138533, "bed_count": 2885, "bed_per_capita": 2.53, "lat": 31.90, "lon": 54.37},
    {"province": "Golestan", "pop": 1868819, "bed_count": 2821, "bed_per_capita": 1.50, "lat": 36.83, "lon": 54.43},
    {"province": "Ardabil", "pop": 1270420, "bed_count": 2550, "bed_per_capita": 2.00, "lat": 38.24, "lon": 48.30},
    {"province": "Qazvin", "pop": 1273761, "bed_count": 2301, "bed_per_capita": 1.80, "lat": 36.27, "lon": 49.99},
    {"province": "Semnan", "pop": 702360, "bed_count": 2034, "bed_per_capita": 2.89, "lat": 35.57, "lon": 54.37},
    {"province": "Ilam", "pop": 580158, "bed_count": 998, "bed_per_capita": 1.72, "lat": 33.64, "lon": 46.43},
    {"province": "Chaharmahal and Bakhtiari", "pop": 947763, "bed_count": 1435, "bed_per_capita": 1.51, "lat": 32.32, "lon": 50.86},
    {"province": "Kohgiluyeh and Boyer-Ahmad", "pop": 713052, "bed_count": 805, "bed_per_capita": 1.12, "lat": 30.67, "lon": 51.55},
    {"province": "Bushehr", "pop": 1163400, "bed_count": 1471, "bed_per_capita": 1.26, "lat": 28.97, "lon": 50.84},
    {"province": "Hormozgan", "pop": 1776415, "bed_count": 2207, "bed_per_capita": 1.24, "lat": 27.17, "lon": 56.27},
    {"province": "North Khorasan", "pop": 863092, "bed_count": 1083, "bed_per_capita": 1.25, "lat": 37.45, "lon": 57.33},
    {"province": "South Khorasan", "pop": 768898, "bed_count": 925, "bed_per_capita": 1.20, "lat": 33.89, "lon": 59.22},
    {"province": "Arak", "pop": 1429475, "bed_count": 2324, "bed_per_capita": 1.62, "lat": 34.09, "lon": 49.70},
]

df = pd.DataFrame(data)

# Part 2: Reading Shapefile, merging, and plotting
try:
    shapefile_path = "iran_provinces_new.shp" # Your shapefile name
    provinces_gdf = gpd.read_file(shapefile_path)

    # !!! Important: Use the correct column name here !!!
    # This column in your shapefile must contain the province names.
    # e.g., 'name_provi', 'NAME_ Provinsi', ' استان', etc.
    column_with_province_names = 'name_provi' 

    # Merge data
    merged_gdf = provinces_gdf.merge(df, left_on=column_with_province_names, right_on='province', how='left')

    # Check merge results
    print(f"Total geometries in shapefile: {len(provinces_gdf)}")
    print(f"Rows after merge: {len(merged_gdf)}")
    
    if 'province' in merged_gdf.columns:
        unmapped_count = merged_gdf['province'].isna().sum()
        print(f"Number of provinces with no matching data: {unmapped_count}")
        if len(merged_gdf) > 0:
            mapped_count = len(merged_gdf) - unmapped_count
            print(f"Percentage of provinces with matching data: {(mapped_count / len(merged_gdf)) * 100:.2f}%")
        else:
            print("No data to calculate merge percentage.")
    else:
        print("Province column not found after merge. Merge likely failed.")
        unmapped_count = len(merged_gdf)

    # ----- Plotting -----
    fig, ax = plt.subplots(1, 1, figsize=(8, 7)) # Map size

    # Plot choropleth map
    merged_gdf.plot(column='bed_per_capita', ax=ax, legend=True,
                    legend_kwds={'label': "Hospital beds per 1,000 people", 'orientation': "horizontal"},
                    cmap='viridis', 
                    missing_kwds={'color': 'lightgrey', 'label': 'Data Unavailable'}
                   )

    # Add province labels on the map
    for idx, row in merged_gdf.iterrows():
        if not row.geometry.is_empty:
            point = row.geometry.representative_point()
            province_name = row['province'] 
            # Display text with outline for better readability
            plt.text(
                point.x, point.y,
                province_name,
                ha='center', 
                va='center', 
                fontsize=5,  
                color='white', 
                weight='bold', 
                path_effects=[plt.matplotlib.patheffects.withStroke(linewidth=1.5, foreground='black')] 
            )

    # Plot province borders
    provinces_gdf.plot(ax=ax, facecolor='none', edgecolor='black', linewidth=0.8, zorder=2)

    ax.set_title('Per Capita Bed Count in Iranian Provinces', fontsize=16)
    ax.set_axis_off() # Turn off axes


    # ----- Plotting Combined Bar and Line Chart -----
    fig2, ax2 = plt.subplots(1, figsize=(8, 7)) # Larger size for chart

    # Twin axis for beds
    ax3 = ax2.twinx()
    color_line = 'tab:blue'
    ax3.set_ylabel('Number of Beds', color=color_line)
    ax3.plot(df['province'], df['bed_count'], color=color_line, marker='o', linewidth=2, label='Beds')
    ax3.tick_params(axis='y', labelcolor=color_line)
    ax3.grid(axis='y', linestyle='--', alpha=0.6) # Grid for bed axis

    # Primary axis for population
    color_bar = 'tab:red'
    ax2.set_xlabel('Province', fontsize=12)
    ax2.set_ylabel('Population', color=color_bar, fontsize=12)
    ax2.bar(df['province'], df['pop'], color=color_bar, alpha=0.5, label='Population')
    ax2.tick_params(axis='y', labelcolor=color_bar)
    ax2.set_xticks(range(len(df['province']))) 
    ax2.set_xticklabels(df['province'], rotation=90, ha='center') # Rotate labels

    # Grid for population axis
    ax2.grid(axis='y', linestyle=':', alpha=0.7)

    ax2.set_title('Population vs. Bed Count by Province', fontsize=16)

    # Final adjustments and display
    fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout for map title
    fig2.tight_layout() # Adjust layout for combined chart
    plt.show()

except FileNotFoundError:
    print(f"Error: File '{shapefile_path}' not found.")
    print("Please ensure the shapefile (including .shp, .shx, .dbf, .prj files) is in the correct directory.")
    print("Make sure the filename is exactly 'iran_provinces_new.shp'.")
except KeyError as e:
    print(f"Error: Province name column ('{column_with_province_names}') not found in shapefile or DataFrame.")
    print(f"Key error: {e}")
    print(f"Please verify and update the 'column_with_province_names' variable with the correct column name from your shapefile.")
except Exception as e:
    print(f"An unexpected error occurred during shapefile processing or plotting: {e}")