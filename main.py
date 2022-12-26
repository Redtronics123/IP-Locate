import requests


class IpSearcher:
    def __init__(self):
        # enter your IP
        self.ip_adress = input("Please write the ip: ")

        # get request
        self._response = requests.get(f"http://ip-api.com/json/{self.ip_adress}").json()

        if self._response["status"] != "success":
            print("request failed")
            exit()

        # print all important results
        print("Results")
        print("The location: ", self._response["city"])
        print("Service: ", self._response["as"])
        print("Organisation: ", self._response["org"])
        print("Timezone: ", self._response["timezone"])


if __name__ == "__main__":
    IpSearcher()
