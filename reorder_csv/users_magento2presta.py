# Converts magento's customer_entity & customer_address_entity tables into prestashops ps_customer & ps_address tables.

## 1. use this sql to get magento's user data, and export as csv:
## SELECT ce.entity_id, ce.prefix, ce.firstname, ce.lastname, ce.email, ce.store_id, ce.created_at, ce.updated_at, mr.points_balance, cae.city, cae.company, cae.country_id, cae.postcode, cae.region, cae.street, cae.telephone FROM magento_reward as mr INNER JOIN customer_entity as ce ON mr.customer_id=ce.entity_id INNER JOIN customer_address_entity as cae ON ce.entity_id=cae.parent_id
# make sure to exclude customer's csv files from version control

import csv
import secrets


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

        for index, row in enumerate(readCSV):

            # generate 32 varchar secret key
            secret_key = secrets.token_hex(16)
            reset_key = secrets.token_hex(20)

            # skip rows with 0 points
            if row[8] == '0':
                continue
            else:

                # assigns value for gender
                if row[1] in ('Mr', 'Mr ', 'MR', '先生'):
                    row[1] = 1
                elif row[1] in ('Ms', 'Mrs', '女士', 'Ms.', '太太'):
                    row[1] = 2
                else:
                    row[1] = 'NULL'

                output_writer.writerow([f'{row[0]},1,1,{row[1]},3,{row[5]},0,NULL,NULL,NULL,{row[2]},{row[3]},{row[4]},,2020-04-15 17:08:32,NULL,1,NULL,NULL,0,NULL,0,1,0,{secret_key},NULL,1,0,0,{row[6]},{row[7]},{reset_key},2024-01-01 11:11:11'])


with open('magento_reward.csv', encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    with open('output_points.csv', mode='w', newline='', encoding="utf8") as output_file:
        output_writer = csv.writer(output_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        next(readCSV) # skip first line
        
        for index, row in enumerate(readCSV):
            # skip rows with 0 points
            if row[8] == '0':
                continue
            else:
                output_writer.writerow([f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[8]}, {row[6]}, {row[7]}'])
