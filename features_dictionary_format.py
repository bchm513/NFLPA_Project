FEATURES_DICTIONARY_FORMAT = {

    # game level id that uniquely identifies a player given the specific game we are comparing
    "game_level_id" : {

        # 1. Player-Level Predictors (Baseline Risk Modifiers)
        "player_level": {
            "age": "",
            "nfl_experience": "",
            "position_group": "",
            "body_mass": "",
            "bmi": "",

            # Injury history -- list of prior injuries dicts
            "prior_injury": {
                "prior_injury_type": "",
                "prior_injury_recurrence": "",
                "games_missed_prior": ""
            },

            # Workload
            "career_workload": "",
            "total_career_snaps": "",

            # Roster / role
            "roster_status": "",  # active, inactive, practice_squad
            "starter_indicator": "",
            "rotational_indicator": "",
            "contract_year": ""
        },

        # 2. Travel & Circadian Stress Predictors
        "travel_circadian": {

            # Travel load
            "travel_distance_recent": "",
            "cumulative_travel_distance": "",

            # Time zones
            "time_zone_crossings": "",
            "net_time_zone_diff": "",
            "absolute_time_zones": "",
            "travel_direction": "",  # east_to_west / west_to_east

            # Circadian alignment
            "circadian_misalignment_index": "",
            "kickoff_body_clock_diff": "",

            # International travel
            "international_game": "",
            "international_country": "",
            "international_travel_direction": ""
        },

        # Environmental Stress
        "environmental": {
            "temperature": "",
            "temperature_delta": "",
            "humidity": "",
            "wind_speed": "",
            "indoor_stadium": "",

            # Altitude
            "stadium_altitude": "",
            "altitude_change": ""
        }
    }
}
