class Flavor:
    def __init__(self, id, sold=False, likes=1):
        self.id = id
        self.sold = sold
        self.likes = likes


class ShopStatistic:
    def __init__(self):
        self.statistic = {}

    def update(self, prefs):
        for flav_id in prefs:
            flavor = self.statistic.get(flav_id, None)
            if flavor is not None:
                flavor.likes += 1
            else:
                self.statistic[flav_id] = Flavor(flav_id)


def sell_lollipops(prefs, shop_statistic):
    if prefs is None:
        print("-1")
        return

    shop_statistic.update(prefs)
    flav_id = sell_correct_lollipop(prefs, shop_statistic)
    print(flav_id)


def sell_correct_lollipop(prefs, shop_statistic):
    customers_flavors = []
    for flav_id in prefs:
        flavor = shop_statistic.statistic.get(flav_id)
        if not flavor.sold:
            customers_flavors.append(flavor)

    if customers_flavors:
        customers_flavors.sort(key=lambda flav: flav.likes)
        customers_flavors[0].sold = True
        return customers_flavors[0].id
    return "-1"


number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N = int(input())

    shop_statistic = ShopStatistic()
    for _ in range(N):
        line = [int(i) for i in input().split()]

        if line == "-1":
            exit()

        D = line[0]
        if D != 0:
            flavors = line[1:]
        else:
            flavors = None
        sell_lollipops(flavors, shop_statistic)
    # print("Case #{}: {}".format(i, res))
