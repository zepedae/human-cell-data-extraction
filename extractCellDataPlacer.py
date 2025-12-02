# This program reads cell_ids and data ranges from "Placer1_uniques_cells_and_dates.csv" and 
# input in Placer to extract human cell phone activity data
""" 1. Organize location data according to date and location with raster cells
2. Copy 8 cell ids that need extracting in same time frame 
    (e.g., locations were recorded within 1 week of each other)
3. Open Placer "https://analytics.placer.ai/explore"
4. In search bar enter first cell_id str("Cell ID " + cell_id) and search
5. Click "Add competitor" and enter Cell ID for the remaining 7 cell_ids
6. Add correct date range
    a. click "Last full 12 months"
    b. click "Date range"
    c. enter start date
    d. enter end date
    e. click "Apply"
7. Select "All visit durations"
8. "Add filter" should already be on visitors only
9. Download "Hourly visits"
10. Restart with search bar until all cell_ids have been extracted
 """
# activate virtual environment: source venv/bin/activate

import pandas as pd

df = pd.read_excel("Placer1_unique_cells_and_dates.xls")