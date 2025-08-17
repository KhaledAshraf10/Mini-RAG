# MINI-RAG
this is a minimal implementation of the rag model for question answersing

## Rquirments

- python 3.8 or later

#### Install python using miniconda

1. downlaod and install MiniConda from here
2. create a new envirment using the following command :

```bash
$ conda create -n mini-rag python=3,8
```

3. activate the enviroment :

```bash
$ conda activate mini-rag-app
```

### (Optional) Setup you command line interface for better readability

``` bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
## installation 


### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.