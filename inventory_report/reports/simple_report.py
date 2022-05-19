from datetime import datetime
from statistics import mode


class SimpleReport:
    def generate(data):
        old_date = min([products["data_de_fabricacao"] for products in data])

        current_date = datetime.now().strftime("%Y-%m-%d")

        closest_expiration_date = min([
            products["data_de_validade"]
            for products in data
            if products["data_de_validade"] > current_date
        ])

        most_common_company = mode([
            company["nome_da_empresa"] for company in data
          ])

        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{most_common_company}\n"
        )

# Na Linha 9, o strftime() transforma a hora atual em
# string para comparação da linha 11-15
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# O mode() da linha 17, retorna o valor mais comum
# https://docs.python.org/pt-br/dev/library/statistics.html
