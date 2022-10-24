from django.test import SimpleTestCase


class TestHelloView(SimpleTestCase):
    def test_hello_world(self):
        response = self.client.get("/hello/")
        self.assertContains(response, "Hello World!")

    # def test_hello_nate(self):
    #     response = self.client.get("/hello/nate/")
    #     self.assertContains(response, "Hello, nate")

    # def test_hello_Brittany(self):
    #     response = self.client.get("/hello/Brittany/")
    #     self.assertContains(response, "Hello, Brittany")

    # def test_hello_Ethan(self):
    #     response = self.client.get("/hello/Ethan/")
    #     self.assertContains(response, "Hello, Ethan")


# class TestRollView(SimpleTestCase):
#     def test_roll_die_view(self):
#         response = self.client.get("/roll-die/9/")
#         self.assertLessEqual(response, "...")

# class TestRandomBetweenView(SimpleTestCase):
#     def test_random_between(self):
#         response = self.client.get("random-between/<int:lo>/<int:hi>/")
#         self.assertContains(response, "...")
