# importing module phonenumbers
import pandas as pd # data processing
pd.options.mode.chained_assignment = None  # default='warn'
import pycountry , phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number


##############################################
## load file 
df = pd.read_csv("country_codes.csv")
print (df.shape)
df.head()

df['numbers_with_plus']='+'+df['Phone']
df['country_name']=df['Country']



        
for i in range(0,len(df.numbers_with_plus)):
    var=df.numbers_with_plus[i]
    new_col='country_name'
    try:
        pn = phonenumbers.parse(var)
        country = pycountry.countries.get(alpha_2 = region_code_for_number(pn))
    except:
        continue
    else:
        if(country):
            df[new_col][i]=country.name
            
            
df.to_excel("country_codes_new_2.xlsx")