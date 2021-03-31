# gui app to quickly see price difference for two outcomes
# don't use floats for real production projects

import traceback
import PySimpleGUI as sg

def diff_calculator(stake_amt, price_before, price_after, price_after_two):
    price_diff = (price_after - price_before) / price_before * 0.999
    price_diff_rounded = round(price_diff * 100, 3)
    profit_loss = round((stake_amt * price_after * 0.999) - (stake_amt * price_before), 2)

    price_diff_two = (price_after_two - price_before) / price_before
    price_diff_two_rounded = round(price_diff_two * 100, 3)
    profit_loss_two = round((stake_amt * price_before * 0.999) * price_diff_two, 2)
    

    print(f'staked: ${stake_amt * price_before} ({int(stake_amt * price_before * 7.78)} hkd)')
    print(f'out ${price_after}:')
    print(f'${profit_loss} ( {int(profit_loss * 7.78)} hkd )')
    print(f'{round(price_diff_rounded, 1)}%')
    print('')
    print(f'out ${price_after_two}:')
    print(f'${profit_loss_two} ( {int(profit_loss_two * 7.78)} hkd )')
    print(f'{round(price_diff_two_rounded, 1)}%')
    print('---')


layout = [
    [sg.Text('Stake Amt:'), sg.InputText(key='_STAKE_AMT_', size=(15, 1))],
    [sg.Text('Entry Price:'), sg.InputText(key='_PRICE_BEFORE_', size=(15, 1))],
    [sg.Text('Exit Price 1:'), sg.InputText(key='_PRICE_AFTER_', size=(15, 1))],
    [sg.Text('Exit Price 2:'), sg.InputText(key='_PRICE_AFTER_TWO_', size=(15, 1))],
    [sg.Text('')],
    [sg.Button("Calculate", size=(10, 1), bind_return_key=True, key='_CALCULATE_')],
    [sg.Output(size=(60, 10))],
]

window: object = sg.Window('Price Diff Calculator', layout, element_justification='left')

try:
    while True:
        event, values = window.read()
        if event is None:
            break
        if event == '_CALCULATE_':
            STAKE_AMT = float(values['_STAKE_AMT_'])
            PRICE_BEFORE = float(values['_PRICE_BEFORE_'])
            PRICE_AFTER = float(values['_PRICE_AFTER_'])
            PRICE_AFTER_TWO = float(values['_PRICE_AFTER_TWO_'])


            if STAKE_AMT == '' or PRICE_BEFORE == '' or PRICE_AFTER == '' or PRICE_AFTER_TWO == '':
                print('Stake Amt or Entry price cannot be empty')
            elif PRICE_AFTER == '' and PRICE_AFTER_TWO == '':
                print('Both Exit prices cannot be empty')
            else:
                diff_calculator(STAKE_AMT, PRICE_BEFORE, PRICE_AFTER, PRICE_AFTER_TWO)
except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened. Here is the info:', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)