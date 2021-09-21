FROM python:3-onbuild  

#copy over to image --- the onbuild image expects files in dir: /usr/src/app
COPY . /usr/src/app

# Commands in a list
CMD ["python", "api.py"]