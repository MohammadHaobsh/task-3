def mood_tracker():
    print("Welcome to the Mood Tracker!")
    print("Please choose your mood from the following options:")
    print("1. Happy")
    print("2. Sad")
    print("3. Stressed")
    print("4. Relaxed")
    print("5. Energetic")
    
    allowed_moods = {
        "1": "happy",
        "2": "sad",
        "3": "stressed",
        "4": "relaxed",
        "5": "energetic",
        "happy": "happy",
        "sad": "sad",
        "stressed": "stressed",
        "relaxed": "relaxed",
        "energetic": "energetic"
    }
    
    positive_moods = ["Happy", "Relaxed", "Energetic"]
    negative_moods = ["Sad", "Stressed"]
    
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    mood_log = []

    # Collect mood input for each day
    for day in days_of_week:
        while True:
            mood_input = input(f"How do you feel on {day}? ").strip().lower()
            if mood_input in allowed_moods:
                mood_log.append(allowed_moods[mood_input].capitalize())
                break
            else:
                print("Invalid input. Please choose a number (1-5) or a word from the options: happy, sad, stressed, relaxed, energetic.")
    
    # Count occurrences of each mood
    mood_counts = {mood.capitalize(): 0 for mood in allowed_moods.values() if mood in allowed_moods.values()}
    for mood in mood_log:
        mood_counts[mood] += 1

    # Print mood breakdown
    print("\nMood Breakdown for the Week:")
    total_days = len(days_of_week)
    for mood, count in mood_counts.items():
        percentage = (count / total_days) * 100
        print(f"{mood}: {percentage:.2f}%")

    # Count occurrences of positive and negative moods
    positive_count = sum(1 for mood in mood_log if mood in positive_moods)
    negative_count = sum(1 for mood in mood_log if mood in negative_moods)

    # Determine the dominant group and the most frequent mood within it
    if positive_count > negative_count:
        print("\nThe overall mood for the next week is expected to be positive. 🌞")
        # Determine the most frequent positive mood
        positive_mood_counts = {mood: mood_log.count(mood) for mood in positive_moods}
        most_frequent_positive = max(positive_mood_counts, key=positive_mood_counts.get)
        if most_frequent_positive == "Happy":
            print("Next week is expected to be a joyful and positive week! 🌞")
        elif most_frequent_positive == "Relaxed":
            print("Next week looks calm and balanced. Take it easy and enjoy the moments! 🌿")
        elif most_frequent_positive == "Energetic":
            print("Next week is full of energy and potential. Use this momentum to achieve your goals! ⚡")
    elif negative_count > positive_count:
        print("\nThe overall mood for the next week is expected to be negative. 🌧️")
        # Determine the most frequent negative mood
        negative_mood_counts = {mood: mood_log.count(mood) for mood in negative_moods}
        most_frequent_negative = max(negative_mood_counts, key=negative_mood_counts.get)
        if most_frequent_negative == "Sad":
            print("Next week might feel a bit heavy. Remember to take care of yourself and seek support if needed. 🌧️")
        elif most_frequent_negative == "Stressed":
            print("Next week could be challenging. Prioritize your tasks and don't forget to rest. 💼")
    else:
        print("\nThe mood for the next week is balanced between positive and negative feelings. Take it one day at a time. 🌤️")

    print("\nThank you for using the Mood Tracker!")

# Run the Mood Tracker
mood_tracker()
