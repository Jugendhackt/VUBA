# Parameters
  - Coordinates
    - Lat:float
    - Long:float
  - Limit:int (optional implementation)
  
# Return
  - [] Bikes
    - Coordinates
      - Lat:float
      - Lon:float
    - Provider: string
    - Accuracy: float (use 0.0 if unknown)
    - AdditionalInfo: string (Supports Markdown)
    - BikeID: string
    - IsStationary: bool
    - StationID: string