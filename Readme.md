# ECB Currency Scraper
Welcome! 
This is `Readme` for ECB (European Central Bank) Currency Scraper API in Django.

Accordingly to assignment the task was designed to take around 3-hours, the code/application is more really an outline for the project to build up on. However it consists of basic features that present the desierd functionalities and possible final outcome. All was achieved within given timeframe with some breaks in between. 
It has been a while since I coded in Django (1.5 year or so) and did not manage to finalize all parts i would like to finish. Further work is mentioned in TODO List section.

Project is written in Django 2.1.4 and Python 3.
Author: *Tobiasz Kukawka*
##### Explanation includes following sections:
* Requirements
* Run Project
* API
* Database
* TODO List
    
# Requirements:
In order to set requirements for the project you need python's virtualenv tool. If you satisfy this requirement please follow the steps below:
1. Create virtualenv directory
```
virtualenv venv
```
2. Install Requirements:
```
pip install -r ./requirements.txt
```
3. Activate virtual environment:
```
source venv/bin/activate
```

Now you are ready to go to launch the project.

# Run Project:
Project can be executed right away after cloning it from github repository with a basic database/migrations and some data.

In order to run the project execute:
```
python ./scraper/manage.py runserver 8000
```
You can specify different `port` if `8000` is taken.

After starting the project, the scraper thread will run in the background everyhour to scrape for any new records. 
The code is located under `ecb/tasks.py`. The thread itself is started while loading the `ecb/urls.py`

# API - ECB
Corresponding code for ECB Api is located under `scraper/ecb`

One and only API is located under url
`http://localhost:8000/ecb/feed/currency/`
The API returns all currency data that it managed to gather since the start/records in the database in the json format.

##### Filter Params
There are two filter params available for the API Call:
1. *target* - target currency that you are requesting data for. It is available from the set of:
  ['PLN', 'GBP', 'USD', 'CZK', 'DKK', 'HUF']. It can be easily extended to additional currencies by extending the list located under `/scraper/ecb/settings.py`. The example of request: `http://127.0.0.1:8000/ecb/feed/currency/?target=PLN`
2. *date* - exact date to filter on the results. Passed in format `Y-M-D` e.g. `http://127.0.0.1:8000/ecb/feed/currency/?date=2018-12-14`

If unexpected params are passed or in incorrect form, errors will be raised.

# Database
For the purpose of 1 API call the database for currencies feed is basic and simple. It is just an idea how it can be implemented and extended to enrich it with more fields. The outline is as follows:

`RSSFeedModel` consissts of following fields:
* target = models.CharField(max_length=5, blank=True, null=True)
* date = models.DateTimeField(default=None, blank=True, null=True)
* link = models.URLField(default=None, blank=True, null=True)  
* exchange_rate = models.CharField(max_length=20, blank=True, null=True)
* title = models.CharField(max_length=100, blank=True, null=True)  
* summary = models.CharField(max_length=200, blank=True, null=True)


# TODO List
1. Serializers - serializers should be added on the filter parameters to improve the control over the parameters and their values.
2. Validation/Filtering of data should be moved into separate part of the view-handling
3. Extend Database with more fields as just couple was picked up.
4. Improve Database Model + Fields definitions (types, char lengts etc)
5. Format returned in a more readible structure e.g. without "model" and "pk" fields
6. Add Unit and Integration tests for the code/models as well as the api itself.
7. Improve Error Handling and Raised Errors
8. Format code accordingly to given standards (e.g. lint)
9. Sort/fix imports