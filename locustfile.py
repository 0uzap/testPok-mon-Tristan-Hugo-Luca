from locust import HttpUser, between, task

class Scenario(HttpUser):
    # Temps de pause entre les requêtes
    wait_time = between(1, 7)

    def on_start(self):
        self.nbTrainer = 0
        self.id_trainer1 = None

    @task
    def index(self):
        response = self.client.get("/trainers")
        if response.status_code == 200:
            self.nbTrainer = len(response.json())
        else:
            print("Erreur lors de la récupération des trainers")

        response = self.client.post("/trainers/", json={"name": "lucas", "birthdate": "2022-11-11"})
        
        if response.status_code == 201:
            self.id_trainer1 = response.json().get("id")
            print(f"Trainer créé avec ID: {self.id_trainer1}")
        else:
            print("Erreur lors de la création du trainer")
