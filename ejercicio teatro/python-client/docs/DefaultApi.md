# swagger_client.DefaultApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**planta_cancelar**](DefaultApi.md#planta_cancelar) | **GET** /planta/cancelar | Cancela la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser cancelada y 0 en caso de que se haya cancelado
[**planta_leer_get**](DefaultApi.md#planta_leer_get) | **GET** /planta/leer | Retorna el estado de la planta
[**planta_vender_get**](DefaultApi.md#planta_vender_get) | **GET** /planta/vender | Vende la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser vendida y 0 en caso de que se haya vendido


# **planta_cancelar**
> int planta_cancelar(fila, columna)

Cancela la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser cancelada y 0 en caso de que se haya cancelado

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fila = 56 # int | Numero de la fila a cancelar
columna = 'columna_example' # str | Columna a cancelar

try: 
    # Cancela la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser cancelada y 0 en caso de que se haya cancelado
    api_response = api_instance.planta_cancelar(fila, columna)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->planta_cancelar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fila** | **int**| Numero de la fila a cancelar | 
 **columna** | **str**| Columna a cancelar | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planta_leer_get**
> list[Butaca] planta_leer_get(fila=fila, columna=columna)

Retorna el estado de la planta

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fila = 56 # int | Numero de la fila a consular (optional)
columna = 'columna_example' # str | Columna a consular (optional)

try: 
    # Retorna el estado de la planta
    api_response = api_instance.planta_leer_get(fila=fila, columna=columna)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->planta_leer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fila** | **int**| Numero de la fila a consular | [optional] 
 **columna** | **str**| Columna a consular | [optional] 

### Return type

[**list[Butaca]**](Butaca.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planta_vender_get**
> int planta_vender_get(fila, columna)

Vende la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser vendida y 0 en caso de que se haya vendido

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
fila = 56 # int | Numero de la fila a vender
columna = 'columna_example' # str | Columna a vender

try: 
    # Vende la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser vendida y 0 en caso de que se haya vendido
    api_response = api_instance.planta_vender_get(fila, columna)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->planta_vender_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fila** | **int**| Numero de la fila a vender | 
 **columna** | **str**| Columna a vender | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

