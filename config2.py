#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA = []

CATEGORICAL_VARS_WITH_NA_FREQ = ['Customer Lname']

#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = []

#Variables para hacer mapeo categorico 
DELIVERY_VARS =  ['Delivery Status']
SEGMENT_VARS = ['Customer Segment']
COUNTRY_VARS = ['Customer Country']
SHIPPING_VARS = ['Shipping Mode']
MARKET_VARS = ['Market']

#Mapeos de variables categoricas
DELIVERY_MAP = {'Advance shipping':1, 'Late delivery':2, 'Shipping canceled':3, 'Shipping on time':4, 
                    'Missing':0, 'NA':0, 'NaN':0}
SEGMENT_MAP = {'Consumer':1, 'Corporate':2, 'Home Office':3, 'Missing':0, 'NA':0, 'NaN':0}
COUNTRY_MAP = {'EE. UU.':1, 'Puerto Rico':2, 'Missing':0, 'NA':0, 'NaN':0}
SHIPPING_MAP = {'First Class':1, 'Same Day':2, 'Second Class':3, 'Standard Class':4, 'Missing':0, 'NA':0, 'NaN':0}
MARKET_MAP = {'Africa':1, 'Europe':2, 'LATAM':3, 'Pacific Asia':4, 'USCA':5, 'Missing':0, 'NA':0, 'NaN':0}

#Variables seleccionadas según análisis de Lasso
FEATURES = ['Order Item Product Price', 'Sales', 'Order Item Total','Product Price']

#Variables a eliminar
DROP_VAR=  ['Customer Lname', 'Customer City', 'Customer State', 'Order City', 'Order Country', 'Order State',
           'Product Name', 'Order Status']