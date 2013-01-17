mydict = {'mainkey':[
                     {'subkey':'want_this','other_data':'my_other_data_i_want'},
                     {'subkey':'dont_want_this','other_data':'not_interested'}
                     ],
          'other_key':'do not show this'
          }

main_data = mydict['mainkey']
for data in main_data:
    if data['subkey'] == 'want_this':
        data_i_want = data
        
print mydict['doesnthave']['reallydoesnthave']
