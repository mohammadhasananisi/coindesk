from pandas import DataFrame, concat
import requests


def clone_mobile_data():
    df = DataFrame()
    page = 1
    while True:
        url = (
            "https://api.digikala.com/v1/recommendation/personalized-category/mobile-phone/?page="
            + str(page)
        )

        response = requests.get(url)
        data = response.json()

        df_c = DataFrame(data["data"]["products"])
        if df_c.empty:
            break

        # df_c['selling_price'] = df_c['default_variant'].apply(lambda x: x['price']['selling_price'])

        df_c = df_c[
            [
                "id",
                "title_fa",
                "title_en",
                # 'selling_price'
            ]
        ]
        df = concat([df, df_c], ignore_index=True)
        page += 1
        if data["data"]["pager"]["current_page"] == data["data"]["pager"]["total_pages"]:
            break

    base_url = "https://api.digikala.com/v1/product/"

    def find_other_price(x):
        url = base_url + str(x["id"]) + "/"
        r = requests.get(url)
        data = r.json()
        data = data["data"]["product"]["variants"]
        color_list = {
             "مشکی": 'black',
            "سفید": 'white',
             "صورتی": 'pink',
            "طلایی": 'gold',
             "نقره ای": 'silver',
        }
        price = {}
        for d in data:
            if d["color"]["title"] in color_list.keys():

                color_en = color_list[d["color"]["title"]]
                
                x[color_en] = {
                    "seller": d["seller"]["title"],
                    "selling_price": d["price"]["selling_price"],
                    "rrp_price": d["price"]["rrp_price"],
                }

            # selling_price = d['price']['selling_price']
            # rrp_price = d['price']['rrp_price']
            # print(selling_price, rrp_price)
            # print(d['color']['title'])
            # print(d['seller']['title'])
        if len(price) == 0:
            price = {}
        # concat price to df with **price
        # x = concat([x, DataFrame(price)], axis=1)
        # print(x)
        return x

    # for in every df
    df = df.apply(find_other_price, axis=1)
    df.dropna(inplace=True)
    # print(df)
    return df.to_dict("records")




# if __name__ == "__main__":
#     clone_mobile_data()