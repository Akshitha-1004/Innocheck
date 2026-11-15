def predict_category(text):

    text = text.lower()

    categories = {

        "Agriculture":[
            "crop",
            "farm",
            "irrigation",
            "soil"
        ],

        "Healthcare":[
            "medical",
            "patient",
            "disease",
            "hospital"
        ],

        "Energy":[
            "battery",
            "solar",
            "power",
            "energy"
        ],

        "Robotics":[
            "robot",
            "autonomous",
            "navigation"
        ],

        "IoT":[
            "sensor",
            "iot",
            "monitoring"
        ]

    }

    scores = {}

    for category, words in categories.items():

        scores[category] = sum(
            word in text
            for word in words
        )

    return max(
        scores,
        key=scores.get
    )