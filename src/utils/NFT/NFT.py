from NFT_collection_classes import NFT_scraper_get_collection_activity
from NFT_user_classes import NFT_scraper_user_class


class NFT_scraper(NFT_scraper_get_collection_activity, NFT_scraper_user_class):

    def __init__(self) -> None:
        super().__init__()

    # NFT collection methods
    def get_collection_activity(self,
                                collection_id: str,
                                limit: int = 20) -> list:
        return super().get_activity(collection_id, limit)

    # NFT user methods
    def get_user_details(self, user_address: str) -> dict:
        return super().get_user_details(user_address)

    def get_user_gallery(self, user_address: str, limit: int = 20) -> list:
        return super().get_user_gallery(user_address, limit)

    def get_user_collection(self, user_address: str, limit: int = 20) -> list:
        return super().get_user_collection(user_address, limit)

    def get_user_activity(self, user_address: str, limit: int = 20) -> list:
        return super().get_user_activity(user_address, limit)


my_NFT_scraper = NFT_scraper()
print(
    my_NFT_scraper.get_user_gallery(
        user_address="0x41e22215f10634893c3231ec9562054bca9d2d74"))
print('------------------------------------------------------------')
print(
    my_NFT_scraper.get_user_collection(
        user_address="0x41e22215f10634893c3231ec9562054bca9d2d74"))
print('------------------------------------------------------------')
print(
    my_NFT_scraper.get_user_details(
        user_address="0x41e22215f10634893c3231ec9562054bca9d2d74"))
print('------------------------------------------------------------')
print(
    my_NFT_scraper.get_user_activity(
        user_address="0x41e22215f10634893c3231ec9562054bca9d2d74"))

# api = "https://api.nftbase.com/web/api/v1/user/gallery?user_id=4337377&offset=0&limit=30"
# response = requests.get(api)
# print(response.json())