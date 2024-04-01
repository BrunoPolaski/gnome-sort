[![Tests](https://github.com/wOL-Lucas/gnome-sort/actions/workflows/workflow.yaml/badge.svg)](https://github.com/BrunoPolaski/gnome-sort/actions/workflows/workflow.yaml)


## [Website](http://gnomesort.wollucas.com/views/index.html)

<div>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" width=50px height=50px/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width=50px height=50px/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original-wordmark.svg" width=75px height=75px/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-plain.svg" width=50px height=50px/>
</div>
          

## Install dependencies

```
pip install -r requirements.txt
```


## run fastapi app
```
uvicorn app:app --reload
```



# Métricas
-------------------------------------------------------
<div style="text-align: center;">

**Métricas - Array Aleatório Desordenado**

| Tamanho | Tempo (segundos) | Tempo (minutos) |
|---------|------------------|-----------------|
| 100     | 0.002002239227294922 | 0.0000333706537882487 |
| 1000    | 0.13268589973449707 | 0.0022114316622416184 |
| 10_000  | 10.016445636749268 | 0.1669407606124878 |
| 100_000 | 1012.2218880653381 | 16.87036480108897 |
| 1_000_000 | 39600 ++ | 660 ++ |



**Métricas - Array Ordenado de Forma Decrescente**

| Tamanho | Tempo (segundos) | Tempo (minutos) |
|---------|------------------|-----------------|
| 100     | 0.0019979476928710938 | 0.000033299 |
| 1000    | 0.15919280052185059 | 0.002653213 |
| 10_000  | 20.290143728256226 | 0.338169062 |
| 100_000 | 1968.486481666565 | 32.808108028 |
| 1_000_000 | 39600 ++ | 660 ++ |



**Métricas - Array Ordenado de Forma Crescente**

| Tamanho | Tempo (segundos) | Tempo (minutos) |
|---------|------------------|-----------------|
| 100     | 0.0 | 0.0 |
| 1000    | 0.0 | 0.0 |
| 10_000  | 0.0 | 0.0 |
| 100_000 | 0.005509376525878906 | 0.000091823 |
| 1_000_000 | 0.3135685920715332 | 0.005226143 |



**Métricas - Array Quase Ordenado**

| Tamanho | Tempo (segundos) | Tempo (minutos) |
|---------|------------------|-----------------|
| 100     | 0.0 | 0.0 |
| 1000    | 0.0 | 0.0 |
| 10_000  | 0.0010018348693847656 | 0.000016697 |
| 100_000 | 0.005999088287353516 | 0.000099985 |
| 1_000_000 | 0.2364366054534912 | 0.00394061 |



</div>

