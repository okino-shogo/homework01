def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    temperature_sum = 0
    city_kazu = len(weather_information)
    for city in weather_information:
        temperature_sum += city["temperature"]
        temperature_ave = temperature_sum / city_kazu
    print(temperature_ave)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    resulet = []
    for osaka_city in weather_information:
        if osaka_city["prefecture"] == "大阪府":
            osaka_station = osaka_city["station"]
            resulet.append(osaka_station)
    print(resulet)
    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)

    fuku_tem_sum = 0
    count = 0
    for fukuoka_city in weather_information:
        if fukuoka_city["prefecture"] == "福岡県":
            fukuoka_temperature = fukuoka_city["temperature"]

            fuku_tem_sum += fukuoka_temperature
            count += 1
    fuku_tem_ave = fuku_tem_sum / count

    print(fuku_tem_ave, end="")


if __name__ == "__main__":
    main()
