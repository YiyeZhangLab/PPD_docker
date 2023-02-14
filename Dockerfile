FROM continuumio/anaconda3

WORKDIR /app

COPY env.yml /app

RUN conda env create -n special -f env.yml

SHELL ["conda", "run", "-n", "special", "/bin/bash", "-c"]


COPY . /app

EXPOSE 12345

# # configure the container to run in an executed manner
ENTRYPOINT ["conda", "run", "-n", "special", "python", "app.py"]

# #ENTRYPOINT [ "python" ]

# CMD ["app.py" ]
