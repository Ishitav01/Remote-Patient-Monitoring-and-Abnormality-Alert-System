class HealthSuggestion:
    def __init__(self, user_data):
        """
        Initializes with user health data.
        :param user_data: Dictionary containing health data and preferences.
        """
        self.user_data = user_data

    def generate_suggestions(self):
        """
        Generate health suggestions based on user activity and health data.
        :return: List of suggestions.
        """
        suggestions = []
        inactivity_duration = self.user_data.get("inactivity_duration", 0)
        recent_fall = self.user_data.get("recent_fall", False)
        diet_preference = self.user_data.get("diet_preference", "balanced")

        if inactivity_duration > 300:
            suggestions.append("Consider taking a short walk or stretching exercises.")

        if recent_fall:
            suggestions.append("Please ensure you're in a safe environment. Consider using assistive devices.")

        if diet_preference == "balanced":
            suggestions.append("Include more fruits and vegetables in your diet today.")
        elif diet_preference == "vegetarian":
            suggestions.append("Ensure you're getting enough protein from plant-based sources.")
        elif diet_preference == "vegan":
            suggestions.append("Incorporate a variety of legumes and grains to meet your nutritional needs.")

        return suggestions
