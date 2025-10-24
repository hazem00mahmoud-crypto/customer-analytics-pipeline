FROM python:3.11-slim

RUN pip install pandas numpy matplotlib seaborn scikit-learn scipy requests

RUN mkdir -p /app/pipeline

WORKDIR /app/pipeline

COPY . .

CMD ["/bin/bash"]