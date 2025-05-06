import re


class MentalHealthChatbot:
    def __init__(self):
        # Define response patterns (keyword: response)
        self.responses = {
            r'\b(sad|depressed|down|low)\b': [
                "I'm really sorry you're feeling this way. It’s okay to feel sad sometimes. Would you like to share more or try a breathing exercise?",
                "It sounds tough right now. Maybe writing down your thoughts or talking to someone you trust could help. I'm here for you."
            ],
            r'\b(anxious|worried|nervous|panic)\b': [
                "Anxiety can feel overwhelming, but you're not alone. Try taking slow, deep breaths for a minute. Want to talk about what's on your mind?",
                "It’s okay to feel anxious. Let’s focus on something calming—maybe visualize a peaceful place. What do you think?"
            ],
            r'\b(stressed|overwhelmed|pressure)\b': [
                "Stress can pile up, can’t it? Maybe take a moment to pause and do something small you enjoy. What helps you unwind?",
                "It sounds like a lot is going on. Breaking things into smaller steps might help. Want to share what’s stressing you out?"
            ],
            r'\b(happy|good|great)\b': [
                "That’s awesome to hear! What’s got you in such a great mood today?",
                "Love the positive vibes! What’s making you smile right now?"
            ],
            r'\b(thanks|thank you)\b': [
                "You’re very welcome! I'm here whenever you need me.",
                "No problem at all! Glad I could help."
            ]
        }
        # Fallback response for unrecognized messages
        self.fallback_responses = [
            "I’m here for you. Could you share a bit more about how you’re feeling?",
            "It sounds like you’ve got a lot on your mind. Want to talk it out?"
        ]

    def get_response(self, message):
        # Convert message to lowercase for matching
        message = message.lower().strip()

        # Check each pattern
        for pattern, responses in self.responses.items():
            if re.search(pattern, message, re.IGNORECASE):
                return responses[0]  # Return first matching response (can randomize if desired)

        # Return a fallback response if no patterns match
        return self.fallback_responses[0]