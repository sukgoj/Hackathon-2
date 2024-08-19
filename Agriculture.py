class CropAndSoilManagementSystem:
    def __init__(self):
        self.crops_data = {
            'Wheat': {'soil_type': 'loamy', 'pH': (6.0, 7.5), 'climate': 'temperate'},
            'Rice': {'soil_type': 'clay', 'pH': (5.0, 6.5), 'climate': 'tropical'},
            'Maize': {'soil_type': 'sandy', 'pH': (5.5, 7.0), 'climate': 'warm'},
            
        }

    def recommend_crop(self, soil_type, pH, climate):
        recommendations = []
        for crop, details in self.crops_data.items():
            if details['soil_type'] == soil_type and details['pH'][0] <= pH <= details['pH'][1] and details['climate'] == climate:
                recommendations.append(crop)
        return recommendations if recommendations else ["No suitable crops found."]

    def analyze_soil(self, pH, moisture):
        if pH < 5.5:
            return "Soil is too acidic. Consider liming."
        elif pH > 7.5:
            return "Soil is too alkaline. Consider adding sulfur."
        elif moisture < 20:
            return "Soil moisture is low. Consider irrigation."
        else:
            return "Soil is in good condition."

    def identify_disease(self, crop, symptoms):
        
        if crop == 'Wheat' and 'yellow' in symptoms:
            return "Possible Yellow Rust. Use appropriate fungicide."
        elif crop == 'Rice' and 'brown' in symptoms:
            return "Possible Brown Spot. Use fungicide and improve drainage."
        
        return "No disease identified."

    def seasonal_advice(self, season):
        if season == 'Spring':
            return "Ideal for planting warm-season crops."
        elif season == 'Summer':
            return "Ensure regular irrigation and monitor for pests."
        elif season == 'Autumn':
            return "Prepare for harvest and consider cover crops."
        elif season == 'Winter':
            return "Focus on soil health and plan for next season."
        return "No advice available for this season."



def main():
    system = CropAndSoilManagementSystem()
    
    
    soil_type = 'loamy'
    pH = 6.8
    climate = 'temperate'
    crop = 'Wheat'
    symptoms = ['yellow']
    season = 'Spring'
    moisture = 25
    
    
    crop_recommendations = system.recommend_crop(soil_type, pH, climate)
    soil_analysis = system.analyze_soil(pH, moisture)
    disease_info = system.identify_disease(crop, symptoms)
    seasonal_advice = system.seasonal_advice(season)
    
    
    print("Crop Recommendations:", crop_recommendations)
    print("Soil Analysis:", soil_analysis)
    print("Disease Identification:", disease_info)
    print("Seasonal Advice:", seasonal_advice)

if __name__ == "__main__":
    main()
