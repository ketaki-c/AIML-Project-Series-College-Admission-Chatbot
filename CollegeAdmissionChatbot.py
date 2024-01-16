class CollegeAdmissionChatbot:
    def __init__(self):
        self.context = {}

    def admission_related_qa(self, user_input):
        if "procedure" in user_input.lower():
            return "The admission procedure typically involves submitting an application, transcripts, and any required test scores. It may also include an interview."
        elif "requirements" in user_input.lower():
            return "Admission requirements vary, but commonly include academic transcripts, standardized test scores, letters of recommendation, and a personal statement."
        elif "deadlines" in user_input.lower():
            return "Admission deadlines depend on the college. It's crucial to check the official website for the specific deadlines for application submission."
        else:
            return None  # Indicate that the chatbot cannot answer the query.

    def engage_user(self):
        print("Welcome to the College Admission Chatbot! How can I help you with your admission queries?")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() in ["bye", "goodbye"]:
                print("Thank you for chatting with the College Admission Chatbot. Goodbye!")
                break
            
            admission_response = self.admission_related_qa(user_input)
            
            if admission_response:
                print("Bot:", admission_response)
                self.context[user_input.lower()] = admission_response
            else:
                print("Bot: I'm sorry, I don't have information on that. Please ask another admission-related question.")

    def run(self):
        self.engage_user()

if __name__ == "__main__":
    admission_chatbot = CollegeAdmissionChatbot()
    admission_chatbot.run()
