class ExpertSystem:
    def _init_(self, patient_symptoms):

        self.symptoms = patient_symptoms

        self.diseases = [
            {
                'name': 'Common Cold',
                'symptoms': ['fever', 'cough', 'runny_nose', 'sore_throat', 'fatigue'],
                'treatment': 'Get plenty of rest, stay hydrated, and take over-the-counter cold medication.',
            },
            {
                'name': 'Flu',
                'symptoms': ['fever', 'cough', 'fatigue', 'body_aches'],
                'treatment': 'Rest, drink fluids, and take antiviral medication if prescribed by a doctor.',
            },
            {
                'name': 'Chickenpox',
                'symptoms': ['fever', 'rash', 'itchiness', 'fatigue'],
                'treatment': 'Apply calamine lotion, take oatmeal baths, and avoid scratching the rash.',
            },
            {
                'name': 'Strep Throat',
                'symptoms': ['sore_throat', 'fever', 'swollen_glands'],
                'treatment': 'Take antibiotics as prescribed by a doctor, rest, and drink plenty of fluids.',
            },
            {
                'name': 'Gastroenteritis',
                'symptoms': ['vomiting', 'diarrhea', 'abdominal_pain'],
                'treatment': 'Stay hydrated, eat bland foods, and rest. Seek medical attention if symptoms worsen.',
            },
            {
                'name': 'Asthma',
                'symptoms': ['cough', 'wheezing', 'difficulty_breathing'],
                'treatment': 'Use inhalers as prescribed, avoid triggers, and seek medical help if symptoms worsen.',
            },
            {
                'name': 'Ear Infection',
                'symptoms': ['ear pain', 'fever', 'difficulty_sleeping'],
                'treatment': 'Take antibiotics as prescribed, apply warm compresses, and use over-the-counter pain relievers.',
            },
            {
                'name': 'Allergies',
                'symptoms': ['runny nose', 'sneezing', 'itchy_eyes', 'itchiness'],
                'treatment': 'Avoid allergens, take antihistamines, and use nasal sprays as prescribed.',
            },
            {
                'name': 'Measles',
                'symptoms': ['high_fever', 'cough', 'rash', 'sore_throat'],
                'treatment': 'Rest, stay hydrated, and take fever-reducing medication. Seek medical attention if complications arise.',
            },
            {
                'name': 'Hand, Foot, and Mouth Disease',
                'symptoms': ['fever', 'sore_throat', 'rash', 'blisters'],
                'treatment': 'Rest, stay hydrated, and use over-the-counter pain relievers. Avoid close contact with others to prevent spread.',
            },
            {
                'name': 'Diabetes',
                'symptoms': ['excessive_thirst', 'frequent_urination', 'fatigue', 'unexplained_weight_loss'],
                'treatment': 'Monitor blood sugar levels, adhere to a balanced diet, take insulin as prescribed, and exercise regularly.',
            },
            {
                'name': 'Paranasal Sinusitis',
                'symptoms': ['facial_pain', 'headache', 'nasal_congestion', 'cough'],
                'treatment': 'Use saline nasal sprays, apply warm compresses, take over-the-counter pain relievers, and stay hydrated.',
            },
            {
                'name': 'Diarrheal Diseases',
                'symptoms': ['abdominal_pain', 'diarrhea', 'vomiting', 'dehydration'],
                'treatment': 'Stay hydrated, eat bland foods, and avoid dairy and fatty foods. Seek medical attention if symptoms persist or worsen.'
            }
        ]

    def calculate_shared_symptoms(self, disease_symptoms):
        total_shared_severity = 0
        for symptom in disease_symptoms:
            if symptom in self.symptoms:
                total_shared_severity += self.symptoms[symptom]
        return total_shared_severity
    

    def diagnose_disease(self):
        max_shared_symptoms = 0
        likely_disease = None    
        for disease in self.diseases:
            shared_symptoms = self.calculate_shared_symptoms(disease["symptoms"])
            if shared_symptoms > max_shared_symptoms:
                max_shared_symptoms = shared_symptoms
                likely_disease = disease

        return {
            "name": likely_disease["name"],
            "treatment": likely_disease["treatment"],
        }

    def run(self):
        return self.diagnose_disease()

if __name__ == "__main__":
    data = {}
    expert_system = ExpertSystem(data)
    result = expert_system.run()
    print(result)
