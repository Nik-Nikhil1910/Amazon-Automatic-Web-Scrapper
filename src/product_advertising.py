import boto3
from botocore.exceptions import BotoCoreError, ClientError
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY

# Initialize the Amazon Product Advertising API client
def initialize_client():
    return boto3.client(
        "product-advertising",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name="us-east-1"
    )

# Get product details for an ASIN
def get_product_details(client, asin):
    try:
        response = client.get_items(
            ItemIds=[asin],
            Resources=[
                "ItemInfo.Title",
                "ItemInfo.Features",
                "ItemInfo.ContentInfo",
                "Offers.Listings.Price",
                "Offers.Listings.Availability.Message",
                "Offers.Listings.DeliveryInfo.IsPrimeEligible"
            ]
        )
        
        if "ItemsResult" not in response or not response["ItemsResult"]["Items"]:
            return {"ASIN": asin, "Status": "Unavailable"}

        item = response["ItemsResult"]["Items"][0]
        title = item.get("ItemInfo", {}).get("Title", {}).get("DisplayValue", "Unavailable")
        description = item.get("ItemInfo", {}).get("ContentInfo", {}).get("DisplayValue", "Unavailable")
        price = (
            item.get("Offers", {})
                .get("Listings", [{}])[0]
                .get("Price", {})
                .get("DisplayAmount", "Unavailable")
        )
        availability = (
            item.get("Offers", {})
                .get("Listings", [{}])[0]
                .get("Availability", {})
                .get("Message", "Unavailable")
        )
        is_prime_eligible = (
            item.get("Offers", {})
                .get("Listings", [{}])[0]
                .get("DeliveryInfo", {})
                .get("IsPrimeEligible", False)
        )

        return {
            "ASIN": asin,
            "Title": title,
            "Description": description,
            "Price": price,
            "Availability": availability,
            "PrimeEligible": is_prime_eligible
        }
    except (BotoCoreError, ClientError) as error:
        print(f"Error fetching details for ASIN {asin}: {error}")
        return {"ASIN": asin, "Status": "Error"}
