# Converts magento's customer_entity & customer_address_entity tables into prestashops ps_customer & ps_address tables.

## 1. use this sql to get magento's user data, and export as csv:
## SELECT ce.entity_id, ce.prefix, ce.firstname, ce.lastname, ce.email, ce.store_id, ce.created_at, ce.updated_at, mr.points_balance, cae.city, cae.company, cae.country_id, cae.postcode, cae.region, cae.street, cae.telephone FROM magento_reward as mr INNER JOIN customer_entity as ce ON mr.customer_id=ce.entity_id INNER JOIN customer_address_entity as cae ON ce.entity_id=cae.parent_id
# make sure to exclude customer's csv files from version control

import csv

with open('magento_reward.csv', encoding="utf8") as csvfile:
    #     ps_customer schema:
    #     'id_customer', 'id_shop_group', 'id_shop', 'id_gender', 'id_default_group', 0 - 4
    #     'id_lang', 'id_risk', 'company', 'siret', 'ape', 5 - 9
    #     'firstname', 'lastname', 'email', 'passwd', 'last_passwd_gen', 10 - 14
    #     'birthday', 'newsletter', 'ip_registration_newsletter', 'newsletter_date_add', 'optin', 15 - 19
    #     'website', 'outstanding_allow_amount', 'show_public_prices', 'max_payment_days', 'secure_key', 20 - 24
    #     'note', 'active', 'is_guest', 'deleted', 'date_add', 25 - 29
    #     'date_upd', 'reset_password_token', 'reset_password_validity' 30 -32
    readCSV = csv.reader(csvfile, delimiter=',')
    with open('output_ps_customer.csv', mode='w', newline='', encoding="utf8") as output_file:
        output_writer = csv.writer(output_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        next(readCSV) # skip first line
        for row in readCSV:
            output_writer.writerow([f'{row[0]},1,1,0,3,{row[5]},0,{row[10]},,,{row[2]},{row[3]},{row[4]},,2020-04-15 17:08:32,NULL,1,,0,0,0,,1,0,0,{row[6]},{row[7]},,NULL'])


with open('magento_reward.csv', encoding="utf8") as csvfile:
    # ps_address schema:
    # id_address, id_country, id_state, id_customer, id_manufacturer 0 - 4
    # id_supplier, id_warehouse, alias, company, lastname 5 - 9
    # firstname, address1, address2, postcode, city 10 - 14
    # other, phone, phone_mobile, vat_number, dni   15 - 19
    # date_add, date_upd, active, deleted  20 - 23
    readCSV = csv.reader(csvfile, delimiter=',')
    with open('output_ps_address.csv', mode='w', newline='', encoding="utf8") as output_file:
        output_writer = csv.writer(output_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        next(readCSV) # skip first line
        for index, row in enumerate(readCSV):
            # print(index)
            output_writer.writerow([f'{index}, {row[11]}, {row[13]}, {row[0]}, 0, 0, 0, my address, {row[10]}, {row[3]}, {row[2]}, {row[14]}, {row[12]}, {row[12]}, {row[9]}, NULL, {row[15]}, {row[15]}, 0, 0, {row[6]}, {row[7]}, 1, 0'])