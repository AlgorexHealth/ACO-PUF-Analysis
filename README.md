# ACO Performance Analysis

The included Jupyter Notebook and data processing scripts consume the [CMS Medicare Shared Savings Program Public Use Files](https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/sharedsavingsprogram/program-data.html).

Files stored in the repository were last downloaded from CMS on May 4, 2019. 

## Using the Repository


To get started clone the repository:

```
git clone https://github.com/AlgorexHealth/ACO-PUF-Anaylysis
cd ACO-PUF-Analysis
```

### Python
To use this repository with Python installed on your machine you will need to install the associated packages. It is recommended  that you do this using a Python virtual environment.  



From here create and initialize a virtual environment. 

```
python3 -m venv venv
source venv/bin/activate
```
Once that is done install the necessary dependent packages from the requirements.txt file. 

```
pip install -r requirements.txt
```

Now you can start a jupyter server and open the notebook

```
jupyter notebook
```


### Docker
If you don't have python installed or just want to isolation in a container, you may also run this repository using docker. If you docker and docker-compose installed from a command line you can simply say:

``` 
docker-compose up 
```

Once the image is downloaded and runnning, (the image size is about 2gb so a little large). You should open a browser and got to [http://localhost:8888/lab](http://localhost:8888/lab) and you should be able to run the notebook there. 

