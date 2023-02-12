from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        #self.client.get("/world")


#if __name__ == '__main__':
    #fun = HelloWorldUser
    #fun.hello_world()