import csv

with open('magento_reward.csv', encoding="utf8") as csvfile:
    # print([
    #     'id_customer', #0
    #     'id_shop_group',
    #     'id_shop',
    #     'id_gender',
    #     'id_default_group',
    #     'id_lang', #5
    #     'id_risk',
    #     'company',
    #     'siret',
    #     'ape',
    #     'firstname', #10
    #     'lastname',
    #     'email',
    #     'passwd',
    #     'last_passwd_gen',
    #     'birthday', #15
    #     'newsletter',
    #     'ip_registration_newsletter',
    #     'newsletter_date_add',
    #     'optin',
    #     'website', #20
    #     'outstanding_allow_amount',
    #     'show_public_prices',
    #     'max_payment_days',
    #     'secure_key',
    #     'note', #25
    #     'active',
    #     'is_guest',
    #     'deleted',
    #     'date_add',
    #     'date_upd', #30
    #     'reset_password_token',
    #     'reset_password_validity'
    #     ])
    readCSV = csv.reader(csvfile, delimiter=',')

    with open('output_file.csv', mode='w', newline='', encoding="utf8") as output_file:
        output_writer = csv.writer(output_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        next(readCSV) # skip first line
        for row in readCSV:
            output_writer.writerow([f'{row[0]},1,1,0,3,{row[5]},0,{row[10]},,,{row[2]},{row[3]},{row[4]},,2020-04-15 17:08:32,NULL,1,,0,0,0,,1,0,0,{row[6]},{row[7]},,NULL'])
