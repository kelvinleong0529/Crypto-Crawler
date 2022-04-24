import requests


class gamefi_scraper:

    def __init__(self) -> None:
        pass

    def __get_value(self, input_dict: dict, key: str) -> str:
        if isinstance(input_dict, dict):
            return str(input_dict[key]) if key in input_dict else "N/A"
        return "N/A"

    def __search_by_category(self, category: str) -> list:
        page_index = 1
        token_detail_list = []
        while True:
            api = "https://v2.gamefi.org/_next/data/05TfXTSF5_7vpLam60k8c/hub.json?category={category}&page={page_index}".format(
                category=category, page_index=page_index)
            response = requests.get(api)
            if str(response.status_code) == "200":
                data = response.json()["pageProps"]["data"]
                if page_index == data["lastPage"]:
                    break
                data = data["data"]
                for index, token_iterator in enumerate(data):
                    # initialize a dict to store the details
                    token = {}

                    # gamefi token details
                    token["game_name"] = self.__get_value(
                        token_iterator, "game_name")
                    token["verified"] = self.__get_value(
                        token_iterator, "verified")
                    token["network"] = self.__get_value(
                        token_iterator, "network_available")
                    token["address"] = self.__get_value(
                        token_iterator, "token_address")
                    token["category"] = self.__get_value(
                        token_iterator, "category")
                    token["developer"] = self.__get_value(
                        token_iterator, "developer")
                    token["language"] = self.__get_value(
                        token_iterator, "language")
                    token["description"] = self.__get_value(
                        token_iterator, "short_description")

                    # gamefi token IGO info
                    token["igo_price"] = self.__get_value(
                        token_iterator, "token_price")
                    token["igo_roi"] = self.__get_value(token_iterator, "roi")

                    # gamefi token pricing info
                    token["price"] = self.__get_value(token_iterator, "price")
                    token["price_change_24h"] = self.__get_value(
                        token_iterator, "price_change_24h")
                    token["price_change_7d"] = self.__get_value(
                        token_iterator, "price_change_7d")
                    token["volume_24h"] = self.__get_value(
                        token_iterator, "volume_24h")
                    token["market_cap"] = self.__get_value(
                        token_iterator, "market_cap")

                    # gamefi important links and URL
                    token["official_website_link"] = self.__get_value(
                        token_iterator, "official_website")
                    token["web_game_link"] = self.__get_value(
                        token_iterator, "web_game_link")
                    token["android_link"] = self.__get_value(
                        token_iterator, "android_link")
                    token["ios_link"] = self.__get_value(
                        token_iterator, "ios_link")
                    token["game_pc_link"] = self.__get_value(
                        token_iterator, "game_pc_link")

                    # gamefi token social media info
                    token["twitter"] = self.__get_value(
                        token_iterator, "twitter_link")
                    token["medium"] = self.__get_value(token_iterator,
                                                       "medium_link")
                    token["discord"] = self.__get_value(
                        token_iterator, "discord_link")
                    token["telegram"] = self.__get_value(
                        token_iterator, "official_telegram_link")

                    # gamefi Coin Market Cap info
                    token["cmc_id"] = self.__get_value(token_iterator,
                                                       "cmc_id")
                    token["cmc_slug"] = self.__get_value(
                        token_iterator, "official_telegram_link")
                    token["cmc_rank"] = self.__get_value(
                        token_iterator, "official_telegram_link")


api = "https://v2.gamefi.org/_next/data/05TfXTSF5_7vpLam60k8c/hub.json?category={category}".format(
    category="Metaverse")
response = requests.get(api)
print(response.json()["pageProps"]["data"]["page"],
      response.json()["pageProps"]["data"]["lastPage"])
