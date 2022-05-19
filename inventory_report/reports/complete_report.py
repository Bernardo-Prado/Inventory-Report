from datetime import datetime
from statistics import mode


class CompleteReport:
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

        companies = [products["nome_da_empresa"] for products in data]

        companies_quantity = []

        filtered_companies_quantity = []

        unordered_companies_list = ''

        for company in companies:
            companies_quantity.append(f"{company}: {companies.count(company)}")

        for company in companies_quantity:
            if company not in filtered_companies_quantity:
                filtered_companies_quantity.append(company)

        for company in filtered_companies_quantity:
            unordered_companies_list += f"- {company}\n"

        return(
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{most_common_company}\n\n"
            "Produtos estocados por empresa: \n"
            f"{unordered_companies_list}"
        )
