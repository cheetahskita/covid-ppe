# Web Scraping for COVID PPE

In September, 2019, the World Economic Forum [announced a partnership with Uplink](https://www.weforum.org/agenda/2020/09/these-15-innovations-are-helping-us-to-fight-covid-19-and-its-aftermath), an open source collaboration platform, to develop open source solutions to the many problems surrounding the COVID-19 pandemic. One problem was how healthcare providers had difficulty sourcing quality protective equipment from reliable suppliers. Origin Trail, a startup specializing in blockchain technology, [proposed an open source database of COVID PPE](https://uplink.weforum.org/uplink/s/uplink-contribution/a012o00001OSRbUAAX/origintrail-trusted-covid19-essential-supplies-repository) that could provide verifiable credentials on certified medical equipment using blockchain. Due to the variety and scale of medical PPE, Origin Trail needed help sourcing basic information to initially populate their database.

This project collects basic information of COVID PPE by scraping information from the web and records it in tabular form to submit to Origin Trail for their open source database. The biggest challenge in this project was the lack of availability for Universal Product Codes, i.e. UPC Codes or GTIN Numbers. For whatever reason, American suppliers do not list UPC codes in their catalogs, but the UPC Code is essential to tracking a product internationally. Therefore, each product had to be quereied in a generic UPC database (built by a third party using web scrapers) and the most commonly used UPC for a given product was recorded.

In total, 500 unique pieces of equipment were submitted and accepted by Origin Trail from the following suppliers:

### Halyard Health

Link: https://products.halyardhealth.com/infection-prevention.html

Supplies:
* Medical Exam Gloves
* Patient Care
* Facial/Respiratory Protection
* Protective Apparel

### 3M

Link: [https://www.3m.com/3M/en_US/company-us/all-3m-products/~/All-3M-Products/Health-Care/Personal-Protective-Equipment/](https://www.3m.com/3M/en_US/company-us/all-3m-products/~/All-3M-Products/Health-Care/Personal-Protective-Equipment/?N=5002385+8707795+8711017+8720539+3294857497&rt=r3)

Supplies:
* Respirators
* Face Protection
* Protective Apparel
* Protective Eyewear
