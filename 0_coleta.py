# Coleta de dados da API do Poder360
import pandas as pd
import requests
import os

def pega_pesquisas(ano, cargo):

    # Cria dir para salvar dados brutos
    if not os.path.exists("raw_data"):
        os.makedirs("raw_data")

    # GET
    token = {"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjY3M2U1YmMzNDFjMzBlNTJjMDQ4YzIwNTJhY2M1MTk3N2QxNDA5ZjM4YjlmYjM2MzMyNmUzZjRkMGM4NmRlNGY5MTYwNzE4M2IyMThlZmYzIn0.eyJhdWQiOiIxIiwianRpIjoiNjczZTViYzM0MWMzMGU1MmMwNDhjMjA1MmFjYzUxOTc3ZDE0MDlmMzhiOWZiMzYzMzI2ZTNmNGQwYzg2ZGU0ZjkxNjA3MTgzYjIxOGVmZjMiLCJpYXQiOjE1ODk5MTEzODgsIm5iZiI6MTU4OTkxMTM4OCwiZXhwIjoxNjIxNDQ3Mzg4LCJzdWIiOiI0OCIsInNjb3BlcyI6W119.cAT_Gq0BIQpGFR5kj5fjEecB70E1A3UdnwLmqNPFpvNj9dYzZZ8Wb0rqIbwgPYEA7iGeQJUW49EK2clRn1J2EPFykbfaEhDJ_9Avobo6rNRiYHZf6_Teh9l_-O9GGWbfma6iSdNB2Vh-sp67hs8ZcfQ0LeOyTRyzh-I3NYDxldc0I6O9haoemm8nW8ScOkt13l4NchKYEtNHYJqpqRfFHSxvi0hsBj2lcSEJ-aiIvtsutBw2SJGm_aNlLjsw_mDXbr5h1VC0PadBfcrcvg134vLJyswADvNiNrvZ_nC_wWnj2BpC-DV01sh2tDlthIfyhuP7qbSUmLdfYej6Gy2iYkGN3xE5M6h4W-2-j-oQ7IjnSWm3WGOCXUsRQ0cDX67vnRMQj7MNMIb_OGXMrPyjCa-fTBPO6-qPQX7nplxaNeMKp-BGYICeU6857CisCbl9bEI3DD0zKNk0RGAlJgAb2393DdJPmk1vH-8l4lZuFFZBoVH_W4AHgFl-JjYtUVJ9YMu0Azd5hCUSmtboIbAFXLUxdNAyOpneL9FLMOxgRgKL-UV6U_CzLyOPIrthCYpb7oJWq7h1cwPQhElVe9bEgo3F1wtWidiq_TR5_V2d8TrOzToLVjk7CgnwrOVOCfzdDgGSRd-vORTMpPTQP3-AW6jhcwIzPmV_jZyyvplFmtI"}
    endpoint = "https://pesquisas.poder360.com.br/api/consulta/fetch/"
    queries = {"ano" : ano, "cargos_id" : cargo}

    r = requests.get(endpoint, params = queries, headers = token).json()

    # Exporta os dados brutos
    pd.DataFrame(r).to_csv("raw_data/pesquisas.csv", sep = ";", index = False)

pega_pesquisas(2022, 3)
    